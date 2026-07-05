# Ana İlaç Listesi (drug_list) — Rekürren GBM Kombinasyon Sistemi

**Amaç:** Bu proje boyunca değerlendirilen TÜM etken maddeleri tek referansta toplamak.
Konu dağıldıkça buraya dönülür; yeni etken madde/ilaç değerlendirmeleri bu tabloya eklenir.

**Hastanın tümör zayıflıkları (V1–V8):**
V1_TERT (promoter C250T, truncal) · V2_TP53 (çok-varyant kayıp, truncal) ·
V3_PTEN_PI3K (R130* + chr10 kaybı) · V4_NFKB (NFKBIA del) · V5_MGMT (metillenmemiş) ·
V6_WNT_TCF7L2 (del, düşük öncelik/gap) · V7_METABOLIC · V8_IMMUNE (soğuk: TMB 4.7, MSS).

**Erişim kodları:** F=Türkiye repurpose · A=Türkiye onkoloji ilacı · O=yurtdışı onkoloji ·
T=deneme/trial-kapılı · X=çıkarıldı/deprioritize.

**Sütun okuma notları:**
- *Kanıt düzeyi:* ⭐=güçlü öne çıkan, ⛔=randomize negatif. "İnsan çalışması" > "vaka/retro" > preklinik.
- *KBB geçişi:* "ölçülmüş-iyi" = beyin konsantrasyonu deneysel ölçülmüş (hücre-içi yeterli düzey kanıtı);
  "CNS-aktif" = geçtiği biliniyor ama ölçülmemiş; "ölçülmüş-zayıf" = geçiş zayıf ölçülmüş.
- *Toksisite:* ⚠=kara kutu veya kritik; hastanın Lamide (lakozamid) kullanımı → QT-uzatanlarda EKG şartı.

---


### ⭐ Pano incelemesiyle öne çıkan YENİ/daha iyi adaylar

