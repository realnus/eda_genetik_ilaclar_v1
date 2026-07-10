"""verify.py — KANIT DOĞRULAMA KAPISI (bu ortamda MCP/OpenAlex ile çalışır).

Bu ortamda OpenAlex çağrısı `repl` tool'undan host.mcp("literature", ...) ile yapılır.
Bir sunucuda ise doğrudan HTTPS: GET https://api.openalex.org/works/doi:<doi>?api_key=$OPENALEX_API_KEY

Kural (terfi kapısı):
  - Öneri terfi edilebilmesi için adayın EN AZ BİR doğrulanmış (verified=1) kanıtı olmalı.
  - Kanıt yönü 'does_not_support' veya seviyesi 'randomize-negatif' ise aday DÜŞÜRÜLÜR (terfi engellenir).
  - DOI'si olmayan / doğrulanmamış aday 'ön-aday' kalır; rapora '⚠ doğrulanmadı' etiketiyle girer.
"""
import os

NEGATIVE_LEVELS = {"randomize-negatif"}
NEGATIVE_DIRECTIONS = {"does_not_support"}

def evidence_status(con, drug_id):
    """Bir adayın kanıt durumunu özetle. Dönüş: dict."""
    cur=con.cursor()
    q = "SELECT doi,title,year,evidence_level,direction,verified FROM evidence WHERE drug_id=?"
    cur.execute(q.replace("?","%s") if os.environ.get("DB_BACKEND")=="postgres" else q, (drug_id,))
    rows=cur.fetchall()
    if not rows:
        return {"status":"kanıt-yok","promotable":False,"label":"⚠ kanıt yok","evidence":[]}
    verified=[r for r in rows if r[5]==1]
    negative=[r for r in rows if (r[3] in NEGATIVE_LEVELS or r[4] in NEGATIVE_DIRECTIONS)]
    if negative:
        return {"status":"negatif-kanıt","promotable":False,
                "label":"⛔ negatif kanıt (terfi engellendi)","evidence":rows}
    if verified:
        return {"status":"doğrulandı","promotable":True,
                "label":f"✅ doğrulandı ({verified[0][3]}, {verified[0][2]})","evidence":rows}
    return {"status":"doğrulanmadı","promotable":False,
            "label":"⚠ kanıt var ama doğrulanmadı","evidence":rows}

def verify_doi_openalex(doi):
    """Üretim: OpenAlex ile DOI gerçek mi + başlık/yıl. Bu ortamda repl'den host.mcp kullanın:
       host.mcp("literature","openalex_get_work", work_id=doi) -> {title, publication_year, ...}
       Sunucuda: requests.get(f"https://api.openalex.org/works/doi:{doi}",
                 params={"api_key": os.environ["OPENALEX_API_KEY"]})
    """
    raise NotImplementedError("repl: host.mcp('literature','openalex_get_work', work_id=doi)")
