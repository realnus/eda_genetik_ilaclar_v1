"""db.py — bağlantı katmanı. SQLite (geliştirme) ↔ Postgres (üretim) tek arayüz.
Kimlik bilgileri ORTAM DEĞİŞKENLERİNDEN okunur — asla koda gömülmez.
Postgres için:  DB_BACKEND=postgres  PGHOST=... PGUSER=... PGPASSWORD=... PGDATABASE=claude_science
                (şema: eda_ngs_drug_research)
SQLite için:    DB_BACKEND=sqlite (varsayılan)  DB_PATH=gbm_eda.db
"""
import os

BACKEND = os.environ.get("DB_BACKEND", "sqlite")
SCHEMA = "eda_ngs_drug_research"

def connect():
    if BACKEND == "postgres":
        import psycopg2
        conn = psycopg2.connect(
            host=os.environ["PGHOST"], user=os.environ["PGUSER"],
            password=os.environ["PGPASSWORD"],
            dbname=os.environ.get("PGDATABASE", "claude_science"),
            port=int(os.environ.get("PGPORT", "5432")),
        )
        with conn.cursor() as c:
            c.execute(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA};")
            c.execute(f"SET search_path TO {SCHEMA};")
        conn.commit()
        return conn
    else:
        import sqlite3
        conn = sqlite3.connect(os.environ.get("DB_PATH", "gbm_eda.db"))
        conn.execute("PRAGMA foreign_keys=ON;")
        return conn

def ph(n):
    """Placeholder stili: SQLite '?' , Postgres '%s'."""
    return ", ".join(["%s" if BACKEND == "postgres" else "?"] * n)