| İlaç | Zayıflık | Kanıt düzeyi | KBB geçişi | Toksisite (başlıca) | Erişim | Not |
|---|---|---|---|---|---|---|
| Marizomib | V4_NFKB | ⭐ İnsan çalışması GBM; beyin-ölçülmüş-iyi (pano skor 86.7) | ölçülmüş-iyi (beyne geçen proteazom inh.) | CNS etkileri (ataksi, halüsinasyon, yorgunluk), bulantı | O/T (yurtdışı onkoloji / deneme) | ⭐ V4 boşluğunu dolduran YENİ aday; beyne geçen ilk proteazom inhibitörlerinden |
| Bortezomib | V4_NFKB | İnsan vaka/retro GBM; beyin-ölçülmüş (pano 71.3) | ölçülmüş-iyi | Periferik nöropati (doz-kısıtlayıcı), trombositopeni, herpes reaktivasyonu | O (yurtdışı onkoloji — myelom onaylı) | Marizomib alternatifi; nöropati riski daha yüksek |
| Simvastatin | V7_METABOLIC | İnsan vaka/retro; beyin-ölçülmüş-iyi (pano 65.8) | ölçülmüş-iyi (lipofilik statin) | Miyopati/rabdomiyoliz (özellikle CYP3A4 etkileşimi), hepatotoksisite; kara kutu YOK (openFDA) | F (Türkiye repurpose) | ⭐ Atorvastatin YERİNE — beyin geçişi daha iyi; ⚠ itraconazol ile CYP3A4 çakışması |
| Dordaviprone (ONC201) | YENİ eksen (DRD2/ClpP) | ⭐ İnsan çalışması GBM; beyin-geçişli (pano EN YÜKSEK 94.0) | ölçülmüş-iyi | Genelde iyi tolere; minimal miyelosupresyon (avantaj), yorgunluk | O/T (yurtdışı; H3K27M'de onaylı yol) | ⭐ Sistemde YOKtu; H3K27M durumu netleştirilmeli — belirleyici |


### 🔬 Deneme-kapılı çekirdek (sintetik-letal + hedefli)

| İlaç | Zayıflık | Kanıt düzeyi | KBB geçişi | Toksisite (başlıca) | Erişim | Not |
|---|---|---|---|---|---|---|
| Paxalisib | V3_PTEN_PI3K | İnsan çalışması; beyin-ölçülmüş-iyi (pano 80.2) | ölçülmüş-iyi (beyin-penetran PI3K/mTOR) | Hiperglisemi (metforminle dengelenir), mukozit, döküntü | T (deneme — GBM AGILE NCT03970447) | V3 birincil seçim; doğrulandı |
| Adavosertib (WEE1i) | V2_TP53 | İnsan vaka/retro; beyin-ölçülmüş-iyi (pano 81.0) | ölçülmüş-iyi | Miyelosupresyon (doz-kısıtlayıcı, alkilleyici ile), bulantı | T (deneme — NCT05765812 Debio0123 benzeri) | Sintetik-letal çekirdek; p53-null hedefi; doğrulandı |
| Ceralasertib (ATRi) | V2_TP53 | İnsan vaka/retro; beyin-ölçülmüş-iyi (pano 75.2) | ölçülmüş-iyi | Miyelosupresyon, anemi | T (deneme) | WEE1 alternatifi/tamamlayıcısı |
| 6-thio-2-deoxyguanosine | V1_TERT | İnsan vaka/retro; beyin-ölçülmüş (pano 68.0) | ölçülmüş-iyi | Deneysel; sınırlı insan güvenlik verisi | T (deneysel) | V1 için nadir gerçekçi aday; ateganosine (71.0) benzer |


### 💊 Hızlı repurpose (Türkiye'de ulaşılabilir)

| İlaç | Zayıflık | Kanıt düzeyi | KBB geçişi | Toksisite (başlıca) | Erişim | Not |
|---|---|---|---|---|---|---|
| Metformin | V7_METABOLIC | İnsan çalışması; beyin-ölçülmüş-iyi (pano 82.4) | ölçülmüş-iyi (br:pl ~0.2-0.4) | ⚠ Laktik asidoz (kara kutu), GİS | F (Türkiye repurpose) | Doz-boşluk GENİŞ (~600-1000×) → sitotoksik değil, metabolik duyarlılaştırıcı/sinerjik |
| Hidroksiklorokin | V4,V7 (otofaji) | Faz1/2 GBM — 10.4161/auto.28984 | CNS-aktif (lizozomotropik birikim) | ⚠ İrreversibl retinopati, QT/kardiyomiyopati (Lamide ile EKG), SJS/TEN | F (Türkiye repurpose) | Doz-boşluk SINIRDA; klinik otofaji blokajı değişken |
| Valproik asit | V5_MGMT (HDAC) | HDAC inh.; radyoduyarlılaştırma | CNS-aktif (ölçülmemiş) | ⚠ Hepatotoksisite (kara kutu), pankreatit, hiperamonyemi | F (ama ÜÇÜNCÜ AEİ) | Hasta zaten 2 AEİ kullanıyor → geri planda; nörolog kararı |
| Celecoxib | V8,V4 (COX-2) | CUSP9v3 bileşeni — 10.3390/ph14121241 | ölçülmüş-iyi | ⚠ Kardiyovasküler+GİS (kara kutu) | F (Türkiye repurpose) | Doz-boşluk geniş (apoptoz için); COX-2 baskısı nM'de sağlanır |
| Mebendazol | V2-kısmi,V7 (tübülin) | ⭐ Faz1 GBM NCT01729260 (COMPLETED) | beyin-penetran (polimorf C; Bai 2015) | Karaciğer (yüksek doz), nadir nötropeni | F (Türkiye repurpose) | Doz-boşluk EN DAR; en gerçekçi doğrudan repurpose etki; emilim değişken |
| Atorvastatin | V7_METABOLIC | Repurpose statin — 10.1186/s13046-021-02041-2 | ⚠ ölçülmüş-ZAYIF (pano beklemede) | Miyopati/rabdomiyoliz, hepatotoksisite | F ama → SİMVASTATİNE çevir | Beyin geçişi zayıf; simvastatin tercih edilmeli |


### 🏥 Ulaşılabilir onkoloji ilaçları (backbone)

| İlaç | Zayıflık | Kanıt düzeyi | KBB geçişi | Toksisite (başlıca) | Erişim | Not |
|---|---|---|---|---|---|---|
| Bevacizumab (Altuzan) | V7,V8 | Faz3 recurrent GBM (PFS↑) — 10.1200/jco.2008.19.8721 | anti-anjiyogenik (damar hedefi) | Hipertansiyon, kanama, GİS perforasyon, yara iyileşmesi | A (hasta kullanıyor) | Zaten kullanımda; V7/V8 damar/mikroçevre düğümünü kapsıyor |
| Levetirasetam (Keppra) | — (antiepileptik) | Standart AEİ | CNS-aktif | Davranışsal/psikiyatrik, somnolans; PK-sessiz | A (hasta kullanıyor) | İlaç etkileşimi minimal; güvenli zemin |
| Lakozamid (Lamide) | — (antiepileptik) | Standart AEİ | CNS-aktif | ⚠ Kardiyak iletim/PR uzaması → QT-uzatanlarla EKG şartı | A (hasta kullanıyor) | HCQ/itraconazol eklenirse bazal+takip EKG |
| Temozolomid | V5_MGMT (alkilleyici) | Standart GBM | iyi | Miyelosupresyon, hepatotoksisite | A (Türkiye onkoloji) | MGMT-metillenmemiş → sınırlı fayda ama omurga ilaç |
| Lomustin | V5_MGMT (alkilleyici) | Rekürren standart — 10.1016/j.ctrv.2020.102029 | iyi (lipofilik nitrozüre) | ⚠ Gecikmeli/kümülatif miyelosupresyon (4-6 hafta, kara kutu) | A (Türkiye onkoloji) | Rekürren GBM omurga; her 6 haftada bir |
| Regorafenib | V7,V8 (multikinaz) | REGOMA lomustine üstün — 10.1016/s1470-2045(18)30675-2 | orta | ⚠ Hepatotoksisite (kara kutu), el-ayak sendromu, hipertansiyon | A (Türkiye onkoloji) | Bevacizumab ile HT çakışması; V7/V8 zaten kapsalı |
| Everolimus | V3_PTEN_PI3K | mTOR — 10.18632/oncotarget.7961 | ⚠ ölçülmüş-ZAYIF (pano beklemede) | Non-enfeksiyöz pnömoni, enfeksiyon, hiperglisemi | A/O (off-label) | Paxalisib yedeği ama beyin geçişi zayıf → paxalisib birincil |


### ⛔ Çıkarılan / deprioritize edilen

| İlaç | Zayıflık | Kanıt düzeyi | KBB geçişi | Toksisite (başlıca) | Erişim | Not |
|---|---|---|---|---|---|---|
| İtraconazol | V7,V8 | ReDO — 10.3332/ecancer.2015.521 | ⚠ ZAYIF (P-gp atar; pano beklemede) | ⚠ KKY (kara kutu), CYP3A4 (en ağır), QT (Lamide riski) | X (deprioritize) | Açtığı düğümler zaten kapsanıyor; en ağır etkileşim yükü → çıkarıldı |
| Disulfiram | V4 (proteazom-dolaylı) | ⛔ DIRECT randomize NEGATIF — 10.1001/jamanetworkopen.2023.4149 | ölçülmüş-zayıf | Grade≥3 AE %34 vs %11; nöropati | X (çıkarıldı) | ⛔ Randomize denemede sağkalım faydası YOK + fazla toksik → önerilmez |


---

## Nasıl kullanılır (ileriki değerlendirmeler için)

Yeni bir etken madde önerildiğinde, şu 7 sütunla bu tabloya bir satır ekleyin:
1. **Zayıflık:** V1–V8'den hangisini/hangilerini hedefliyor (yeni eksen ise belirt).
2. **Kanıt düzeyi:** insan çalışması / vaka / preklinik; varsa DOI veya NCT.
3. **KBB geçişi:** ölçülmüş-iyi / CNS-aktif / ölçülmüş-zayıf / bilinmeyen.
4. **Toksisite:** başlıca organ + kara kutu + mevcut ilaçlarla etkileşim.
5. **Erişim:** F/A/O/T/X.
6. **Doz-boşluk** (repurpose ilaçlar için): in-vitro etkili vs tümörde ulaşılabilir
   (bkz. `dose_estimates/` klasörü).
7. **Not:** düğüm örtüşmesi, redundans, önemli uyarı.

**İlgili dosyalar:** `PANO_INCELEME_kanit_ve_hucre_ici_duzey.md` (pano çapraz-analizi),
`dose_estimates/` (doz-boşluk hesapları), `TOXICITY_PROFILE.md` (detaylı toksisite),
`TWO_TRACK_STRATEGY.md` (K1–K4 kombinasyonları), `REDUNDANCY_ANALYSIS.md` (düğüm örtüşmesi).

*Kanıt düzeyleri ve KBB etiketleri literatür/pano derlemesidir; her satır kaynağından
doğrulanmalı, kararlar nöro-onkologla birlikte alınmalıdır.*
