# Kombinasyon Tedavisi Araştırma Dosyası — Nüks Glioblastom (IDH-vahşi tip, RTK1)

**Amaç.** Bu tümörün spesifik moleküler zayıflıklarından kan-beyin bariyeri (BBB)'ni geçebilen ilaç kombinasyonlarına — hem onkoloji ajanlarını hem de yeniden kullanılabilir, eczaneden erişilebilir ilaçları kapsayan — kanıta dayalı, yapılandırılmış bir harita; birden fazla hayatta-kalma yolağına *aynı anda* saldırmak üzere tasarlanmıştır. Yeni kanıtlar ortaya çıktıkça yeniden çalıştırılıp güncellenebilecek şekilde oluşturulmuştur.

---

## 1. Tümörün zayıflık parmak izi

Doğrudan 2026-05-21 tarihli genomik profilleme özetinden türetilmiştir. Her biri bir terapinin çekebileceği bir kaldıraçtır.

| # | Değişiklik (raporunuzdan) | Klonalite | Ne yapar | Hedeflenebilir düğüm |
|---|------------------------------|-----------|--------------|----------------|
| V1 | **TERT** promoter C250T | Truncal sürücü (VAF %23) | Telomerazı yeniden aktive eder → ölümsüzlük | Telomer replikasyon stresi (ATR), telomeraz substratı |
| V2 | **TP53** kaybı — splice + Y163N + G245S + P152L | Truncal / eş-klonal (~%24–25) | G1/S kontrol noktası devre dışı → tümör hayatta kalmak için **G2/M kontrol noktasına** yaslanır | **WEE1, CHK1, ATR, PLK1** |
| V3 | **PTEN** R130\* + **kromozom 10 kaybı** | Geniş kromozom 10 kaybı üzerinde subklonal PTEN | **PI3K/AKT/mTOR**'u serbest bırakır | Beyne nüfuz edebilen PI3K/mTOR, AMPK |
| V4 | **NFKBIA** delesyonu (14q13.2) | Fokal delesyon | IκB-α kaybı → sürekli **NF-κB** hayatta-kalma sinyali | NF-κB, proteazom ekseni, kök hücre benzeri özellik (stemness) |
| V5 | **MGMT** promoter **metillenmemiş** | Biyobelirteç | Aktif MGMT alkilasyonu onarır → **temozolomide direnci** | MGMT'den bağımsız yollar; duyarlılaştırıcılar |
| V6 | **TCF7L2** delesyonu (10q25) | Fokal delesyon | Wnt/β-catenin bozulması (bağlama-bağımlı) | Wnt/GSK3 (keşifsel, düşük öncelik) |
| V7 | GBM **metabolik** fenotip | Soy düzeyinde | Warburg glikolizi, mevalonat/kolesterol bağımlılığı, otofaji ile hayatta kalma | OXPHOS, HMG-CoA, otofaji/lizozom |
| V8 | **İmmünolojik olarak soğuk** (TMB 4.7, MSS, HRD−, PD-L1 0) | Biyobelirteç | Düşük neoantijen yükü → tek ajanlı checkpoint blokajı olası değil | Mikroçevre / miyeloid modülasyon |

