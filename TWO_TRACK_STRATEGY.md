# İki-Yollu Tedavi Stratejisi — Rekürren GBM (IDH-yabanıl tip, RTK1)

## Amaç ve tasarım mantığı

**Amaç.** Bu tümörün spesifik moleküler zayıflıklarından kan-beyin bariyeri (BBB)'ni geçebilen ilaç kombinasyonlarına — hem onkoloji ajanlarını hem de yeniden kullanılabilir, eczaneden erişilebilir ilaçları kapsayan — kanıta dayalı, yapılandırılmış bir harita; birden fazla hayatta-kalma yolağına *aynı anda* saldırmak üzere tasarlanmıştır.

---

### Tasarım mantığı — "sürücüleri kapsa, kaçışları engelle"

Tüm zayıflıklara *aynı anda* saldırma hedefiyle örtüşen nüks-GBM literatürü katmanlı bir tasarımda birleşmektedir. Bu belge bu tasarımı takip eder:

1. **Önce truncal sürücüler.** TERT (V1) ve TP53 kaybı (V2) truncal'dır — esasen her tümör hücresinde mevcuttur. Bunları göz ardı eden bir rejim tümörün yalnızca bir kısmını tedavi eder.
2. **p53-null sentetik-öldürücü fırsatı (V2) en güçlü hedeflenmiş fırsattır.** G1/S kontrol noktası devre dışı kaldığında, hücreler DNA hasarından kurtulmak için **G2/M kontrol noktasına** (WEE1/ATR/CHK1) bağımlı hale gelir. Bu kontrol noktasını kaldırmak *ile aynı zamanda* bir DNA-hasar kaynağı (radyasyon veya alkilleyici ajan) uygulamak hücreleri ölümcül mitotik felakete iter. Bu gerçek, gen-eşleşmeli bir zayıflıktır — genel bir sitotoksik değildir.
3. **Büyüme ve hayatta-kalma pompalarını kapat (V3, V4).** PI3K/mTOR ve NF-κB aktive olmuş iki hayatta-kalma eksenidir; beyne nüfuz edebilen inhibitörler + yeniden kullanılabilen baskılayıcılar her ikisine de vurur.
4. **Metabolik/otofaji kaçış yollarını aç bırakma (V7).** Hedeflenmiş stres altındaki tümörler otofaji ve metabolik esneklik yoluyla hayatta kalır — yeniden kullanım katmanı (metformin, statin, klorokin, disülfiram) bu kapıları kapatır.
5. **İmmünoterapiye aşırı yatırım yapma (V8).** Soğuk profil, tek-ajan checkpoint inhibitörlerinden az bir yarar öngörür; mikroçevre modülatörleri (örn. celecoxib) yardımcı ajanlardır, ana kaldıraç değil.

---

## İlaç sınıflandırması — etiket açıklaması

Her ilacın yanında `[ ]` içinde erişim/kullanım sınıfı belirtilmiştir:

| Etiket | Anlamı |
|--------|--------|
| `[repurpose]` | GBM-dışı endikasyonda onaylı, eczaneden erişilebilir; **GBM'de kullanımı off-label** (Metformin=diyabet, Simvastatin=kolesterol, Hidroksiklorokin=sıtma/romatoloji ilacı) |
| `[onkoloji]` | GBM'de **onaylı/standart** onkoloji ilacı (Temozolomid, Bevacizumab) |
| `[onkoloji · off-label]` | Başka kanserde onaylı onkoloji ilacı, **GBM'de off-label** (Regorafenib — GBM'de REGOMA faz-2 verisi) |
| `[deneme]` | **Araştırma aşaması** — henüz tam onaylı değil, klinik çalışma/genişletilmiş erişim gerekir (Paxalisib, WEE1i, Marizomib, 6-thio-dG) |
| `[destek]` | Tümör hedefi değil — **nöbet kontrolü** (antiepileptik: Keppra, Lamide) |

> **repurpose vs off-label farkı:** Her repurpose ilaç GBM'de off-label kullanılır. Ayrımı şöyle yaptık: `[repurpose]` = aslında kanser-dışı bir ilaç (eczane); `[onkoloji · off-label]` = zaten bir onkoloji ilacı ama GBM dışı bir kanser için onaylı.

---

## Hızlı başla, denemeleri paralel yürüt, zaman kaybetme

**Temel ilke:** tümörü hedeflemeye başlamak için deneme ilaçlarını bekleme. Hızlı, erişilebilir ilaçlarla *şimdi* mümkün olduğunca çok zayıflığı kapsa; deneme-kapılı hedefli ilaçları *paralel* olarak takip et; ve deneme yolu tıkanır ya da reddedilirse tümörün her cepheden baskı altında kalmasını sağlayan bir yedek planı hazır tut.

![Erişim hızına göre kapsam — güncel ilaçlar]({{artifact:c498e211-8729-48fd-a5f5-770408e28231}})

**Kapsam haritasından ana bulgu:** hızlı yollar (repurposing + erişilebilir onkoloji) birlikte **8 zayıflığın 7'sini hemen** hedefleyebiliyor. Yalnızca **TERT/telomer ekseni (V1)** ve **temiz p53-null sintetik-letal vuruş (V2)** gerçekten deneme ilaçlarına ihtiyaç duyuyor.

---

## Tümörün zayıflık parmak izi (V1–V8)

Aşağıdaki stratejilerdeki her ilaç, bunlardan bir veya birkaçını vurmak için seçildi. Doğrudan 2026-05-21 genomik profilleme özetinden türetildi.

| # | Değişiklik (rapordan) | Klonalite | Ne yapıyor | Hedeflenebilir düğüm |
|---|---------------------------|-----------|------------|----------------------|
| V1 | **TERT** promotör C250T | Truncal sürücü (VAF %23) | Telomerazı yeniden aktive eder → ölümsüzlük | Telomer replikasyon stresi (ATR), telomeraz substratı |
| V2 | **TP53** kaybı — splice + Y163N + G245S + P152L | Truncal / eş-klonal (~%24–25) | G1/S kontrol noktası kayıp → tümör DNA hasarında hayatta kalmak için **G2/M kontrol noktasına** dayanır | **WEE1, CHK1, ATR, PLK1** |
| V3 | **PTEN** R130\* + **kromozom 10 kaybı** | Geniş chr10 kaybında subklonal PTEN | **PI3K/AKT/mTOR** yolağını serbest bırakır | Beyin-geçişli PI3K/mTOR, AMPK |
| V4 | **NFKBIA** delesyonu (14q13.2) | Fokal delesyon | IκB-α kaybı → sürekli **NF-κB** hayatta-kalma sinyali | NF-κB, proteazom ekseni, kök-hücresellik |
| V5 | **MGMT** promotör **metillenmemiş** | Biyobelirteç | Aktif MGMT alkilasyonu onarır → **temozolomid direnci** | MGMT'den bağımsız yollar; duyarlılaştırıcılar |
| V6 | **TCF7L2** delesyonu (10q25) | Fokal delesyon | Wnt/β-katenin bozulması (bağlama bağlı) | Wnt/GSK3 (keşifsel, düşük öncelik) |
| V7 | GBM **metabolik** fenotipi | Soy düzeyinde | Warburg glikolizi, mevalonat/kolesterol bağımlılığı, otofaji ile hayatta kalma | OXPHOS, HMG-CoA, otofaji/lizozom |
| V8 | **İmmünolojik olarak soğuk** (TMB 4.7, MSS, HRD−, PD-L1 0) | Biyobelirteç | Düşük neoantijen yükü → tek-ajan kontrol noktası blokajı olası değil | Mikroçevre / miyeloid modülasyonu |

**Hızlı-yol erişilebilirliği:** V3, V4, V5, V6, V7, V8 repurposing + erişilebilir-onkoloji ilaçlarıyla (Strateji 1) **şimdi tam olarak** hedeflenebilir. **V2** şu an yalnızca *kısmen/yaklaşık* hedeflenebilir (alkilleyici + mebendazol/valproat mitotik stresi üzerinden) — **temiz** sintetik-letal vuruşu deneme ilaçları (WEE1/ATR) gerektirir. **V1 (TERT)** deneme ilaçları olmadan **hiç** hedeflenemez. Yani gerçekten deneme erişimine bağımlı olan iki zayıflık **V1 (tamamen) ve V2 (temiz vuruş için)**; geri kalan her şey hemen başlayabilir.

