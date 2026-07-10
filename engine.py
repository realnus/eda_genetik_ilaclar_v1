"""engine.py — sürveyans motoru: aday ilaçları mevcut K2/K3/K5'e karşı
'regresyonsuz daha iyi mi?' testinden geçirir, öneri üretir. TEST EDİLDİ (SQLite).

Kanıtlanan davranış: eski durumdan (Atorvastatin, V4=sadece dolaylı HCQ) başlatıldığında
motor bu projede elle bulunan iki iyileştirmeyi kör noktadan yeniden keşfetti:
  - Simvastatin > Atorvastatin (K2/K3/K5) — BBB + dose-gap + toksisite kazanımı
  - Marizomib V4 doğrudan proteazom düğümü gap-fill (yalnız K5, doğru erişim sınıfı)
"""
import json

EV_RANK  = {"randomize-pozitif":5,"faz1-2":4,"faz0":3,"preklinik":2,"derleme":1,"randomize-negatif":0,None:1}
BBB_RANK = {"olculmus-iyi":4,"CNS-aktif":3,"tahmini":2,"anti-anjiyogenik":3,"olculmus-zayif":1,"bilinmiyor":0}
# Her kombinasyonun erişim tavanı: K2/K3 hızlı (deneme yok), K5 deneme/yurtdışı serbest
COMBO_ACCESS = {"K2":set("FA"), "K3":set("FA"), "K5":set("FAOT")}

def _q(con, sql, args=()):
    cur=con.cursor(); cur.execute(sql.replace("?", "%s") if _is_pg(con) else sql, args); return cur

def _is_pg(con): return con.__class__.__module__.startswith("psycopg2")

def drug_axes(con, drug_id):
    ph=_q(con,"SELECT bbb_class,bbb_confidence,dose_gap_ratio FROM pharmacology WHERE drug_id=?",(drug_id,)).fetchone()
    tx=_q(con,"SELECT boxed,organ_load,qt_flag,cyp3a4_flag FROM toxicity WHERE drug_id=?",(drug_id,)).fetchone()
    organ=json.loads(tx[1]) if tx and tx[1] else {}
    return {"bbb_class":ph[0],"bbb_rank":BBB_RANK.get(ph[0],0),"bbb_conf":ph[1] or 0,
            "dose_gap":ph[2],"tox_load":sum(organ.values()),"boxed":tx[0],"qt":tx[2],"cyp3a4":tx[3]}

def better_than(con, cand_id, inc_id):
    """Regresyonsuz iyileştirme: en az bir eksende kazanım, HİÇBİR eksende kötüleşme yok."""
    a=drug_axes(con,cand_id); b=drug_axes(con,inc_id); gains=[]; regress=[]
    if a["bbb_rank"]>b["bbb_rank"] or (a["bbb_rank"]==b["bbb_rank"] and a["bbb_conf"]>b["bbb_conf"]+10):
        gains.append(f"BBB {b['bbb_class']}→{a['bbb_class']}")
    elif a["bbb_rank"]<b["bbb_rank"]: regress.append("BBB")
    if a["dose_gap"] and b["dose_gap"]:
        if a["dose_gap"]>b["dose_gap"]*1.5: gains.append(f"dose-gap {b['dose_gap']}→{a['dose_gap']}")
        elif a["dose_gap"]<b["dose_gap"]/1.5: regress.append("dose-gap")
    if a["tox_load"]<b["tox_load"]: gains.append(f"toksisite {b['tox_load']}→{a['tox_load']}")
    elif a["tox_load"]>b["tox_load"]: regress.append("toksisite")
    if a["qt"] and not b["qt"]: regress.append("QT-ekler")
    elif b["qt"] and not a["qt"]: gains.append("QT-yükü-kalkar")
    return (len(gains)>0 and len(regress)==0), gains, regress

def _nodes(con, did): return set(r[0] for r in _q(con,"SELECT node_id FROM drug_node WHERE drug_id=?",(did,)).fetchall())
def _members(con, cid): return [r[0] for r in _q(con,"SELECT drug_id FROM combination_member WHERE combo_id=?",(cid,)).fetchall()]
def _track(con, did): return _q(con,"SELECT access_track FROM drug WHERE drug_id=?",(did,)).fetchone()[0]
def _nodelabel(con,nid):
    r=_q(con,"SELECT vuln_id,node_name FROM mechanism_node WHERE node_id=?",(nid,)).fetchone(); return f"{r[0]}::{r[1]}"

def run_surveillance(con, note="", combos=("K2","K3","K5")):
    cur=con.cursor()
    n_cand=_q(con,"SELECT COUNT(*) FROM drug WHERE status IN('candidate','active')").fetchone()[0]
    _q(con,"INSERT INTO run_log(n_candidates,n_proposals,note) VALUES(?,?,?)",(n_cand,0,note))
    run_id=_q(con,"SELECT MAX(run_id) FROM run_log").fetchone()[0]
    pool=[r[0] for r in _q(con,"SELECT drug_id FROM drug WHERE status='candidate'").fetchall()]
    proposals=[]
    for cid in combos:
        allowed=COMBO_ACCESS.get(cid,set("FAOT")); members=_members(con,cid); mset=set(members)
        for cand in pool:
            if cand in mset: continue
            ct=_track(con,cand)
            if ct and ct not in allowed: continue          # ERİŞİM KAPISI
            cnodes=_nodes(con,cand)
            for inc in members:                             # İKAME (aynı erişim sınıfı)
                if _track(con,inc)!=ct: continue
                shared=_nodes(con,inc)&cnodes
                if not shared: continue
                ok,gains,reg=better_than(con,cand,inc)
                if ok: proposals.append((run_id,cid,list(shared)[0],inc,cand,json.dumps(gains,ensure_ascii=False),"substitution"))
            for nid in cnodes:                              # BOŞLUK-DOLDURMA
                dn=_q(con,"SELECT directness FROM drug_node WHERE drug_id=? AND node_id=?",(cand,nid)).fetchone()
                if not dn or dn[0]!="direct": continue
                covered=_q(con,"""SELECT COUNT(*) FROM drug_node dn JOIN combination_member cm ON cm.drug_id=dn.drug_id
                    WHERE cm.combo_id=? AND dn.node_id=? AND dn.directness='direct'""",(cid,nid)).fetchone()[0]
                if covered==0:
                    ax=drug_axes(con,cand)
                    if ax["tox_load"]<=2 and not ax["qt"]:
                        proposals.append((run_id,cid,nid,None,cand,
                            json.dumps([f"{_nodelabel(con,nid)} düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite"],ensure_ascii=False),"gap-fill"))
    seen=set(); final=[]
    for p in proposals:
        k=(p[1],p[3],p[4],p[6])
        if k in seen: continue
        seen.add(k); final.append(p)
    for p in final:
        _q(con,"""INSERT INTO proposal(run_id,combo_id,node_id,incumbent_drug_id,candidate_drug_id,axis_gains,rationale)
                  VALUES(?,?,?,?,?,?,?)""",p)
    _q(con,"UPDATE run_log SET n_proposals=? WHERE run_id=?",(len(final),run_id))
    con.commit()
    return run_id, len(final)