**Canlı kanıt teyidi (bu oturumda sorgulandı).** Open Targets Platform'da, tümörde değişikliğe uğramış genler glioblastomla ilişkili en üst sıradaki hedefler arasında yer almaktadır: **TP53 (skor 0.72), PTEN (0.64), TERT (0.54)** — yani bu profilin taşıdığı sürücüler, alanın hastalıkla en çok ilişkilendirdiği genlerdir. CIViC'te, **TERT** promoter mutasyonu glioblastomda *kötü-prognoz* kanıtı taşımaktadır (5 kayıttan 4'ü, yön SUPPORTS; 3'ü Seviye B, 1'i Seviye D), ve **TP53** *temozolomide-direnci* kanıtı taşımaktadır — TMZ'nin tek başına burada zayıf bir kaldıraç olduğunu bağımsız olarak güçlendirmektedir (MGMT-metillenmemiş durumu ile tutarlı). Not: **PTEN** için, tek prognostik CIViC kaydı (EID343) yön olarak *DOES_NOT_SUPPORT*'tur — yani PTEN mutasyonunun GBM'de prognostik **olmadığı** bildirilmektedir; PTEN'in buradaki terapötik önemi bir prognostik düğüm olarak değil, **prediktif** bir düğüm (PI3K/mTOR yolak aktivasyonu) olarak gelmektedir.

---

## 2. Tasarım mantığı — "sürücüleri kapsa, kaçışları engelle"

Hedefinizle (tüm zayıflıklara *aynı anda* saldırmak) örtüşen nüks-GBM literatürü katmanlı bir tasarımda birleşmektedir. Bu dosya bu tasarımı takip eder:

1. **Önce truncal sürücüler.** TERT (V1) ve TP53 kaybı (V2) truncal'dır — esasen her tümör hücresinde mevcuttur. Bunları göz ardı eden bir rejim tümörün yalnızca bir kısmını tedavi eder.
2. **p53-null sentetik-öldürücü fırsatı (V2) en güçlü hedeflenmiş fırsattır.** G1/S kontrol noktası devre dışı kaldığında, hücreler DNA hasarından kurtulmak için **G2/M kontrol noktasına** (WEE1/ATR/CHK1) bağımlı hale gelir. Bu kontrol noktasını kaldırmak *ile aynı zamanda* bir DNA-hasar kaynağı (radyasyon veya alkilleyici ajan) uygulamak hücreleri ölümcül mitotik felakete iter. Bu gerçek, gen-eşleşmeli bir zayıflıktır — genel bir sitotoksik değildir.
3. **Büyüme ve hayatta-kalma pompalarını kapat (V3, V4).** PI3K/mTOR ve NF-κB aktive olmuş iki hayatta-kalma eksenidir; beyne nüfuz edebilen inhibitörler + yeniden kullanılabilen baskılayıcılar her ikisine de vurur.
4. **Metabolik/otofaji kaçış yollarını aç bırakma (V7).** Hedeflenmiş stres altındaki tümörler otofaji ve metabolik esneklik yoluyla hayatta kalır — yeniden kullanım katmanı (metformin, statin, klorokin, disülfiram) bu kapıları kapatır.
5. **İmmünoterapiye aşırı yatırım yapma (V8).** Soğuk profil, tek-ajan checkpoint inhibitörlerinden az bir yarar öngörür; mikroçevre modülatörleri (örn. celecoxib) yardımcı ajanlardır, ana kaldıraç değil.

---

## 3. Aday ilaç kütüphanesi (zayıflıklara + BBB'ye eşlenmiş)

Kapsam matrisi figürüne bakınız. **R** katmanı = yeniden kullanılabilir/eczaneden erişilebilir;
**O** katmanı = onkoloji/hedefe yönelik (deneysel çalışma veya onkolog gözetiminde etiket-dışı).

### Yeniden kullanılabilir, BBB'yi geçebilen (R katmanı)
- **Metformin** — AMPK aktivasyonu → mTOR baskılanması; kompleks-I inhibisyonu OXPHOS'u düşürür. *V3, V7'yi hedefler.* BBB: orta.
- **Disülfiram + bakır** — Cu-DDC, NPL4/p97'yi agrege eder → proteotoksik stres; NF-κB & ALDH (kök hücre benzeri özellik) inhibisyonu. *V4, V7'yi hedefler.* BBB: iyi. (DIRECT çalışması NCT02678975; CUSP9 NCT02770378.)
- **Klorokin / Hidroksiklorokin** — otofaji/lizozom blokajı, tedavi stresi altında önemli bir hayatta-kalma mekanizmasını ortadan kaldırır. *V4, V7'yi hedefler.* BBB: iyi. (Randomize adjuvan çalışma NCT00224978.)
- **Atorvastatin** (lipofilik statin) — mevalonat blokajı → prenilasyonu & kolesterol tedarikini bozar. *V7'yi hedefler.* BBB: orta.
- **Celecoxib** — COX-2/PGE2 baskılanması → mikroçevre. *V8, V4'ü hedefler.* CUSP9'un bileşeni. BBB: orta.
- **Mebendazol** — mikrotübül destabilizasyonu; GBM preklinik + Johns Hopkins çalışmaları. *V2, V7'yi hedefler.* BBB: değişken.
- **Valproik asit** — HDAC inhibisyonu; olası radyoduyarlılaştırma (kanıt karışık). *V2, V5'i hedefler.* BBB: iyi.

### Onkoloji / hedefe yönelik (O katmanı)
- **Paxalisib (GDC-0084)** — BBB'yi geçmek üzere tasarlanmış çift PI3K/mTOR inhibitörü; PTEN-kaybı gerekçesi. *V3'ü hedefler.* (GBM AGILE NCT03970447; paxalisib+metformin+keto NCT05183204.)
- **Adavosertib (AZD1775, WEE1 inhibitörü)** — p53-null hücrelerde G2/M tutukluğunu ortadan kaldırır → mitotik felaket. *V2'yi hedefler.* (GBM Faz 0 NCT02207010; +RT/TMZ NCT01849146.)
- **ATR inhibitörü (ceralasertib / berzosertib)** — p53 kaybı + telomer stresinden kaynaklanan replikasyon stresini kullanır. *V2, V1'i hedefler.*
- **6-thio-2'-deoxyguanosine** — telomeraz substratı → TERT+ hücrelerde seçici olarak telomer disfonksiyonu; preklinik CNS aktivitesi. *V1'i hedefler.* (Deneysel, eczaneden erişilebilir değil.)
- **Temozolomide (bağlam)** — standart alkilleyici, ancak MGMT-metillenmemiş = azalmış yarar → tek başına kaldıraç olarak değil, *duyarlılaştırılmış/kombinasyon* DNA-hasar kaynağı olarak kullanın. *V5 için bağlam.*

---

## 4. Aday kombinasyon rejimleri

Erişim spektrumunu kapsayan üç rejim. En düşükten en yüksek erişim engeline doğru sıralanmıştır.

### Rejim A — Yeniden kullanım omurgası (tümü eczaneden erişilebilir)
**Metformin + Disülfiram/Cu + Klorokin + Atorvastatin + Celecoxib.**
V3, V4, V7, V8'i kapsar. Yalnızca jenerik oral, BBB'yi geçebilen ilaçlar kullanarak geniş yolak baskılaması. **Emsal:** **CUSP9\*** protokolü (NCT02770378), 9 ilaçlık bir yeniden kullanım kokteyli + metronomik TMZ'nin nüks GBM'de *uygulanabilir ve tolere edilebilir* olduğunu göstermiştir.
**Boşluk:** p53-null G2/M bağımlılığına (V2) veya telomer eksenine (V1) doğrudan vurmaz; sitostatiğe yaslanır.

> **⚠ Disülfiram üzerine kanıt-düzeyi güncellemesi (bu iterasyonda eklendi).** **DIRECT randomize çalışması**
> (NCT02678975; JAMA Netw Open 2023, n=88 nüks GBM), disülfiram + bakırın alkilleyici
> kemoterapiye eklenmesinin 6-aylık sağkalımı alkilleyici kemoterapiye kıyasla **anlamlı
> derecede iyileştirmediğini** ve anlamlı derecede daha fazla toksisiteye neden olduğunu
> bulmuştur (grade ≥3 advers olaylar %34 vs %11; ciddi advers olaylar %41 vs %16). Yazarlar
> nüks GBM için **önerilmemesi gerektiği** sonucuna varmıştır. Bu, tüm kütüphanedeki en yüksek
> kanıt düzeyi olup *negatiftir* — disülfiram bir omurga çapası olarak **önceliğinin
> düşürülmesi** gerekir. Bu, çoklu-hedef *kavramını* geçersiz kılmaz, ancak spesifik
> disülfiram+Cu kolu sonuç vermemiştir, dolayısıyla bir yeniden kullanım omurgası buna
> yaslanmamalıdır. Değiştirilmesi veya çıkarılması düşünülmeli ve toksisite sinyali göz
> önünde bulundurularak onkologla görüşülmelidir.

### Rejim B — Hedeflenmiş sentetik-öldürücü çekirdek (onkoloji/deneysel erişim gerektirir)
**Paxalisib + (Adavosertib *veya* ATR inhibitörü) + bir DNA-hasar kaynağı (RT veya alkilleyici ajan).**
V2, V3, V1'i kapsar. Bu, stratejinin gen-eşleşmeli kalbidir: p53-null bir tümörde beyne
nüfuz edebilen PI3K/mTOR blokajı + G2/M-kontrol noktası ortadan kaldırılması. **Emsal:**
paxalisib GBM AGILE (NCT03970447); adavosertib GBM Faz 0/1 (NCT02207010, NCT01849146).
**Boşluk:** erişimi sınırlı; örtüşen miyelosüpresyon dikkatli dozlama/sıralama gerektirir.

### Rejim C — Entegre (omurga + bir hedeflenmiş çapa) — *en gerçekçi*
**Paxalisib + Metformin + ketojenik metabolik baskı + Disülfiram/Cu + Klorokin.**
V2 (metabolik/replikasyon stresi yoluyla kısmi), V3, V4, V7'yi kapsar. **Emsal:** gerçek
bir çalışma **paxalisib + ketojenik diyet + metformin**'i GBM'de test etmiştir (NCT05183204) —
bu tam kombinasyonun doğrudan gerçek-dünya analoğu. **Durum uyarısı: NCT05183204,
ClinicalTrials.gov'da SUSPENDED (askıya alınmış) olarak listelenmektedir** (neden burada
teyit edilmemiştir — güvenmeden önce doğrulayın; askıya alma finansman, kayıt veya
güvenlik/idari nedenleri yansıtıyor olabilir). Bu, kombinasyonun tasarlandığını ve
başlatıldığını gösterir, olumlu sonuçlarla tamamlandığını değil. Bu, tartışılmaya değer
makul bir uygulanabilir başlangıç noktasıdır — jenerik metabolik/hayatta-kalma-baskılama
omurgasının üzerine katmanlanmış erişilebilir bir hedeflenmiş çapa (paxalisib) — ancak
destekleyici emsali askıya alınmış bir çalışmadır, olgunlaşmış sonuç verisi değil.