---

## Başlangıç ilaç öncelik sıralaması — hangi ilaçla, hangi sırayla başlanmalı

Aşağıdaki tablo, hızlı/erişilebilir omurganın ilaçlarını **hangi sırayla eklenmesi gerektiğine** göre dizer. Hepsini aynı gün başlatmak yerine, bu sırayla **adım adım eklemek** hedeflenir: her basamak yeni bir zayıflık veya güç ekler, ama toksisite de arttığı için her ilacın tolere edildiği doğrulandıktan sonra bir sonrakine geçilir. Beş ilacın tamamı eklendiğinde, aşağıdaki **K3 (geniş hızlı omurga)** kombinasyonuna ulaşılmış olur.

**Zemin (hasta zaten kullanıyor):** Altuzan (bevacizumab, V7/V8) + Keppra + Lamide.

| Sıra | İlaç | Açtığı zayıflık | Neden bu sırada | Basamak |
|------|------|------------------|------------------|---------|
| **1** | **İrinotekan** `[onkoloji]` (veya Temozolomid/Lomustin) | DNA-hasar zemini (irinotekan: topo-I; TMZ/lomustin: alkilleyici) | Omurga sitotoksik; diğer her şeyin üzerine eklenen DNA-hasar kaynağı. İrinotekan farklı mekanizma + bev-sinerjisi için tercih (bkz. BNCT-sonrası bölüm) | ↓ |
| **2** | **Metformin** `[repurpose]` | V3 + V7 (OXPHOS) | En düşük toksisite, **QT-nötr** (Lamide ile tam uyumlu), güçlü metabolik duyarlılaştırma | ↓ |
| **3** | **Simvastatin** `[repurpose]` | V7 (mevalonat — farklı düğüm) | Yine düşük toksisite, QT-nötr; metforminden **ayrı** bir metabolik düğümü vurur | **← en güvenli çekirdek (ilk 3 ilaç; tamamen QT-nötr, Lamide ile uyumlu)** |
| **4** | **Hidroksiklorokin** `[repurpose]` | **V4 (NF-κB)** + V7 otofaji | Yeni bir zayıflık (V4) açar — ama **QT uzatır** → Lamide nedeniyle bazal + takip **EKG** ve yıllık **göz muayenesi** şart | **← +V4 basamağı (buradan itibaren EKG + göz takibi başlar)** |
| **5** | **Regorafenib** `[onkoloji · off-label]` | V3 + V8 (multikinaz) | En güçlü erişilebilir-onkoloji kanıtı (REGOMA randomize) — ama **en yüksek toksisite**: karaciğer (kara kutu) + Altuzan ile hipertansiyon istifi | **← burası tam K3** |

**Okuma:** Metformin + Simvastatin güvenli, QT-nötr **oral** çekirdektir; buna DNA-hasar omurgası olarak **irinotekan** eklenir (topo-I; QT-nötr değil — nötropeni/ishal/nöbet/UGT1A1 kendi izlemini gerektirir; erişim gecikirse TMZ/lomustin). Tolere edilince **Hidroksiklorokin** `[repurpose]` eklenir (V4 kapsamı açılır) — buradan itibaren EKG + göz takibi gerekir. En son, en güçlü ama en toksik ilaç **Regorafenib** `[onkoloji · off-label]` eklenir; bu noktada aşağıdaki **K3** kombinasyonuna ulaşılır. Yani başlangıç, tek bir kademeli titrasyon yoludur.

---

## Neden aynı zayıflığa birden çok ilaç? — düğüm haritası

Bir zayıflık (ör. V7 metabolik) tek bir hedef değildir; içinde **birden çok ayrı mekanizma düğümü** barındırır. Aynı zayıflığı birden çok ilaçla vurmak, ilaçlar **farklı düğümlerden** vuruyorsa değerlidir (çok-cepheli kuşatma); **aynı düğümü aynı şekilde** vuruyorsa ikincisi çoğu zaman ek fayda getirmeden yalnızca toksisite ekler.

![Zayıflık → mekanizma düğümü → ilaç haritası]({{artifact:31e91138-7174-4bc2-8120-b97cbaec3e2d}})

**Haritanın okunuşu:**
- **Mavi çubuk = tek ilaç (benzersiz düğüm)** — gerçek katkı. Örn. V7 içinde **Bevacizumab (damar)**, **Metformin (OXPHOS/mitokondri)** ve **Simvastatin (mevalonat/lipid)** üç *ayrı* düğümdedir → gereksiz tekrar değil, tümörü aynı anda damardan, enerjiden ve yapı-taşından sıkıştırmak.
- **Kırmızı çubuk = aynı düğümde 2+ ilaç (çakışma)** — dikkat gereken tekrar. Haritadaki iki kırmızı satırın ikisinde de **İtraconazol** var (otofaji düğümünde HCQ ile, damar düğümünde Bevacizumab ile çakışıyor). Açtığı her düğüm zaten kapalı olduğu ve en ağır CYP3A4 + QT yükünü getirdiği için **itraconazol kombinasyonlardan çıkarıldı**.
- **★ = hasta zaten kullanıyor** (Bevacizumab/Altuzan).
- **V4/NF-κB'de yükseltme:** artık *doğrudan* proteazom düğümü (Marizomib) var — önceden yalnızca HCQ'nun *dolaylı* etkisi vardı.

Tam düğüm-düzeyi analiz `REDUNDANCY_ANALYSIS.md` dosyasındadır.

---

## Kombinasyon detayları (K3 başlangıç · K4/K5 deneme yükseltmeleri)

**Prensip:** her tümör zayıflığını, **her mekanizma düğümüne tek güçlü ilaç** koyarak, organ toksisitesini üst üste yığmadan hedeflemek (bkz. yukarıdaki düğüm haritası ve `REDUNDANCY_ANALYSIS.md`).

