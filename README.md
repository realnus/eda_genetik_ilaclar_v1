# EDA NGS İlaç Sürveyans Sistemi — Rekürren GBM (IDH-yabanıl, RTK1)

Bu proje **tek, sabit** bir genomik profil için çalışır (jenerik NGS motoru değil). Görevi: mevcut
**K2 / K3 / K5** kombinasyonları için, aynı tümör zayıflıklarını **daha iyi ve/veya daha az toksik**
vuran ilaç adaylarını sürekli aramak, ve **neden daha iyi** olduğunu gerekçeli bir ilerleme raporu
olarak sunmak. Klinik dosyalar (`TWO_TRACK_STRATEGY.html`, `_doz.md`) **otomatik ezilmez** —
öneriler onkolog onayına kadar bekler.

## Doğrulanmış davranış (bu ortamda test edildi)
Sistem, **eski durumdan** (K2/K3/K5'te Atorvastatin; V4 için yalnız HCQ'nun dolaylı etkisi)
başlatıldığında, bu projede daha önce **elle** bulunan iki iyileştirmeyi **kör noktadan yeniden
keşfetti**:
- **Simvastatin → Atorvastatin** (K2/K3/K5) — BBB (ölçülmüş-zayıf→ölçülmüş-iyi) + dose-gap + toksisite kazanımı, sıfır regresyon.
- **Marizomib**, V4 doğrudan proteazom düğümü için boşluk-doldurma — **yalnız K5'te** (doğru erişim sınıfı; K2/K3'e sızmadı).

Bu, "daha iyi kombinasyon bulan sistem" iddiasının bilinen-doğru-cevaplı testidir ve geçti.

## Mimari
| Katman | Otomatik | Not |
|---|---|---|
| Zayıflık → düğüm haritası | evet | `seed_data.json` (bu profile sabit) |
| İlaç → düğüm eşlemesi | evet | curated + ingest |
| Regresyonsuz "daha iyi mi?" testi | evet | `engine.better_than` — BBB/dose-gap/toksisite/QT eksenleri |
| Erişim-sınıfı kapısı | evet | K2/K3 = hızlı (F/A); K5 = deneme serbest (F/A/O/T) |
| **Kanıt doğrulama kapısı** | **hayır (zorunlu)** | `verify.py` — DOI/çalışma/yön; terfiden önce şart |
| Klinik dosya güncelleme | onay sonrası | `promote.py` (siz bağlarsınız) |

## Dosyalar
- `schema.sql` — 11 tablo (SQLite). Postgres için aşağıya bakın.
- `seed_data.json` — sabit profil + ilaç havuzu: curated altın çekirdek (21) + ChEMBL/literatür ile eklenen yeni adaylar (Ixazomib, Carfilzomib, WNT-974) = **24 ilaç**.
- `db.py` — SQLite↔Postgres tek bağlantı katmanı (kimlik bilgisi env'den).
- `init_db.py` — şema kur + seed yükle.
- `engine.py` — sürveyans motoru (TEST EDİLDİ).
- `run.py` — bir çalıştırma + ilerleme raporu (`reports/progress_run_<id>.md`).
- `verify.py` — kanıt doğrulama kapısı (iskelet — üretimde HTTP çağrılarını bağlayın).
- `gbm_eda.db` — örnek dolu SQLite (referans).

## Çalıştırma (SQLite — geliştirme)
```bash
export DB_BACKEND=sqlite DB_PATH=gbm_eda.db PYTHONPATH=.
python init_db.py       # şema + seed
python run.py           # sürveyans + rapor
```

## Postgres'e geçiş (üretim / sizin sunucunuz)
1. Kimlik bilgilerini **`.env`** dosyasına koyun (koda ASLA gömmeyin):
   ```
   DB_BACKEND=postgres
   PGHOST=46.196.36.10
   PGUSER=claude_science
   PGPASSWORD=***          # sohbette düz metin geçti — DEĞİŞTİRİN
   PGDATABASE=claude_science
   ```
2. `db.py` şemayı `eda_ngs_drug_research` altında otomatik oluşturur. Her yeni proje = ayrı şema.
3. `schema.sql` SQLite lehçesindedir (`AUTOINCREMENT`, `datetime('now')`). Postgres için
   `schema_pg.sql` üretin: `INTEGER PRIMARY KEY AUTOINCREMENT` → `SERIAL PRIMARY KEY`,
   `datetime('now')` → `now()`. (Küçük, mekanik dönüşüm; istenirse hazırlanır.)
4. `python init_db.py && python run.py` — aynı arayüz.

## Zamanlama (aylık — literatür günlük değişmez)
```cron
0 6 1 * *  cd /opt/eda_ngs && . .env && python run.py >> reports/cron.log 2>&1
```

## Kanıt doğrulama kapısını bağlama (ZORUNLU, üretimde)
`verify.py` içindeki `verify_doi` / `verify_trial` / `check_direction` fonksiyonlarını gerçek
API çağrılarıyla doldurun (OpenAlex `api_key` env'den; clinicaltrials.gov v2; openFDA). Kural:
**randomize-negatif** bir sonuç adayı düşürür; en az bir **doğrulanmış + destekleyici** kanıt
olmadan hiçbir öneri terfi edilmez. Doğrulama olmadan otomatik terfi = bu projenin düzelttiği
hataların ölçekte tekrarı.

## Terfi mekanizması + geriye dönük olgu dosyası (`promote.py`)
Bir öneri terfi edildiğinde `promotion` tablosuna **tam anlık-görüntü** yazılır: tekil toksisite,
kombine/DDI toksisite (kombinasyondaki organ kanalı örtüşmesi), KBB geçişi, kanıt düzeyi+DOI, ve
motorun eksen kazanımları. Böylece "sistem bu ilaca neden terfi etti?" sorusu **geriye dönük**
yanıtlanır.

- `promote.promote(con, proposal_id, promoted_by="system")` — kanıtı doğrulanmış öneriyi terfi eder.
- Onkolog farklı bir ilaç seçerse: `promote.promote(con, proposal_id, promoted_by="onkolog", override=True)`
  — kanıt kapısını onkolog kararıyla geçer, kayıt **'onkolog tercihi'** olarak işaretlenir.
- Doğrulanmamış aday `override=False` ile terfi edilemez (kapı çalışır).
- `promote.case_file(con, vuln_id=None)` — her zayıflık için **büyüyen terfi zincirini** markdown
  olarak üretir (`reports/TERFI_OLGU_DOSYASI.md`). Her satır: mevcut→aday, tekil+kombine tox, KBB, kanıt.

Bu, onkoloğa "en iyi liste" ile gitmenizi ve sistemin progressive ilerlemesini göstermenizi sağlar.

## Güvenlik
- Kimlik bilgileri yalnız `.env`'de; kaynak koda/artefakta yazılmaz.
- Postgres şifresi sohbette açık geçti — sunucuda **değiştirin**.
