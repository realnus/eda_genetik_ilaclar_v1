"""promote.py — TERFİ MEKANİZMASI + geriye dönük olgu dosyası.

Bir öneriyi (proposal) terfi ettirir:
  1. Kanıt kapısını uygular (verify.evidence_status → promotable olmalı; onkolog override edebilir).
  2. Tekil toksisite + kombine/DDI toksisite + KBB + kanıt gerekçelerini TAM anlık-görüntü olarak
     promotion tablosuna yazar (geriye dönük 'neden bu ilaç?' sorusu buradan yanıtlanır).
  3. combination_member'ı günceller (ikame → değiştir, gap-fill → ekle).
  4. proposal.status='promoted'.

Onkolog farklı bir ilaç önerirse: promote(proposal_id=None, manual=dict(...)) ile elle terfi kaydı
açılır; sistem 'onkolog tercihi' olarak işaretler ve olgu dosyasına dahil eder.
"""
import os, json

def _q(cur,s,a=()): 
    cur.execute(s.replace("?","%s") if os.environ.get("DB_BACKEND")=="postgres" else s, a); return cur

def _single_tox(con, name):
    cur=con.cursor()
    _q(cur,"""SELECT t.boxed,t.organ_load,t.qt_flag FROM toxicity t JOIN drug d ON d.drug_id=t.drug_id
              WHERE d.name=?""",(name,))
    r=cur.fetchone()
    if not r: return "veri yok"
    organ=json.loads(r[1]) if r[1] else {}
    parts=[f"organ yükü toplam {sum(organ.values())} ({', '.join(f'{k}:{v}' for k,v in organ.items())})"]
    if r[0]: parts.append("kutu-içi uyarı VAR")
    if r[2]: parts.append("QT uzatır (Lamide ile EKG)")
    return "; ".join(parts)

def _combined_tox(con, combo_id, name):
    """Adayı kombinasyona kattığımızda örtüşen organ kanalları (DDI proxy)."""
    cur=con.cursor()
    _q(cur,"SELECT organ_load FROM toxicity t JOIN drug d ON d.drug_id=t.drug_id WHERE d.name=?",(name,))
    r=cur.fetchone(); cand=json.loads(r[0]) if r and r[0] else {}
    _q(cur,"""SELECT t.organ_load FROM combination_member cm JOIN toxicity t ON t.drug_id=cm.drug_id
              WHERE cm.combo_id=?""",(combo_id,))
    combo={}
    for (ol,) in cur.fetchall():
        for k,v in (json.loads(ol) if ol else {}).items(): combo[k]=combo.get(k,0)+v
    overlaps={k:(cand[k],combo.get(k,0)) for k in cand if combo.get(k,0)>0}
    if not overlaps: return "kombinasyonla örtüşen organ kanalı yok (temiz katkı)"
    return "örtüşme: "+"; ".join(f"{k} (aday+{v[0]}, mevcut {v[1]})" for k,v in overlaps.items())

def _bbb(con, name):
    cur=con.cursor()
    _q(cur,"SELECT bbb_class,bbb_confidence,dose_gap_ratio FROM pharmacology p JOIN drug d ON d.drug_id=p.drug_id WHERE d.name=?",(name,))
    r=cur.fetchone()
    if not r: return "veri yok"
    s=f"KBB: {r[0]} (güven {r[1]})"
    if r[2] is not None: s+=f"; dose-gap {r[2]}"
    return s

def _evidence(con, name):
    cur=con.cursor()
    _q(cur,"""SELECT e.doi,e.title,e.year,e.evidence_level,e.direction,e.verified
              FROM evidence e JOIN drug d ON d.drug_id=e.drug_id WHERE d.name=?""",(name,))
    rows=cur.fetchall()
    if not rows: return "kayıtlı kanıt yok"
    best=rows[0]
    tag="✅doğrulandı" if best[5]==1 else "⚠doğrulanmadı"
    return f"{best[3]} · yön={best[4]} · {tag} · {best[2]} · DOI:{best[0]}"