Aşağıda üç kombinasyon **kendi içinde tam** olarak veriliyor — her biri mevcut üç ilacı (Altuzan/Keppra/Lamide) tekrar gösterir:
- **K3** = hızlı omurganın tam hâli (deneme gerekmez) — **başlangıç noktası**.
- **K4** = K3 zeminine deneme sintetik-letal çekirdeği (paxalisib + WEE1i).
- **K5** = kanıt + beyin-konsantrasyonu optimize (V4'ü doğrudan Marizomib ile vurur, statin simvastatin).

> **En önemli kısıt:** Lamide (lakozamid) kardiyak iletimi etkiler → QT-uzatan bir ilaç (hidroksiklorokin) eklenirse **bazal + takip EKG şart** (FDA lakozamid etiketi). Üçüncü bir antiepileptik olan valproik asit geri planda tutuldu.

![Minimum-toksisite kombinasyonları — kapsam vs toksisite]({{artifact:84c68191-a3aa-4f0b-a484-3469c9f141ca}})


## ⚡ BNCT sonrası güncelleme (Temmuz 2026) — acil TMZ ikamesi ve DNA-hasar ekseni

**Klinik bağlam (güncel):** Hasta ilk cerrahi + radyoterapi sonrası ~18 ay nükssüz kaldı; nüks **TMZ + bevacizumab rejimi altındayken** gelişti. İkinci rezeksiyon multifokal/dağınık tümör nedeniyle **BNCT (bor-nötron yakalama tedavisi)** ile tamamlandı; taze NGS **BNCT sonrası** alındı. Bu üç olgu (TMZ altında ilerleme · MGMT-metilsiz · BNCT sonrası) ilaç önceliklerini aşağıdaki gibi kaydırır.

### TMZ'nin yeri — neden ana eksen değil, ama neden tümüyle atılmıyor
TMZ hasta tarafından **çok iyi tolere edildi** (bevacizumab gibi) — bu bir avantaj. Ancak: (a) MGMT promotör **metilsiz** olduğunda metilguanin-metiltransferaz DNA onarımı sürer ve alkilleyici faydası düşer ([Hegi 2005](https://doi.org/10.1056/NEJMoa043331)); gerçekten metilsiz tümörde TMZ'den fayda gösterilememiştir ([Hegi 2024](https://doi.org/10.1093/neuonc/noae108)); ilerleyen GBM'de TMZ yeniden-uygulaması faydası için MGMT metilasyonu güçlü bir prognostik biyobelirteçtir ([DIRECTOR / Clin Cancer Res 2015](https://doi.org/10.1158/1078-0432.CCR-14-2737)). (b) Tümör **TMZ içeren rejim altında** ilerledi — mekanizma "kesin direnç mi, doğal seyir/klonal evrim mi" olsa da, pratik sonuç: TMZ şu anki tümörü kontrol etmedi. **Sonuç:** TMZ omurga yapılmaz; ancak iyi tolere edildiği için aşağıda **köprü seçeneği** olarak kalır.

### Acilen ne konmalı? — katmanlı yanıt
"TMZ yerine ne?" sorusu iki hızda yanıtlanır — biri mekanik-ideal ama erişim gerektirir, biri hemen erişilebilir köprüdür. **İkisi paralel yürür: köprüyü hemen başlat, ideal ajanın erişimini şimdi aç.**

| Öncelik | Etken madde | Neden (BNCT sonrası mantık) | Erişim | Kanıt |
|---|---|---|---|---|
| **1 — mekanik-ideal (erişimi ŞİMDİ aç)** | **WEE1i** (adavosertib / Debio 0123) veya **ATRi** (ceralasertib) `[deneme]` | BNCT bir **radyasyon** modalitesidir → DNA çift-zincir kırığı. Nüks GBM hücreleri radyasyondan **ATM↔ATR geçişiyle** ve G2/M kontrol noktasına sığınarak kaçar; hastanın **TP53-null** durumu bu kontrol noktasını zaten kırılgan yapar → DDR inhibisyonu hem **radyoduyarlılaştırıcı** hem **p53-null sintetik-letal**. | Deneme / off-label — haftalar sürebilir | [Kaur 2022, ATM/ATR geçişi](https://doi.org/10.1007/s12032-022-01657-4) · [Cetin 2023, WEE1 radyoduyar. — *EGFRvIII-özgü*](https://doi.org/10.1186/s13014-023-02210-x) · [Mueller 2013, WEE1+RT — *pediatrik HGG*](https://doi.org/10.1093/neuonc/not220) — *tümü preklinik; erişkin GBM'de BNCT-sonrası randomize kanıt yok* |
| **2 — erişilebilir KÖPRÜ (hemen başlat)** | **İrinotekan** `[onkoloji]` | Topoizomeraz-I inhibitörü → **alkilleyicilerden farklı DNA-hasar düğümü** (stratejiye yeni mekanizma ekler, tekrar etmez); **MGMT'den bağımsız**; hasta **zaten Altuzan aldığından** GBM'de kanıtlı bev-sinerjisi (BRAIN faz II: bev+irinotekan PFS-6 %50,3 vs %42,6, yanıt %37,8 vs %28,2 — ancak OS farkı yok). **Doz uyarısı:** nöbet riskini artırır (Keppra/Lamide ile izlem); Keppra/Lamide enzim-indükleyici *olmadığından* düşük-doz koluna uyar; **UGT1A1** testi önerilir. | Eczane/onkoloji — hemen | [Friedman 2009, BRAIN](https://doi.org/10.1200/JCO.2008.19.8721) · [DPWG UGT1A1 2022](https://doi.org/10.1038/s41431-022-01243-2) · [EIAED-PK 2015](https://doi.org/10.1002/jcph.543) |
| **2-yedek — alkilleyici köprü** | **Lomustin (CCNU)** `[onkoloji]` | İrinotekana erişim gecikirse; nüks GBM standart ikinci-basamak alkilleyici, bev ile kombine çalışılmış (BELOB). Aynı alkilleme eksenini tekrarladığından yeni düğüm eklemez → ikinci tercih. | Eczane/onkoloji | [Weller 2020, lomustin standardı](https://doi.org/10.1016/j.ctrv.2020.102029) · [Taal 2014, bev±lomustin](https://doi.org/10.1016/S1470-2045(14)70314-6) |
| **2-alt — köprü (tolerans avantajı)** | **Metronomik TMZ** (50 mg/m²/gün sürekli) + MGMT-düşürücü `[onkoloji]` | Hasta TMZ'yi iyi tolere etti; metronomik şema kümülatif maruziyeti artırır. Beklenen fayda düşük (metilsiz) ama toksik değil; **levetirasetam (zaten alıyor) + fluoksetin** MGMT-düşürücü rasyoneliyle birlikte spekülatif kurtarma. | Eczane/onkoloji — hemen | [DIRECTOR / Clin Cancer Res 2015](https://doi.org/10.1158/1078-0432.CCR-14-2737) |

> **Karar mantığı:** İrinotekan (farklı-mekanizma sitotoksik omurga; erişim gecikirse lomustin veya iyi-tolere-edilen metronomik TMZ) **köprü** olarak boşluk bırakmadan başlar; WEE1i/ATRi erişimi paralel açılır ve geldiğinde köprünün yerini alır (veya kontrollü biçimde eklenir). Böylece "başvuru uzarsa zaman kaybetme" riski ortadan kalkar.

### Bevacizumab (Altuzan) — korunur, artık ikinci bir gerekçesi var
Bevacizumab hem çok iyi tolere edildi hem de BNCT sonrası ek kanıtlı bir rol kazandı: BNCT nüks malign gliomda radyasyon nekrozunu artırır ve bevacizumab bu radyasyon hasarını azaltmak için değerlendirilmiştir ([Furuse 2022, BNCT+bevacizumab](https://doi.org/10.1093/jjco/hyac004)); beyin radyasyon nekrozunda bevacizumab randomize/plasebo-kontrollü olarak çalışılmıştır ([Levin 2011, RT-nekroz](https://doi.org/10.1016/j.ijrobp.2009.12.061)). Yani BNCT sonrası hastada bevacizumab **tümör-hedefli + radyasyon-nekrozu önleyici** çift rol taşır.

### K3 — Geniş hızlı omurga ⭐ BAŞLANGIÇ KOMBİNASYONU
**Kapsam:** 6/8 zayıflık (V2, V3, V4, V5, V7, V8) · Yukarıdaki öncelik sıralamasının **tam hâli** (5 ilaç eklendiğinde ulaşılan nokta). Deneme gerektirmez — hepsi hızlı/erişilebilir. Toksisite en yüksek olduğu için yukarıdaki gibi **basamaklı** ulaşılır, tek seferde değil.

> **BNCT sonrası köprü notu:** TMZ ana eksen değildir (MGMT-metilsiz + TMZ altında ilerleme). K3 zemininde TMZ'nin yerine **erişilebilir köprü** olarak öncelikle **irinotekan** (topoizomeraz-I; farklı mekanizma + bev-sinerjisi), erişim gecikirse **lomustin** veya iyi-tolere-edilen **metronomik TMZ** kullanılabilir — bkz. üstteki *BNCT sonrası güncelleme* bölümü.

| İlaç | Hangi zayıflığı/düğümü vuruyor | Yarattığı toksisite |
|------|-------------------------------|---------------------|
| _Mevcut ilaçlar (zaten kullanılıyor):_ | | |
| **Altuzan (bevacizumab)** `[onkoloji]` | V7 + V8 — VEGF/anti-anjiyogenez düğümü (damar normalizasyonu, ödem/steroid azaltıcı) — kaynak: [Friedman 2009](https://doi.org/10.1200/jco.2008.19.8721) | Hipertansiyon, GİS perforasyon/kanama, yara iyileşme gecikmesi (ameliyat öncesi ≥28 gün kesilir), proteinüri |
| **Keppra (levetirasetam)** `[destek]` | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | Davranışsal/psikiyatrik etkiler, uyku hâli. Farmakokinetik olarak SESSİZ — diğer ilaçlarla minimal etkileşim (avantaj) |
| **Lamide (lakozamid)** `[destek]` | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | **Kardiyak iletim (PR/QT) etkisi** — QT-uzatan ilaç eklenirse EKG şart; baş dönmesi/ataksi |
| _Bu kombinasyonda eklenenler:_ | | |
| **İrinotekan** `[onkoloji]` | **V2** (DNA-hasar zemini — topoizomeraz-I → replikasyon-stresi kaynaklı çift-zincir kırığı; **MGMT'den bağımsız** — metilsiz tümörde alkilleyici dirence takılmaz). *Not: MGMT/V5 bir biyobelirteçtir, ilaç hedefi değil; irinotekan bu ekseni gerektirmez.* — kaynak: [Friedman 2009, BRAIN](https://doi.org/10.1200/JCO.2008.19.8721) | Nötropeni, ishal, **nöbet riski↑** (Keppra/Lamide ile izlem), UGT1A1 farmakogenetiği |
| **Metformin** `[repurpose]` | V3 (PI3K/mTOR — AMPK üzerinden dolaylı) + V7 (OXPHOS/kompleks-I) — kaynak: [Sato 2012](https://doi.org/10.5966/sctm.2012-0058) · [Sesen 2015](https://doi.org/10.1371/journal.pone.0123721) | Laktik asidoz (kara kutu, böbrek yetmezliğinde), B12 eksikliği, GİS. Düşük genel toksisite |
| **Simvastatin** `[repurpose]` _(atorvastatin yerine)_ | V7 (mevalonat/kolesterol düğümü) — kaynak: [Alizadeh 2017](https://doi.org/10.1038/srep44841) · [Jiang 2021](https://doi.org/10.1186/s13046-021-02041-2) | Miyopati/rabdomiyoliz (nadir), karaciğer enzim artışı, hafif hiperglisemi. **Beyin geçişi atorvastatinden daha iyi** (pano: ölçülmüş-iyi); ⚠ CYP3A4 substratı — itraconazol ile kontrendike (zaten kullanılmıyor) |
| **Hidroksiklorokin** `[repurpose]` | V4 (NF-κB) + V7 (otofaji/lizozom düğümü — hayatta-kalma kaçışını kapatır) — kaynak: [Rosenfeld 2014](https://doi.org/10.4161/auto.28984) | **QT uzaması** (Lamide ile EKG şart), **geri dönüşsüz retinopati** (yıllık göz muayenesi), kardiyomiyopati |
| **Regorafenib** `[onkoloji · off-label]` | V3 (multikinaz) + V8 (anti-anjiyogenez) — REGOMA randomize kanıtı — kaynak: [Lombardi 2019 (REGOMA)](https://doi.org/10.1016/s1470-2045(18)30675-2) | **Hepatotoksisite (kara kutu)**, hipertansiyon (Altuzan ile istiflenir), el-ayak sendromu, GİS |

**Bu kombinasyonun toksisite tablosu:** dört ilaçlık hızlı çekirdeğe (İrinotekan + Metformin + Simvastatin + Hidroksiklorokin; yedek TMZ/lomustin) **Regorafenib** `[onkoloji · off-label]` eklenir (V3 multikinaz, REGOMA randomize kanıtı). **İki yeni risk istiflenir:** (1) **karaciğer** — Regorafenib kara kutu hepatotoksisite + simvastatin → karaciğer testleri sık; (2) **hipertansiyon** — Regorafenib + mevcut **Altuzan (bevacizumab)** `[onkoloji]` kan basıncını üst üste bindirir. Hidroksiklorokin QT'si + Lamide nedeniyle **EKG** yine şart. Zayıflık kapsamı Regorafenibsiz hâle göre artmaz — ek fayda multikinaz gücünde, ek maliyet toksisitede.

### K4 — Deneme eklenmiş (sintetik-letal çekirdek)
**Kapsam:** 6/8 zayıflık (V2, V3, V4, V5, V7, V8) + V2'ye TEMİZ vuruş · **Toplam toksisite skoru:** 27 · Deneme ilaçları erişilebilirse en güçlü V2 hedeflemesi.

> **BNCT sonrası öncelik:** K4'teki **WEE1i / ATRi** artık yalnızca V2 sintetik-letal değil — BNCT bir radyasyon modalitesi olduğundan bu ajanlar aynı zamanda **radyoduyarlılaştırıcıdır** (nüks GBM'in ATM↔ATR kaçışını ve p53-null G2/M bağımlılığını hedefler). Bu, K4'ü **BNCT sonrası en yüksek mekanik-uyumlu** yükseltme yapar; erişim başvurusu şimdi açılmalıdır. **Kanıt kapsamı uyarısı:** radyoduyarlılaştırma verisi ağırlıkla **preklinik** ve yan-grup/pediatriktir — Cetin 2023 **EGFRvIII-pozitif** GBM hücrelerine özgü, Mueller 2013 **pediatrik** yüksek-dereceli gliom/DIPG modelidir; erişkin GBM'de **BNCT-sonrası randomize klinik kanıt yoktur**. Bu güçlü bir *mekanistik zamanlama* gerekçesidir, kanıtlanmış klinik fayda değil.

| İlaç | Hangi zayıflığı/düğümü vuruyor | Yarattığı toksisite |
|------|-------------------------------|---------------------|
| _Mevcut ilaçlar (zaten kullanılıyor):_ | | |
| **Altuzan (bevacizumab)** `[onkoloji]` | V7 + V8 — VEGF/anti-anjiyogenez düğümü (damar normalizasyonu, ödem/steroid azaltıcı) — kaynak: [Friedman 2009](https://doi.org/10.1200/jco.2008.19.8721) | Hipertansiyon, GİS perforasyon/kanama, yara iyileşme gecikmesi (ameliyat öncesi ≥28 gün kesilir), proteinüri |
| **Keppra (levetirasetam)** `[destek]` | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | Davranışsal/psikiyatrik etkiler, uyku hâli. Farmakokinetik olarak SESSİZ — diğer ilaçlarla minimal etkileşim (avantaj) |
| **Lamide (lakozamid)** `[destek]` | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | **Kardiyak iletim (PR/QT) etkisi** — QT-uzatan ilaç eklenirse EKG şart; baş dönmesi/ataksi |
| _Bu kombinasyonda eklenenler:_ | | |
| **Metformin** `[repurpose]` | V3 (PI3K/mTOR — AMPK üzerinden dolaylı) + V7 (OXPHOS/kompleks-I) — kaynak: [Sato 2012](https://doi.org/10.5966/sctm.2012-0058) · [Sesen 2015](https://doi.org/10.1371/journal.pone.0123721) | Laktik asidoz (kara kutu, böbrek yetmezliğinde), B12 eksikliği, GİS. Düşük genel toksisite |
| **Simvastatin** `[repurpose]` _(atorvastatin yerine)_ | V7 (mevalonat/kolesterol düğümü) — kaynak: [Alizadeh 2017](https://doi.org/10.1038/srep44841) · [Jiang 2021](https://doi.org/10.1186/s13046-021-02041-2) | Miyopati/rabdomiyoliz (nadir), karaciğer enzim artışı, hafif hiperglisemi. **Beyin geçişi atorvastatinden daha iyi** (pano: ölçülmüş-iyi); ⚠ CYP3A4 substratı — itraconazol ile kontrendike (zaten kullanılmıyor) |
| **Hidroksiklorokin** `[repurpose]` | V4 (NF-κB) + V7 (otofaji/lizozom düğümü — hayatta-kalma kaçışını kapatır) — kaynak: [Rosenfeld 2014](https://doi.org/10.4161/auto.28984) | **QT uzaması** (Lamide ile EKG şart), **geri dönüşsüz retinopati** (yıllık göz muayenesi), kardiyomiyopati |
| **İrinotekan** `[onkoloji]` | **V2** (DNA-hasar zemini — topoizomeraz-I → replikasyon-stresi kaynaklı çift-zincir kırığı; **MGMT'den bağımsız** — metilsiz tümörde alkilleyici dirence takılmaz). *Not: MGMT/V5 bir biyobelirteçtir, ilaç hedefi değil; irinotekan bu ekseni gerektirmez.* — kaynak: [Friedman 2009, BRAIN](https://doi.org/10.1200/JCO.2008.19.8721) | Nötropeni, ishal, **nöbet riski↑** (Keppra/Lamide ile izlem), UGT1A1 farmakogenetiği |
| **Paxalisib** `[deneme]` | V3 (PI3K/mTOR — beyin-geçişli, DİREKT) — deneme ilacı — kaynak: [Wen 2022](https://doi.org/10.1200/jco.2022.40.16_suppl.2047) | Hiperglisemi (sınıf etkisi — Metformin ile kısmen dengelenir), mukozit, ruh hâli değişikliği |
| **WEE1 inhibitörü** `[deneme]` | V2 (p53-null sintetik-letal — G2/M kontrol noktası) — deneme ilacı — kaynak: [Mir 2010](https://doi.org/10.1016/j.ccr.2010.08.011) · [Mueller 2022](https://doi.org/10.1093/noajnl/vdac073) | **Kemik iliği baskılanması** (alkilleyici ile doz-kısıtlayıcı çakışma → sık kan sayımı), bulantı, yorgunluk |

**Bu kombinasyonun toksisite tablosu:** hızlı çekirdek zeminine (İrinotekan + Metformin + Simvastatin + Hidroksiklorokin; yedek TMZ/lomustin) **Paxalisib + WEE1 inhibitörü** (deneme) eklenir. **Ana risk — kemik iliği:** İrinotekan (topo-I) + WEE1 inhibitörü: **kemik iliği örtüşmesi** (nötropeni) → doz-kısıtlayıcı miyelosupresyon riski sürer, sık tam kan sayımı; farklı mekanizmalar (replikasyon-stresi vs G2/M kontrol noktası) olduğundan mitotik-katastrofi açısından potansiyel sinerji, ama toksisite örtüşmesi izlenir (bkz. TOXICITY_PROFILE Bölüm C). *Yedek TMZ/lomustin kullanılırsa alkilleyici+WEE1 aynı ekseni vurur — miyelosupresyon daha da belirgin.* Paxalisib hiperglisemisi **Metformin** `[repurpose]` ile kısmen dengelenir (olumlu örtüşme). Hidroksiklorokin QT'si + **Lamide** → EKG şartı burada da geçerli. Sadece deneme erişimi sağlanırsa.

### K5 — Kanıt + beyin-konsantrasyonu optimize (PANO İNCELEMESİYLE GÜÇLENDİRİLMİŞ)
**Kapsam:** 6/8 zayıflık (V2, V3, V4, V5, V7, V8) + V2'ye TEMİZ vuruş · **V4 artık GÜÇLÜ ilaçla** (dolaylı HCQ değil) · Deneme/yurtdışı erişim gerekli.

> **BNCT sonrası not:** K5 de deneme WEE1i/paxalisib içerir; K4 ile aynı **radyoduyarlılaştırma + sintetik-letal** gerekçesi geçerlidir. K5'in ek üstünlüğü V4'ü doğrudan (Marizomib) vurması ve beyin-konsantrasyonu optimize ilaç seçimidir.

> **Fark:** `PANO_INCELEME_kanit_ve_hucre_ici_duzey.md` çapraz-analizinde hem kanıt hem
> beyin-konsantrasyonu (hücre-içi yeterli düzey) kriterini geçen adaylarla kurulmuştur. İki
> kritik iyileştirme: (1) **V4/NF-κB'yi HCQ'nun *dolaylı* etkisi yerine Marizomib** (beyin-geçen
> proteazom inhibitörü, GBM insan çalışması) ile *doğrudan* hedefler; (2) **statin simvastatin**
> (beyin geçişi daha iyi). Marizomib **miyelosupresyon EKLEMEZ**, bu yüzden K4 kombinasyonundaki kemik
> iliği darboğazını büyütmez.

| İlaç | Hangi zayıflığı/düğümü vuruyor | Yarattığı toksisite |
|------|-------------------------------|---------------------|
| _Mevcut ilaçlar (zaten kullanılıyor):_ | | |
| **Altuzan (bevacizumab)** `[onkoloji]` | V7 + V8 — VEGF/anti-anjiyogenez düğümü (damar normalizasyonu, ödem/steroid azaltıcı) — kaynak: [Friedman 2009](https://doi.org/10.1200/jco.2008.19.8721) | Hipertansiyon, GİS perforasyon/kanama, yara iyileşme gecikmesi (ameliyat öncesi ≥28 gün kesilir), proteinüri |
| **Keppra (levetirasetam)** `[destek]` | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | Davranışsal/psikiyatrik etkiler, uyku hâli. Farmakokinetik olarak SESSİZ — diğer ilaçlarla minimal etkileşim (avantaj) |
| **Lamide (lakozamid)** `[destek]` | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | **Kardiyak iletim (PR/QT) etkisi** — QT-uzatan ilaç eklenirse EKG şart; baş dönmesi/ataksi |
| _Bu kombinasyonda eklenenler:_ | | |
| **İrinotekan** `[onkoloji]` | **V2** (DNA-hasar zemini — topoizomeraz-I → replikasyon-stresi kaynaklı çift-zincir kırığı; **MGMT'den bağımsız** — metilsiz tümörde alkilleyici dirence takılmaz). *Not: MGMT/V5 bir biyobelirteçtir, ilaç hedefi değil; irinotekan bu ekseni gerektirmez.* — kaynak: [Friedman 2009, BRAIN](https://doi.org/10.1200/JCO.2008.19.8721) | Nötropeni, ishal, **nöbet riski↑** (Keppra/Lamide ile izlem), UGT1A1 farmakogenetiği |
| **Metformin** `[repurpose]` | V3 (PI3K/mTOR — AMPK üzerinden) + V7 (OXPHOS/kompleks-I) — kaynak: [Sato 2012](https://doi.org/10.5966/sctm.2012-0058) · [Sesen 2015](https://doi.org/10.1371/journal.pone.0123721) | Laktik asidoz (kara kutu, böbrek yetmezliğinde), B12 eksikliği, GİS. Düşük genel toksisite |
| **Simvastatin** `[repurpose]` _(atorvastatin yerine)_ | V7 (mevalonat/kolesterol düğümü) — kaynak: [Alizadeh 2017](https://doi.org/10.1038/srep44841) · [Jiang 2021](https://doi.org/10.1186/s13046-021-02041-2) | Miyopati/rabdomiyoliz, karaciğer enzim artışı. **Beyin geçişi atorvastatinden daha iyi**; ⚠ CYP3A4 substratı |
| **Marizomib** `[deneme]` _(deneme/yurtdışı)_ | **V4 (NF-κB) — DOĞRUDAN, beyin-geçen proteazom inhibitörü** (pano skor 86.7, insan çalışması) — kaynak: [Potts 2011](https://doi.org/10.2174/156800911794519716) | **CNS etkileri** (ataksi, konfüzyon, yorgunluk) — ⚠ Keppra+Lamide üzerine binebilir, nörolojik izlem; periferik nöropati bortezomibden az |
| **Paxalisib** `[deneme]` _(deneme)_ | V3 (PI3K/mTOR — beyin-geçişli, DİREKT) — kaynak: [Wen 2022](https://doi.org/10.1200/jco.2022.40.16_suppl.2047) | Hiperglisemi (Metformin ile dengelenir), mukozit, ruh hâli |
| **WEE1 inhibitörü** `[deneme]` _(deneme)_ | V2 (p53-null sintetik-letal — G2/M kontrol noktası) — kaynak: [Mir 2010](https://doi.org/10.1016/j.ccr.2010.08.011) · [Mueller 2022](https://doi.org/10.1093/noajnl/vdac073) | **Kemik iliği baskılanması** (irinotekan omurgasıyla — yedek TMZ/lomustin kullanılırsa daha belirgin — doz-kısıtlayıcı çakışma → sık kan sayımı) |

> **❌ Dordaviprone (ONC201) DIŞLANDI:** Hastanın **H3K27M testi NEGATİF** olduğu doğrulandı.
> ONC201'in onaylı/güçlü kanıtlı yolu H3K27M-mutant gliomlara özgüdür; bu hasta için uygun
> değildir ve bu kombinasyona dahil edilmemiştir. (İlgili panodaki yüksek skor yalnızca H3K27M-pozitif popülasyona aitti.)

**Bu kombinasyonun toksisite tablosu:** deneme çekirdekli K4 kombinasyonuna kıyasla iki iyileştirme — V4 artık *dolaylı HCQ* değil
*doğrudan Marizomib* ile vuruluyor (HCQ çıkarılırsa **QT/retinopati yükü de düşer**), ve statin
beyin-geçişli simvastatine çevrildi. **Ana risk yine kemik iliği** (irinotekan + WEE1; yedek TMZ/lomustin ise daha belirgin) → sık tam
kan sayımı; ancak Marizomib bu ekseni BÜYÜTMEZ. **Yeni izlem ekseni: CNS** —
Marizomib'in ataksi/konfüzyonu mevcut iki AEİ (Keppra+Lamide) üzerine binebilir. (Dordaviprone/
ONC201, hastanın **H3K27M-negatif** olması nedeniyle bu kombinasyondan çıkarıldı.) Erişim:
Marizomib/paxalisib/WEE1i deneme veya yurtdışı; simvastatin+metformin+irinotekan (yedek TMZ/lomustin) hızlı/ulaşılabilir.

**Özet:** V1 (TERT) ve V6 (Wnt) hızlı ilaçlarla kapanamaz (V1 sadece deneme — ATR-i / 6-thio-dG; V6 doğrudan güçlü ilaç yok, celecoxib sadece dolaylı). Diğer 6 zayıflık, mevcut üç ilaca **minimum ek toksisiteyle** hedeflenebilir. **En güvenli başlangıç, QT-nötr oral çekirdektir** (Metformin + Simvastatin; Lamide ile tam uyumlu); DNA-hasar omurgası **irinotekan** kendi izlemiyle (kan sayımı/nöbet/UGT1A1) eklenir, erişim gecikirse TMZ/lomustin. **Hidroksiklorokin eklendiğinde** V4 de kapsanır ve en iyi kapsam/toksisite dengesine ulaşılır (EKG + göz muayenesi şartıyla) — bu, tam **K3** kombinasyonuna giden yoldur. **K5, deneme/yurtdışı erişim sağlanırsa en güçlü kanıt-temelli seçenektir** — V4'ü doğrudan Marizomib ile vurur ve statin simvastatine çevrilir (pano incelemesi).

*Not: itraconazol bu kombinasyonların hiçbirinde yok — açtığı her düğüm zaten başka ilaçça kapsanıyor ve en ağır CYP3A4 + QT yükünü getiriyor (Lamide/lakozamid varken özellikle riskli).*

---

## Doz notları — 50 kg kadın için kontrol edildi

Aşağıdaki doz sayfaları, K3/K4/K5'teki her ilaç için **50 kg'lık bir kadın hasta** özelinde kontrol edilmiştir (BSA ~1.45 m², 152 cm). Her sayfada beyin geçişi, rol, önerilen doz ve **50 kg için doz kontrolü** bölümü vardır.

| İlaç | Kombinasyon | Doz tipi (50 kg) | Doz notu |
|------|-------------|------------------|----------|
| **İrinotekan** `[onkoloji]` | K3/K4/K5 (birincil omurga) | BSA (mg/m²); non-EIAED → 125 mg/m² kolu; UGT1A1 | Doz sayfası hazırlanabilir |
| **Metformin** `[repurpose]` | K3/K4/K5 | sabit (eGFR'ye bağlı) | [Metformin doz notu]({{artifact:6156e7a7-7a0e-4cb6-99b0-2870995b997f}}) |
| **Simvastatin** `[repurpose]` | K3/K4/K5 | sabit (CYP3A4 sınırlı) | [Simvastatin doz notu]({{artifact:62616a72-626a-4f90-ad16-df4b3d1496d7}}) |
| **Hidroksiklorokin** `[repurpose]` | K3/K4 | ⚠ KİLOYA BAĞLI — ≤250 mg/gün | [Hidroksiklorokin doz notu]({{artifact:ed91448c-6a1c-4825-9d34-1ee2e2fa3a44}}) |
| **Regorafenib** `[onkoloji · off-label]` | K3 | sabit (düşük kütlede azalt) | [Regorafenib doz notu]({{artifact:65bb0b27-5acf-4d3b-a7d4-f98d4f46398c}}) |
| **Paxalisib** `[deneme]` | K4/K5 | sabit (deneme) | [Paxalisib doz notu]({{artifact:19682d31-f46c-4cb4-9c21-d4ffcff44bc7}}) |
| **Adavosertib (WEE1i)** | K4/K5 | sabit (deneme) | [Adavosertib (WEE1i) doz notu]({{artifact:803bb37b-3013-4bee-b87e-f1fb7f8022c1}}) |
| **Marizomib** `[deneme]` | K5 | BSA (mg/m²) — ölçekli | [Marizomib doz notu]({{artifact:282e2834-585f-475b-88ff-d4822ca779d5}}) |

**50 kg için en kritik nokta:** Çoğu ilaç ya BSA'ya göre otomatik ölçeklenir (Temozolomid, Marizomib) ya da kiloya bağlı değildir (sabit doz veya deneme protokolü). **Tek gerçek kiloya-bağlı tavan hidroksiklorokindedir:** retinopati güvenliği için ≤5 mg/kg → 50 kg'da **≤250 mg/gün** (200 mg standart tablet uygun; 400 mg/gün AŞIRI, kullanılmamalı). Sabit-dozlu ilaçlarda 50 kg'da asıl dikkat, düşük vücut kütlesinde toksisitenin (regorafenib deri/KC, WEE1i+irinotekan/TMZ kemik iliği) daha belirgin olması → azaltılmış başlangıç + sık izlem.

## İzlemedeki olası adaylar (deneysel — kanıt olgunlaşınca yükseltilir)

Bu bölüm, sistematik taramalarda **mekanizması uygun ve beyne girdiği gösterilmiş** ama henüz **erişkin GBM klinik kanıtı olmayan** adayları listeler. Bunlar başlangıç kombinasyonuna (K3) dahil DEĞİLDİR; onkoloğun bilmesi için, kanıt olgunlaştığında (erişkin GBM in-vivo veya glioma Faz 1+ verisi) değerlendirilmek üzere izlenir.

| Aday | Hedef | Mekanizma | Beyne giriş | GBM kanıt durumu | Kısıtlar | Durum |
|------|-------|-----------|-------------|------------------|----------|-------|
| **6-thio-dG** `[deneme]` (ateganosine / THIO) | V1_TERT | Telomeraz-bağımlı substrat analoğu → telomer disfonksiyonu (gerçek TERT hedefi; hastanın **TERT promotör C250T** mutasyonuyla mekanistik uyumlu) | KBB geçişi gösterilmiş (ortotopik DIPG modeli, abstract düzeyi, DOI [10.1158/1535-7163.mct-17-0792](https://doi.org/10.1158/1535-7163.mct-17-0792)) | Pediatrik beyin tümörü in-vivo (DIPG/HGG/medulloblastom); **erişkin GBM verisi yok**. Klinik: THIO-101 Faz 2 (NSCLC) | Erişkin GBM'de spesifik veri bekliyor | İZLEMEDE — V1 için en güçlü aday |
| **Niasin (B3 vitamini)** `[takviye/repurpose]` (nikotinik asit, kontrollü-salınım) | V8_İMMÜN | Uykudaki miyeloid hücreleri (monosit/makrofaj/mikroglia) yeniden aktive eder → IFN-α14 ile tümör kök hücre büyümesini baskılar; dolaşan hafıza-T ve NK hücrelerini artırır | Oral; nikotinik asit KBB'yi geçer (niasinin bilinen CNS etkisi) | **En güçlü insan verisi bu tabloda:** Faz I-II yeni-tanı GBM (NCT04677049): MTD 2000 mg/gün, ara-analizde PFS-6 **%82 vs tarihsel %54** ([J Neurooncol 2025](https://doi.org/10.1007/s11060-025-05351-z)); immün kayması insan Faz I'de doğrulandı ([NXI 2026](https://doi.org/10.1212/NXI.0000000000200530)); preklinik köken + TMZ sinerjisi ([Sci Transl Med 2020](https://doi.org/10.1126/scitranslmed.aay9924)) | **① Simvastatin ile birlikte KULLANILAMAZ** — çalışma protokolü statini ≥2 hafta önce bıraktırıyor (ya niasin ya statin). **②** Kanıt **yeni-tanı** GBM'de; nüks/BNCT-sonrası veri yok. **③** Tek-kollu, OS kanıtı yok. **④** Flushing; DLT'ler trombositopeni+hiperbilirubinemi → bevacizumab ile trombosit/bilirubin izlemi | İZLEMEDE — V8 immün boşluğu için en somut aday |
| **Eribulin** | V2 (mitotik kol) | Mikrotübül/mitotik inhibitör → TP53-null (G2/M-bağımlı) hücrelerde mitotik katastrofi | Beyin dokusuna penetrasyon ölçülmüş (DOI [10.1111/cas.14067](https://doi.org/10.1111/cas.14067)) | İntraserebral GBM'de RT ile sağkalım artışı, in-vivo (DOI [10.1111/cas.13637](https://doi.org/10.1111/cas.13637)); **klinik GBM verisi yok** (meme/liposarkomda onaylı) | **QT uzatır → Lamide/lakozamid ile bazal+takip EKG şart**; miyelosupresyon örtüşmesi (TMZ/lomustin) | İZLEMEDE — WEE1i altında öncelik |

**Önemli:** Bu adaylar için karar hekimindir. 6-thio-dG ve eribulin, doğrudan V1/V2 deneme adaylarının (WEE1i, ATRi, paxalisib) **altında** öncelikli deneysel seçeneklerdir — birinci basamak değil, deneme yolu için ek düşünülebilir alternatiflerdir.

> **Niasin — erişim ve form (onkolog için not):** Çalışmada kullanılan **NiacinCRT™ çalışmaya özel bir ilaç değildir** — Designs for Health firmasının piyasada satılan bir gıda takviyesidir (500/750 mg tablet, nikotinik asit). Çalışmayı yapan ekibe erişim gerekmez. **Bilimsel olarak yeniden-üretilebilir spesifikasyon markanın kendisi değil, formudur:** *nikotinik asit (niacin), kontrollü/uzatılmış-salınımlı, günlük ~2000 mg, öğünle*. Bu spesifikasyona uyan eşdeğer ürünler vardır. **Kritik ayrım:** form mutlaka **nikotinik asit (niacin)** olmalı — **niacinamid / nikotinamid DEĞİL**; miyeloid-yeniden-aktivasyon ve flushing/lipid etkileri nikotinik aside özgüdür, nikotinamid bu etkiyi vermez. Türkiye'de belirli bir ürünün ruhsat/temin durumu eczane/onkolog tarafından doğrulanmalıdır; yüksek doz (2000 mg/gün) tıbbi gözetim ve karaciğer/trombosit izlemi gerektirir — takviye olsa da bu dozda 'serbest vitamin' gibi değerlendirilmemelidir. **Statin seçimi:** niasin denenecekse simvastatin bırakılır; ikisi birlikte verilmez.

---

## Değerlendirilip elenen adaylar (kanıt gerekçesiyle)

Aşağıdaki ajanlar değerlendirildi ve **stratejiye alınmadı**. Onkoloğun "neden bu ilaç yok?" sorusuna doğrudan yanıt olması için gerekçeleri kanıtıyla verilmiştir.

| Aday | Neden elendi | Kanıt |
|------|--------------|-------|
| **Valproik asit (valproat)** | TMZ-duyarlılaştırma etkisi **p53-bağımlıdır**; hasta **TP53 kayıp/çoklu-mutant** olduğundan p53–PUMA apoptoz yolağı aktive olmaz. Ayrıca en yüksek dereceli klinik kanıtta (1.869 hastalık havuz analizi) **sağkalım yararı doğrulanamadı**. Hasta zaten Keppra + Lamide ile nöbet kontrolünde; valproat üçüncü antiepileptik + bevacizumab ile kanama/hepatotoksisite örtüşmesi getirir. | [Han 2021, p53-PUMA](https://doi.org/10.3389/fonc.2021.722754) · [Happold 2016, havuz analizi](https://doi.org/10.1200/JCO.2015.63.6563) |
| **Melfalan** | GBM'de faz II'de **hiç aktivite yok** (nitrozüre-başarısızlığı sonrası); ayrıca alkilleyici olarak TMZ/lomustin ile aynı ekseni tekrarlar → yeni düğüm eklemez, yalnızca miyelosupresyon. Etkinliği farklı tümörlerde (miyelom, melanom, retinoblastom, medulloblastom). | [Am J Clin Oncol 1988, GBM faz II negatif](https://doi.org/10.1097/00000421-198802000-00011) |
| **Disülfiram (+ bakır)** | En yüksek dereceli kanıt **olumsuz**: randomize DIRECT çalışmasında rekürren GBM'de 6-aylık sağkalımı anlamlı artırmadı, ek toksisite getirdi. | [DIRECT randomize, 2023](https://doi.org/10.1001/jamanetworkopen.2023.4149) |
| **Dordaviprone (ONC201)** | Onaylı/güçlü kanıtlı yolu **H3K27M-mutant** gliomlara özgü; hasta **H3K27M-negatif** → uygun değil. | Hastanın genomik profili (H3K27M negatif) |

> **Valproat için nüans:** Valproat bir hastada *nöbet kontrolü* amacıyla zaten kullanılıyorsa, bunun sürdürülüp sürdürülmeyeceği nöroloğun/onkoloğun kararıdır — buradaki eleme yalnızca valproatı **antitümör (TMZ-duyarlılaştırıcı) beklentisiyle eklemenin** bu tümörde mekanistik/klinik dayanağının olmadığı yönündedir. Valproatın HDAC-inhibisyonu üzerinden p53'ten bağımsız bir radyoduyarlılaştırma sinyali preklinik olarak vardır; ancak bu, p53-kayıplı tümörde net klinik faydaya dönüşmemiştir.

---

## Önemli notlar — deneme çekirdeği, yedek plan ve erişim

Aşağıdaki üç not, yukarıdaki öncelik sıralaması ve kombinasyonların *çevresindeki* kararlar içindir.

### Not 1 — Deneme çekirdeği (paralel yürütülecek)
**Amaç:** yalnızca deneme ilaçlarının yapabildiği iki şeyi eklemek — **temiz p53-null sintetik-letal vuruş (V2)** ve **TERT/telomer ekseni (V1)** — Strateji 1'i durdurmadan.

| İlaç | Hedefler | Erişim yolu |
|------|----------|-------------|
| **Paxalisib** `[deneme]` (beyin-geçişli PI3K/mTOR) | V3 | GBM AGILE **[NCT03970447](https://clinicaltrials.gov/study/NCT03970447)** (rekürren kolu; Avrupa dahil 63 merkez) |
| **WEE1 inhibitörü** `[deneme]` (adavosertib / Debio 0123) | V2 (temiz sintetik letal) | Debio 0123 **[NCT05765812](https://clinicaltrials.gov/study/NCT05765812)** (IDH-yabanıl GBM; ABD/İspanya/İsviçre) |
| **ATR inhibitörü** (ceralasertib/berzosertib) | V2 + V1 | deneme / off-label — her iki truncal sürücüyü vurur |
| **6-thio-dG** `[deneme]` | V1 | yalnızca deneysel — bkz. "İzlemedeki olası adaylar" (TERT promotör mut. ile mekanistik uyumlu, en güçlü V1 adayı) |

Tam mekanizma, kanıt ve deneme uyumu **sintetik-letal çekirdek derin-inceleme** dosyasında. Deneme kayıt görüşmelerine tedavi eden onkologla **şimdi**, Strateji 1 ile paralel başlanmalıdır — deneme taraması haftalar sürer

---

### Not 2 — Yedek plan (deneme yolu tıkanır veya reddedilirse)
Deneme ilaçları elde edilemezse (kayıt kapalı, uygun değil, coğrafya, finansman), **bekleme**. Hedefli çekirdeği erişilebilir ilaçlarla yaklaşık olarak kur ve Strateji 1'i yoğunlaştır:

1. **PI3K/mTOR çıpasını değiştir:** paxalisib yerine **everolimus (off-label)** — daha zayıf (daha kötü kan-beyin bariyeri geçişi, geri-besleme AKT aktivasyonu) ama şimdi elde edilebilir. Metformin üstüne AMPK tarafından mTOR baskısı ekler.
2. **p53-null / DNA-hasar sinerjisini yaklaşık kur:** alkilleyiciyi (metronomik TMZ veya lomustin) repurposing omurgasıyla eşle; **valproik asit** ve **mebendazol** mitotik/kromatin stresi ekler. Bu gerçek bir WEE1/ATR sintetik-letal vuruşu değildir, ama V2 ekseni üzerindeki baskıyı sürdürür.
3. **Regorafenib ekle** — erişilebilir hedefli-kinaz çıpası olarak (en iyi erişilebilir-onkoloji kanıtı).
4. **Metabolik/otofaji katmanını en üst düzeyde tut** (metformin + statin + HCQ + itraconazol) — erişilebilir ilaçların gerçekten güçlü olduğu yer burasıdır.

**Yedek plan kapsamı:** hâlâ 8'de 7 (temiz V1 TERT vuruşu hariç her şey). Hedefli sintetik-letal mekanizmanın *kalitesi* kaybedilir, ancak **zaman kaybedilmez** ve **zayıflık genişliği kaybedilmez**.

---

## Zaman çizelgesi mantığı (üçü de eşzamanlı yürür)

```
Hafta 0 ──▶ STRATEJİ 1'e başla (hızlı omurga)        ── 7/8'i hemen kapsar
Hafta 0 ──▶ STRATEJİ 2 görüşmelerini aç (denemeler)  ── tarama paralel yürür
              │
              ├─ deneme erişimi verilir  ──▶ paxalisib + WEE1/ATR omurgaya eklenir
              └─ deneme yolu tıkanır     ──▶ Strateji 3 yedeğe geç (zaman kaybı yok)
```
Tasarımın amacı: **hiçbir haftada tümör, o an erişilebilir bir ilacın ulaşabileceği bir zayıflıkta baskısız bırakılmaz.**

---

## Onkoloğa götürülecekler

1. Bu döküman + kapsam matrisi + sintetik-letal derin-inceleme.
2. **Güvenlik/etkileşim** listesi (ana dossier §5): örtüşen hepatotoksisite (statin + valproat + itraconazol — itraconazol güçlü bir CYP3A4 inhibitörüdür ve geniş etkileşir), QT etkileri, miyelosupresyon, klorokin retinopatisi ve ilaç-ilaç etkileşimleri. Seçilen kesin kombinasyonun eczacı incelemesi önemlidir — özellikle itraconazol CYP3A4 etkileşimi birlikte verilen ilaçların düzeyini yükseltebilir.
3. İlk sorulacak iki deneme: **[NCT05765812](https://clinicaltrials.gov/study/NCT05765812)** (WEE1) ve **[NCT03970447](https://clinicaltrials.gov/study/NCT03970447)** (paxalisib).
4. **Mevcut antiepileptikler (Keppra + Lamide):** lakozamidin kardiyak iletim etkisi nedeniyle, QT-uzatan herhangi bir ilaç (hidroksiklorokin, itraconazol) eklenmeden önce **bazal + takip EKG** planlanmalı. Valproik asit üçüncü bir antiepileptik olacağından geri planda tutuldu — onkolog/nörolog birlikte değerlendirmeli. Levetirasetam (Keppra) farmakokinetik olarak "sessiz"dir (minimal etkileşim), bu bir avantajdır.

---

## Kaynakça — zayıflık bazında referanslar

Aşağıdaki referanslar, K3/K4/K5 tablolarındaki her ilaç–zayıflık eşleşmesinin dayandığı birincil literatürü zayıflık düğümü bazında listeler. Her bağlantı DOI üzerinden doğrudan makaleye gider; onkolog her iddiayı bağımsız doğrulayabilir.

**V1_TERT — telomeraz / telomer replikasyon stresi**
- 6-thio-dG (telomeraz-bağımlı telomer hasarı, pediatrik beyin tümörü in-vivo) — [Sengupta 2018](https://doi.org/10.1158/1535-7163.mct-17-0792)

**V2_TP53 — p53-null sintetik-letal (G2/M kontrol noktası)**
- Temozolomid — RT+TMZ, GBM standart (alkilleyici DNA hasarı) — [Stupp 2005](https://doi.org/10.1056/NEJMoa043330)
- WEE1 gatekeeper — GBM'de mitotik felaket — [Mir 2010](https://doi.org/10.1016/j.ccr.2010.08.011)
- Adavosertib (WEE1i) + radyasyon — [Mueller 2022](https://doi.org/10.1093/noajnl/vdac073)

**V3_PTEN/PI3K — PI3K/mTOR yolu**
- Metformin — AMPK üzerinden glioma kök hücre — [Sato 2012](https://doi.org/10.5966/sctm.2012-0058)
- Metformin — GBM büyüme inhibisyonu — [Sesen 2015](https://doi.org/10.1371/journal.pone.0123721)
- Paxalisib — beyin-geçişli PI3K/mTOR inhibitörü, GBM faz-2 — [Wen 2022](https://doi.org/10.1200/jco.2022.40.16_suppl.2047)
- Regorafenib — multikinaz, REGOMA randomize — [Lombardi 2019 (REGOMA)](https://doi.org/10.1016/s1470-2045(18)30675-2)

**V4_NFKB — NF-κB / proteazom**
- Hidroksiklorokin — otofaji/lizozom, faz I/II GBM+RT — [Rosenfeld 2014](https://doi.org/10.4161/auto.28984)
- Marizomib — beyin-geçen proteazom inhibitörü (NF-κB dolaylı) — [Potts 2011](https://doi.org/10.2174/156800911794519716)

**V5_MGMT — alkilleyici DNA hasarı**
- Temozolomid — RT ile eşzamanlı, GBM standart tedavi (alkilleyici) — [Stupp 2005](https://doi.org/10.1056/NEJMoa043330)

**V7_METABOLIC — mevalonat / OXPHOS / otofaji / anti-anjiyogenez**
- Bevacizumab — anti-VEGF, rekürren GBM — [Friedman 2009](https://doi.org/10.1200/jco.2008.19.8721)
- Metformin — kompleks-I/OXPHOS (GBM) — [Sesen 2015](https://doi.org/10.1371/journal.pone.0123721)
- Simvastatin — mevalonat kaskadı→intrinsik apoptoz — [Alizadeh 2017](https://doi.org/10.1038/srep44841)
- Statin repurpose (derleme) — [Jiang 2021](https://doi.org/10.1186/s13046-021-02041-2)
- Hidroksiklorokin — otofaji inhibisyonu — [Rosenfeld 2014](https://doi.org/10.4161/auto.28984)

**V8_IMMUNE — anti-anjiyogenez / mikroçevre**
- Bevacizumab — VEGF/anti-anjiyogenez — [Friedman 2009](https://doi.org/10.1200/jco.2008.19.8721)
- Regorafenib — anti-anjiyogenez, REGOMA — [Lombardi 2019 (REGOMA)](https://doi.org/10.1016/s1470-2045(18)30675-2)

**Makale-dışı / veritabanı kaynakları ve notlar**
- **V6_WNT/TCF7L2:** Bu düğüm için beyin-geçişli, klinik-aşama güçlü bir Wnt/GSK3 ilacı literatürde bulunamadı; *kabul edilen boşluk* olarak bırakıldı. Celecoxib yalnızca dolaylı/zayıf COX–Wnt etkisiyle listelenir, birincil GBM Wnt kanıtı yoktur.
- **Marizomib pano skoru (86.7):** `PANO_INCELEME_kanit_ve_hucre_ici_duzey.md` çapraz-analizinden gelen bir iç-sıralama değeridir (kanıt düzeyi + beyin-konsantrasyonu birleşik skoru); birincil mekanizma kaynağı yukarıdaki Potts 2011'dir.
- **6-thio-dG:** Beyin in-vivo verisi pediatrik (DIPG/HGG/medulloblastom) modellerdendir; erişkin-GBM'e özgü klinik veri yoktur (izlemedeki aday).
- **Genomik zayıflık atamaları (V1–V8):** hastanın 2026-05-21 genomik profilleme raporundan türetilmiştir (birincil klinik belge).
