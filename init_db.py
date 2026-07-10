"""init_db.py — şemayı kur + seed_data.json'u yükle. SQLite veya Postgres (DB_BACKEND).
Kullanım:  DB_BACKEND=sqlite DB_PATH=gbm_eda.db python init_db.py
           DB_BACKEND=postgres PGHOST=... PGUSER=... PGPASSWORD=... python init_db.py
"""
import json, db

TABLES=["vulnerability","mechanism_node","drug","drug_node","pharmacology","toxicity","combination","combination_member","evidence"]
# NOT: promotion/proposal/run_log seed'e dahil DEĞİL — terfi geçmişi sistem çalıştıkça birikir.

def main():
    con=db.connect(); cur=con.cursor()
    sql=open("schema.sql").read()
    # Postgres: AUTOINCREMENT/datetime('now') SQLite'a özgü — üretimde schema_pg.sql kullanın (README).
    if db.BACKEND=="sqlite":
        cur.executescript(sql)
    else:
        # Postgres yolu: schema_pg.sql (README'de üretilir) beklenir
        cur.execute(open("schema_pg.sql").read())
    seed=json.load(open("seed_data.json"))
    for t in TABLES:
        rows=seed[t]
        if not rows: continue
        cols=list(rows[0].keys())
        ph=db.ph(len(cols))
        for r in rows:
            cur.execute(f"INSERT INTO {t} ({','.join(cols)}) VALUES ({ph})", [r[c] for c in cols])
    con.commit()
    print("Yüklendi:", {t:len(seed[t]) for t in TABLES})
    con.close()

if __name__=="__main__":
    main()