## 5. Onkolog ile paylaşılması gereken temel güvenlik uyarıları
- **Örtüşen toksisiteler:** miyelosupresyon (alkilleyiciler + checkpoint inhibitörleri),
  QT uzaması (çeşitli ajanlar), hepatotoksisite (disülfiram, statinler, valproat),
  retinopati (klorokin, kümülatif doz).
- **İlaç-ilaç etkileşimleri:** disülfiram-alkol reaksiyonu (kesinlikle kaçınılmalı), valproatın
  enzim etkileri, statin-CYP etkileşimleri.
- **ERCC5 P19L VUS (VAF %78)** germline-analiz eşiğinde yer alıyor — germline durumunun
  doğrulanması değerli olacaktır, çünkü nükleotid-eksizyon-tamir genleri platin/alkilleyici
  işlenmesini etkileyebilir.
- **Sıralama ve zamanlama**, ilaç seçimi kadar önemlidir (örn. checkpoint-inhibitör
  zamanlamasının radyoterapiye göre ayarlanması).

---

---

## 7. Literatür kanıt katmanı (OpenAlex üzerinden doğrulanmış, birincil GBM referansları)

Her aday ilaç, GBM bağlamındaki en iyi klinik veya mekanistik referansına bağlanmıştır. Kanıt *derecesi*, varlığı kadar önemlidir — randomize negatif bir çalışma, umut verici bir preklinik sinyalden daha ağır basar.

