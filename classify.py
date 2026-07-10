"""classify.py — KANIT-YÖNÜ SINIFLANDIRMASI (boru-hattı-içi LLM).
verify.py'nin 'check_direction' açığını kapatır: bir makale VAR olabilir ama sonucu ilacı
DESTEKLEMİYOR olabilir (bu projede: DIRECT randomize-negatif, PTEN DOES_NOT_SUPPORT).

Bu ortamda LLM çağrısı host.llm ile yapılır (repl). Sunucuda: Anthropic/OpenAI API'sine
aynı prompt+system ile POST edin; API anahtarı env'den ($ANTHROPIC_API_KEY vb.).

KRİTİK KURAL: özet yoksa/yetersizse → 'belirsiz' döner, ASLA yön uydurmaz. 'belirsiz' ve
'does_not_support' terfi kapısında adayı DÜŞÜRÜR (promotable=False).
"""
import json, re

SYSTEM = ("Sen bir onkoloji-kanıt sınıflandırıcısısın. Sana bir çalışma başlığı ve özeti verilir. "
 "Yalnızca sağlanan metne dayanarak, çalışmanın söz konusu ilacın ilgili endikasyondaki kullanımını "
 "DESTEKLEYİP desteklemediğini sınıflandır. Metin yetersizse 'belirsiz' de, ASLA uydurma.")

def _prompt(title, abstract):
    return (f"BAŞLIK: {title}\n\nÖZET: {abstract if abstract else '(özet mevcut değil)'}\n\n"
     "Şu JSON'u döndür (yalnız JSON): "
     '{"direction":"supports|does_not_support|mixed|belirsiz","confidence":"yuksek|orta|dusuk","gerekce":"tek cümle"}')

def classify_direction(title, abstract, llm_call):
    """llm_call: (prompt, system) -> metin döndüren çağrılabilir.
    Bu ortamda: lambda p,s: host.llm(p, system=s)['text']
    Sunucuda:   Anthropic messages API sarmalayıcısı."""
    txt = llm_call(_prompt(title, abstract), SYSTEM).strip()
    m = re.search(r'\{.*\}', txt, re.S)
    if not m:
        return {"direction":"belirsiz","confidence":"dusuk","gerekce":"sınıflandırma ayrıştırılamadı"}
    try:
        d = json.loads(m.group(0))
        if d.get("direction") not in ("supports","does_not_support","mixed","belirsiz"):
            d["direction"]="belirsiz"
        return d
    except Exception:
        return {"direction":"belirsiz","confidence":"dusuk","gerekce":"JSON hatası"}

def update_evidence_direction(con, evidence_id, title, abstract, llm_call):
    """Bir kanıt kaydının yön alanını sınıflandırıp DB'ye yazar."""
    import os
    d = classify_direction(title, abstract, llm_call)
    q = "UPDATE evidence SET direction=? WHERE evidence_id=?"
    cur=con.cursor()
    cur.execute(q.replace("?","%s") if os.environ.get("DB_BACKEND")=="postgres" else q,(d["direction"],evidence_id))
    con.commit()
    return d
