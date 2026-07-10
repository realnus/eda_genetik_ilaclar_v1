"""review.py — TERFİ-ANI DANIŞMAN DEĞERLENDİRME (insan-yüzlü LLM katmanı).
Bir öneri onkoloğa gitmeden önce, kuralların kaçırabileceği klinik İŞARETLERİ çıkarır.
KARAR VERMEZ, deterministik kaydı EZMEZ, kanıt UYDURMAZ — yalnız işaret + onkoloğa soru üretir.

Yalnız TERFİ ANINDA çalışır (her taramada değil). Bu ortamda host.llm; sunucuda LLM API'si.
"""
import json, re

SYSTEM = ("Sen bir nöro-onkoloji danışmanısın. Sana bir ilaç terfi önerisinin YAPILANDIRILMIŞ verileri "
 "verilir. Görevin KARAR VERMEK DEĞİL, yalnızca kuralların kaçırmış olabileceği klinik İŞARETLERİ "
 "çıkarmak: kanıt gücü abartılmış mı, gözden kaçan kontrendikasyon/DDI var mı, toksisite örtüşmesi "
 "endişe verici mi, KBB verisi yeterince sağlam mı. Sağlanan veriyi AŞMA, yeni kanıt uydurma. Kısa ve somut ol.")

def _facts(con, drug_name, combo_id, vuln_id):
    import os
    cur=con.cursor()
    q=lambda s,a=(): cur.execute(s.replace("?","%s") if os.environ.get("DB_BACKEND")=="postgres" else s,a)
    q("SELECT bbb_class,bbb_confidence,dose_gap_ratio FROM pharmacology p JOIN drug d ON d.drug_id=p.drug_id WHERE d.name=?",(drug_name,))
    ph=cur.fetchone() or (None,None,None)
    q("SELECT boxed,organ_load,qt_flag FROM toxicity t JOIN drug d ON d.drug_id=t.drug_id WHERE d.name=?",(drug_name,))
    tx=cur.fetchone() or (0,"{}",0)
    q("SELECT evidence_level,direction,verified,doi FROM evidence e JOIN drug d ON d.drug_id=e.drug_id WHERE d.name=?",(drug_name,))
    ev=cur.fetchone()
    return {"aday":drug_name,"zayiflik":vuln_id,"kombinasyon":combo_id,
            "tekil_toksisite":tx[1],"kutu_uyari":bool(tx[0]),"qt":bool(tx[2]),
            "kbb":f"{ph[0]} (güven {ph[1]})","dose_gap":ph[2],
            "kanit":(f"{ev[0]} · yön={ev[1]} · {'doğrulandı' if ev and ev[2] else 'doğrulanmadı'} · DOI {ev[3]}" if ev else "kanıt yok"),
            "hasta_notlari":"Lamide (lakozamid, QT dikkat); Keppra; Altuzan (bevacizumab, V7/V8)"}

def review_promotion(con, drug_name, combo_id, vuln_id, llm_call):
    """llm_call: (prompt, system) -> metin. Bu ortamda: lambda p,s: host.llm(p,system=s,model=host.reasoning_model())['text']"""
    facts=_facts(con, drug_name, combo_id, vuln_id)
    prompt=("Terfi önerisi verileri:\n"+json.dumps(facts,ensure_ascii=False,indent=1)+
     "\n\nŞu JSON'u döndür (yalnız JSON): "
     '{"genel":"onayla-dikkatle|ihtiyatlı|itiraz","isaretler":["..."],"onkologa_soru":["..."]}')
    txt=llm_call(prompt, SYSTEM).strip()
    m=re.search(r'\{.*\}', txt, re.S)
    if not m: return {"genel":"ihtiyatlı","isaretler":["değerlendirme ayrıştırılamadı"],"onkologa_soru":[]}
    try: return json.loads(m.group(0))
    except Exception: return {"genel":"ihtiyatlı","isaretler":["JSON hatası"],"onkologa_soru":[]}