| İlaç | En iyi GBM referansı | Yıl | Kanıt derecesi | Bulgu / not |
|------|-------------------|------|----------------|----------------|
| Paxalisib | [Wen et al., paxalisib in newly diagnosed GBM, unmeth](https://doi.org/10.1200/jco.2022.40.16_suppl.2047) | 2022 | Klinik (Faz 2, ASCO) | Beyne nüfuz edebilen PI3K/mTOR inhibitörü; Rejim B/C dayanağının arkasındaki temel GBM programı. |
| Metformin | [Sato et al., Glioma-initiating cell elimination by m](https://doi.org/10.5966/sctm.2012-0058) | 2012 | Preklinik mekanizma | Metformin, AMPK-FOXO3 yoluyla glioma kök hücrelerini tüketir. |
| Metformin | [Metformin inhibits growth of human GBM cells & enhan](https://doi.org/10.1371/journal.pone.0123721) | 2015 | Preklinik | Metformini GBM'de kemo/RT duyarlılaştırıcısı olarak destekler. |
| Disülfiram+Cu **⚠ NEGATİF** | [DIRECT: Disulfiram+Copper + chemo vs chemo alone in ](https://doi.org/10.1001/jamanetworkopen.2023.4149) | 2023 | Klinik (Randomize, JAMA Netw Open) | ANAHTAR NEGATİF SONUÇ: DIRECT randomize çalışması (n=88, nüks GBM) — kemoterapiye eklenen disülfiram+Cu, 6 aylık sağkalımı anlamlı ölçüde iyileştirmedi. |
| Disülfiram+Cu | [Skrott et al. mechanism — disulfiram/Cu targets NPL4](https://doi.org/10.3390/cells9020469) | 2020 | Preklinik mekanizma | Moleküler temel: Cu-DDC, NPL4'ü agrege eder -> proteotoksik stres. |
| Klorokin/HCQ | [Phase I/II hydroxychloroquine + RT/TMZ in newly diag](https://doi.org/10.4161/auto.28984) | 2014 | Klinik (Faz I/II) | Otofaji inhibisyonu; kemoradyoterapi ile tolere edilebilir HCQ dozu belirlendi (doz-sınırlayıcı toksisite gözlendi). |
| Atorvastatin | [Anticancer effects of mevalonate-pathway modulation ](https://doi.org/10.1038/bjc.2014.431) | 2014 | Preklinik | Gliomda statin/mevalonat blokajı gerekçesi. |
| Selekoksib | [CUSP9* protocol for recurrent GBM (celecoxib is a co](https://doi.org/10.18632/oncotarget.2408) | 2014 | Protokol / gerekçe | Selekoksib, çok-hedefli CUSP9 tasarımındaki 9 yeniden konumlandırılmış ilaçtan biri olarak. |
| Mebendazol | [Antiparasitic mebendazole shows survival benefit in ](https://doi.org/10.1093/neuonc/nor077) | 2011 | Preklinik | Klinik ilgiyi başlatan temel GBM etkinlik sinyali (JHU). |
| Valproik asit | [Postradiation sensitization by HDAC inhibitor valpro](https://doi.org/10.1158/1078-0432.ccr-08-0643) | 2008 | Preklinik (radyoduyarlılaştırma) | HDAC-i radyoduyarlılaştırma; sonraki klinik GBM verileri karışık — dikkatli yorumlanmalı. |
| Adavosertib(WEE1) | [WEE1 inhibitor adavosertib with radiation in diffuse](https://doi.org/10.1093/noajnl/vdac073) | 2022 | Klinik (erken faz) | Gliomda WEE1 abrogasyonu + RT; p53-null sentetik-letal handle uygulamada. |
| ATR inhibitörü | [DNA damage response inhibitors (ATR-CHK1-WEE1) for g](https://doi.org/10.1093/noajnl/vdab015) | 2021 | Derleme (mekanizma/klinik durum) | p53 kaybından ve telomer stresinden kaynaklanan replikasyon stresine karşı ATR inhibisyonunu çerçeveler. |
| 6-tio-dG | [Telomerase-targeted strategies incl. 6-thio-dG (telo](https://doi.org/10.1186/s13073-016-0324-x) | 2016 | Derleme / mekanizma | TERT+ durumunu hedeflemenin gerekçesi; 6-tio-dG deneyseldir, eczaneden temin edilemez. |
| CUSP9 protokolü | [Kast et al., conceptual multi-drug 'Coordinated Unde](https://doi.org/10.18632/oncotarget.969) | 2013 | Kavram / gerekçe | Sizin izlediğiniz tüm-zayıflıkları-aynı-anda-hedefleme stratejisinin orijinal çerçevesi. |
| CUSP9 protokolü | [Efficacy of coordinated pharmacological blockade in ](https://doi.org/10.1007/s00432-019-02920-4) | 2019 | Preklinik doğrulama | Birleşik blokajın GBM kök hücrelerini etkilediğine dair preklinik destek. |

---

## 6. Bunun neden tek seferlik değil bir *sistem* olduğu
Bu dosyada yer alan dosyalar makine tarafından okunabilir ve yeniden çalıştırılabilir:
- `vulnerability_map.json` — tümörün zayıflıkları ve bunların hedeflenebilir düğümleri
- `drug_candidates.json` — zayıflıklar + kan-beyin bariyeri + erişilebilirlikle eşleştirilmiş aday ilaçlar
- `candidate_regimens.json` — emsal çalışmalarla birlikte kombinasyon rejimleri
- `combination_engine.py` — kapsamı yeniden puanlar, boşlukları işaretler ve canlı kanıtı yeniden sorgular
- `coverage_matrix.png` — ilaç × zayıflık görseli

Herhangi bir yeni sonuçtan sonra (yeni mutasyon, yeni çalışma, erişilemez hale gelen bir ilaç)
motorun yeniden çalıştırılması, sıralanmış rejimleri ve kanıt bağlantılarını yeniden üretir. **Sonraki
iterasyonlar** şunları yapabilir: (1) ChEMBL'den ADMET/kan-beyin bariyeri niceliklendirmesi ekleme, (2) uygunluğu kontrol etmek için
belirli aktif çalışmaların tam uygunluk kriterlerini çekme, (3) ilaç-ilaç etkileşim puanlaması ekleme, (4) yeniden konumlandırma
kütüphanesini genişletme (örn. CUSP9 setinin tamamı).