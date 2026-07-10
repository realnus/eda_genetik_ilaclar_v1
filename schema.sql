-- eda_ngs_drug_research — recurrent GBM (IDH-wt, RTK1) sürveyans veritabanı
-- SQLite (geliştirme/test) — Postgres'e taşınabilir standart SQL.
-- Postgres'te: CREATE SCHEMA eda_ngs_drug_research; SET search_path TO eda_ngs_drug_research;

-- 1) Sabit hasta profili ve zayıflıklar (bu proje TEK profil için)
CREATE TABLE IF NOT EXISTS vulnerability (
    vuln_id      TEXT PRIMARY KEY,          -- V1_TERT ...
    label        TEXT NOT NULL,
    driver       TEXT,                      -- genomik değişiklik
    clonality    TEXT,
    priority     INTEGER DEFAULT 3,         -- 1=en yüksek (truncal/açık), 3=düşük
    is_gap       INTEGER DEFAULT 0          -- 1 = güçlü beyin-geçen ilaç yok
);

-- 2) Bir zayıflığın mekanizma düğümleri (redundans mantığı buradan)
CREATE TABLE IF NOT EXISTS mechanism_node (
    node_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    vuln_id      TEXT NOT NULL REFERENCES vulnerability(vuln_id),
    node_name    TEXT NOT NULL,             -- 'mevalonat/kolesterol'
    UNIQUE(vuln_id, node_name)
);

-- 3) Aday ilaç havuzu (curated altın çekirdek + ingest edilen adaylar)
CREATE TABLE IF NOT EXISTS drug (
    drug_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    name           TEXT NOT NULL UNIQUE,
    chembl_id      TEXT,
    source         TEXT,                    -- 'curated' | 'chembl' | 'literature'
    access_track   TEXT,                    -- F/A/O/T/X
    status         TEXT DEFAULT 'candidate',-- candidate|active|removed
    removed_reason TEXT,                     -- YALNIZ status='removed' için
    monitor_note   TEXT,                     -- izlemedeki (candidate) ilaç için tarama/karar notu
    added_at       TEXT DEFAULT (datetime('now'))
);

-- 4) İlaç -> mekanizma düğümü eşlemesi (bir ilaç birkaç düğüm vurabilir)
CREATE TABLE IF NOT EXISTS drug_node (
    drug_id   INTEGER NOT NULL REFERENCES drug(drug_id),
    node_id   INTEGER NOT NULL REFERENCES mechanism_node(node_id),
    directness TEXT DEFAULT 'direct',       -- direct | indirect
    PRIMARY KEY (drug_id, node_id)
);

-- 5) BBB geçişi + hücre-içi yeterlilik (dose-gap)
CREATE TABLE IF NOT EXISTS pharmacology (
    drug_id        INTEGER PRIMARY KEY REFERENCES drug(drug_id),
    bbb_class      TEXT,                    -- 'olculmus-iyi'|'CNS-aktif'|'tahmini'|'olculmus-zayif'|'bilinmiyor'
    bbb_confidence INTEGER,                 -- 0-100 (ölçülmüş=yüksek)
    dose_gap_ratio REAL,                    -- tümör-ulaşılabilir / in-vitro etkili (>=0.3 iyi)
    dose_gap_note  TEXT
);

-- 6) Kanıt kayıtları — DOI + DOĞRULAMA DURUMU (kapı burada)
CREATE TABLE IF NOT EXISTS evidence (
    evidence_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    drug_id       INTEGER NOT NULL REFERENCES drug(drug_id),
    doi           TEXT,
    title         TEXT,
    year          INTEGER,
    evidence_level TEXT,                    -- 'randomize-negatif'|'randomize-pozitif'|'faz1-2'|'preklinik'|'derleme'
    direction     TEXT,                     -- 'supports'|'does_not_support'|'mixed'
    verified      INTEGER DEFAULT 0,        -- 1 = OpenAlex/CT/FDA ile doğrulandı
    verify_source TEXT,                     -- 'openalex'|'clinicaltrials'|'openfda'
    note          TEXT
);

-- 7) Toksisite eksenleri (organ kanalı yükü) + AEİ/DDI bayrakları
CREATE TABLE IF NOT EXISTS toxicity (
    drug_id      INTEGER PRIMARY KEY REFERENCES drug(drug_id),
    boxed        INTEGER DEFAULT 0,
    organ_load   TEXT,                      -- JSON: {"karaciger":2,"kemik_iligi":1,...}
    qt_flag      INTEGER DEFAULT 0,         -- 1 = QT uzatır (Lamide ile EKG)
    cyp3a4_flag  INTEGER DEFAULT 0,
    ddi_note     TEXT
);

-- 8) Mevcut kombinasyonlar (K2/K3/K5) ve üyeleri — sürveyansın hedefi
CREATE TABLE IF NOT EXISTS combination (
    combo_id   TEXT PRIMARY KEY,            -- 'K3','K5'
    label      TEXT,
    coverage   INTEGER,                     -- kaç zayıflık
    tox_score  INTEGER
);
CREATE TABLE IF NOT EXISTS combination_member (
    combo_id  TEXT NOT NULL REFERENCES combination(combo_id),
    drug_id   INTEGER NOT NULL REFERENCES drug(drug_id),
    role      TEXT,                         -- 'current'|'added'
    PRIMARY KEY (combo_id, drug_id)
);

-- 9) Sürveyans çalıştırma günlüğü + öneriler (öneri->onay->terfi kapısı)
CREATE TABLE IF NOT EXISTS run_log (
    run_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    run_at      TEXT DEFAULT (datetime('now')),
    n_candidates INTEGER,
    n_proposals INTEGER,
    note        TEXT
);
CREATE TABLE IF NOT EXISTS proposal (
    proposal_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id       INTEGER REFERENCES run_log(run_id),
    combo_id     TEXT REFERENCES combination(combo_id),
    node_id      INTEGER REFERENCES mechanism_node(node_id),
    incumbent_drug_id  INTEGER REFERENCES drug(drug_id),  -- mevcut ilaç
    candidate_drug_id  INTEGER REFERENCES drug(drug_id),  -- önerilen daha-iyi
    axis_gains   TEXT,                      -- JSON: hangi eksende iyileşme
    rationale    TEXT,
    status       TEXT DEFAULT 'proposed',   -- proposed|approved|rejected|promoted
    created_at   TEXT DEFAULT (datetime('now'))
);


-- 10) TERFİ KAYITLARI — geriye dönük denetim izi (her terfi tam anlık-görüntü)
CREATE TABLE IF NOT EXISTS promotion (
    promotion_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    proposal_id    INTEGER REFERENCES proposal(proposal_id),
    vuln_id        TEXT REFERENCES vulnerability(vuln_id),
    combo_id       TEXT REFERENCES combination(combo_id),
    node_label     TEXT,
    incumbent_name TEXT,               -- terfi anındaki mevcut ilaç (varsa)
    candidate_name TEXT NOT NULL,      -- terfi edilen aday
    reason_single_tox TEXT,            -- tekil toksisite gerekçesi
    reason_combined_tox TEXT,          -- kombine/DDI toksisite gerekçesi
    reason_bbb     TEXT,               -- KBB geçişi gerekçesi
    reason_evidence TEXT,              -- kanıt düzeyi + DOI
    axis_gains     TEXT,               -- JSON: motor eksen kazanımları
    promoted_by    TEXT DEFAULT 'system',  -- 'system' | 'onkolog'
    promoted_at    TEXT DEFAULT (datetime('now'))
);