def promote(con, proposal_id, promoted_by="system", override=False):
    import verify
    cur=con.cursor()
    _q(cur,"""SELECT p.combo_id,p.node_id,di.name,dc.name,dc.drug_id,p.axis_gains,p.rationale,mn.vuln_id,mn.node_name
              FROM proposal p LEFT JOIN drug di ON di.drug_id=p.incumbent_drug_id
              JOIN drug dc ON dc.drug_id=p.candidate_drug_id
              LEFT JOIN mechanism_node mn ON mn.node_id=p.node_id WHERE p.proposal_id=?""",(proposal_id,))
    p=cur.fetchone()
    if not p: return {"ok":False,"err":"öneri bulunamadı"}
    combo_id,node_id,inc,cand,cand_id,gains,rationale,vuln_id,node_name=p
    st=verify.evidence_status(con,cand_id)
    if not st["promotable"] and not override:
        return {"ok":False,"err":f"kanıt kapısı: {st['label']} — terfi engellendi (override=True ile onkolog geçebilir)","status":st}
    # snapshot reasons
    rec=(proposal_id,vuln_id,combo_id,f"{vuln_id}::{node_name}",inc,cand,
         _single_tox(con,cand),_combined_tox(con,combo_id,cand),_bbb(con,cand),_evidence(con,cand),
         gains,promoted_by)
    _q(cur,"""INSERT INTO promotion(proposal_id,vuln_id,combo_id,node_label,incumbent_name,candidate_name,
              reason_single_tox,reason_combined_tox,reason_bbb,reason_evidence,axis_gains,promoted_by)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",rec)
    # apply to combination
    if rationale=="substitution" and inc:
        _q(cur,"DELETE FROM combination_member WHERE combo_id=? AND drug_id=(SELECT drug_id FROM drug WHERE name=?)",(combo_id,inc))
    _q(cur,"INSERT OR IGNORE INTO combination_member VALUES(?,?,?)",(combo_id,cand_id,"added"))
    _q(cur,"UPDATE proposal SET status='promoted' WHERE proposal_id=?",(proposal_id,))
    con.commit()
    return {"ok":True,"promoted":cand,"combo":combo_id,"vuln":vuln_id,"by":promoted_by}

def case_file(con, vuln_id=None):
    """Geriye dönük OLGU DOSYASI: her zayıflık için büyüyen terfi zinciri.
    vuln_id=None → tüm zayıflıklar. Döner: markdown."""
    cur=con.cursor()
    where = "WHERE vuln_id=?" if vuln_id else ""
    args = (vuln_id,) if vuln_id else ()
    _q(cur,f"""SELECT vuln_id,combo_id,node_label,incumbent_name,candidate_name,
               reason_single_tox,reason_combined_tox,reason_bbb,reason_evidence,promoted_by,promoted_at
               FROM promotion {where} ORDER BY vuln_id,promoted_at""",args)
    rows=cur.fetchall()
    from collections import defaultdict
    by_v=defaultdict(list)
    for r in rows: by_v[r[0]].append(r)
    L=["# Terfi Olgu Dosyası — zayıflık bazlı ilerleme\n",
       "Her satır bir terfi kararıdır: sistemin (veya onkoloğun) hangi adayı, hangi mevcut ilacın yerine, "
       "hangi tekil/kombine toksisite ve KBB/kanıt gerekçesiyle seçtiğini gösterir.\n"]
    for v in sorted(by_v):
        L.append(f"\n## {v} — {len(by_v[v])} terfi\n")
        for i,r in enumerate(by_v[v],1):
            inc = r[3] or "(boşluk-doldurma, mevcut yok)"
            L.append(f"### {i}. {inc} → **{r[4]}**  · {r[1]} · {r[10]} · _{r[9]}_")
            L.append(f"- **Düğüm:** {r[2]}")
            L.append(f"- **Tekil toksisite:** {r[5]}")
            L.append(f"- **Kombine/DDI toksisite:** {r[6]}")
            L.append(f"- **KBB:** {r[7]}")
            L.append(f"- **Kanıt:** {r[8]}\n")
    if not rows: L.append("\n_Henüz terfi kaydı yok._")
    return "\n".join(L)
