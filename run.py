"""run.py — bir sürveyans çalıştırması + KANIT-DOĞRULAMA-FARKINDA ilerleme raporu.
Kullanım: DB_BACKEND=sqlite DB_PATH=gbm_eda.db PYTHONPATH=. python run.py
Her öneri, adayın kanıt durumuyla (✅ doğrulandı / ⚠ doğrulanmadı / ⛔ negatif) etiketlenir.
Klinik dosyalar otomatik güncellenmez — yalnız 'promotable' öneriler onay için sunulur.
"""
import os, json, db, engine, verify, promote

def _q(cur,s,a=()): cur.execute(s.replace("?","%s") if db.BACKEND=="postgres" else s, a); return cur

def report(con, run_id):
    cur=con.cursor()
    _q(cur,"SELECT run_at,n_candidates,n_proposals,note FROM run_log WHERE run_id=?", (run_id,))
    rl=cur.fetchone()
    _q(cur,"""SELECT p.combo_id,di.name,dc.name,dc.drug_id,p.axis_gains,mn.vuln_id,mn.node_name,p.rationale,dc.access_track
              FROM proposal p LEFT JOIN drug di ON di.drug_id=p.incumbent_drug_id
              JOIN drug dc ON dc.drug_id=p.candidate_drug_id
              LEFT JOIN mechanism_node mn ON mn.node_id=p.node_id
              WHERE p.run_id=? ORDER BY p.combo_id""",(run_id,))
    rows=cur.fetchall()
    subs=[r for r in rows if r[7]=="substitution"]; gaps=[r for r in rows if r[7]=="gap-fill"]
    def vlabel(did): return verify.evidence_status(con, did)["label"]
    L=[f"# İteratif İlerleme Raporu — Çalıştırma #{run_id}",
       f"**Tarih:** {rl[0]} · **Taranan aday:** {rl[1]} · **Öneri:** {rl[2]} · **Not:** {rl[3]}\n",
       "Otomatik üretildi. Yalnız **✅ doğrulanmış** öneriler terfi edilebilir; **⚠/⛔** etiketliler onkolog "
       "değerlendirmesi öncesi kanıt doğrulaması bekler. Klinik dosyalar onay olmadan değişmez.\n",
       "## 1) İkame önerileri (mevcut → daha iyi)\n"]
    if subs:
        L+=["| Kombinasyon | Düğüm | Mevcut | → Öneri | Kanıt | Neden (regresyonsuz) |","|---|---|---|---|---|---|"]
        L+=[f"| {r[0]} | {r[5]} {r[6]} | {r[1]} | **{r[2]}** [{r[8]}] | {vlabel(r[3])} | {', '.join(json.loads(r[4]))} |" for r in subs]
    else: L.append("_Yok._")
    L.append("\n## 2) Boşluk-doldurma önerileri (kapanmayan düğümü doğrudan vur)\n")
    if gaps:
        L+=["| Kombinasyon | Zayıflık/Düğüm | + Aday | Erişim | Kanıt | Gerekçe |","|---|---|---|---|---|---|"]
        L+=[f"| {r[0]} | {r[5]} {r[6]} | **{r[2]}** | {r[8]} | {vlabel(r[3])} | {json.loads(r[4])[0]} |" for r in gaps]
    else: L.append("_Yok._")
    # promotable summary
    prom=[r for r in rows if verify.evidence_status(con,r[3])["promotable"]]
    L.append(f"\n## 3) Terfi edilebilir (kanıtı doğrulanmış) öneriler: {len(prom)}\n")
    if prom:
        for r in prom:
            L.append(f"- **{r[2]}** → {r[0]} / {r[5]} ({vlabel(r[3])})")
    else:
        L.append("_Bu çalıştırmada kanıtı doğrulanmış yeni öneri yok — diğerleri kanıt doğrulaması bekliyor._")
    L.append("\n## 4) Sonraki adım\nOnkolog ✅ önerileri onaylarsa → promote.py klinik dosyaları (TWO_TRACK_STRATEGY.html, _doz.md) günceller.\n")
    return "\n".join(L)

def main():
    con=db.connect()
    rid,n=engine.run_surveillance(con, note=os.environ.get("RUN_NOTE","zamanlanmış sürveyans"))
    rep=report(con, rid)
    os.makedirs("reports", exist_ok=True)
    open(f"reports/progress_run_{rid}.md","w").write(rep)
    # geriye dönük terfi olgu dosyasını yalnız terfi kaydı VARSA yenile (boş stub ile ezme)
    _c=con.cursor()
    _c.execute("SELECT COUNT(*) FROM promotion")
    if _c.fetchone()[0] > 0:
        open("reports/TERFI_OLGU_DOSYASI.md","w").write(promote.case_file(con))
    print(rep)
    print(f"\n[run.py] {n} öneri · rapor: reports/progress_run_{rid}.md · olgu: reports/TERFI_OLGU_DOSYASI.md")
    con.close()

if __name__=="__main__":
    main()
