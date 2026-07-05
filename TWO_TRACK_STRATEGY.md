# İki-Yollu Tedavi Stratejisi — Rekürren GBM (IDH-yabanıl tip, RTK1)
## Hızlı başla, denemeleri paralel yürüt, zaman kaybetme

**Temel ilke:** tümörü hedeflemeye başlamak için deneme ilaçlarını bekleme. Hızlı, erişilebilir ilaçlarla *şimdi* mümkün olduğunca çok zayıflığı kapsa; deneme-kapılı hedefli ilaçları *paralel* olarak takip et; ve deneme yolu tıkanır ya da reddedilirse tümörün her cepheden baskı altında kalmasını sağlayan bir yedek planı hazır tut.

![Erişim hızına göre kapsam — güncel ilaçlar]({{artifact:4144a4d4-dc30-45bb-8c0f-66bf59115a16}})

**Kapsam haritasından ana bulgu:** hızlı yollar (repurposing + erişilebilir onkoloji) birlikte **8 zayıflığın 7'sini hemen** hedefleyebiliyor. Yalnızca **TERT/telomer ekseni (V1)** ve **temiz p53-null sintetik-letal vuruş (V2)** gerçekten deneme ilaçlarına ihtiyaç duyuyor.

---

## Hedef referansı — tümörün zayıflıkları (V1–V8)

Aşağıdaki stratejilerdeki her ilaç, bunlardan bir veya birkaçını vurmak için seçildi. Doğrudan 2026-05-21 genomik profilleme özetinden türetildi (tam detay `DOSSIER.md` içinde).

| # | Değişiklik (raporunuzdan) | Klonalite | Ne yapıyor | Hedeflenebilir düğüm |
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

> **Neden basamaklı ekleme?** Her ilaç ayrı bir toksisite ekler; hepsini aynı gün başlatmak, bir yan etki çıkarsa hangi ilacın sorumlu olduğunu gizler. Tek tek ekleyerek her ilacın tolere edildiği doğrulanır, sonra bir sonrakine geçilir.

**Zemin (hasta zaten kullanıyor):** Altuzan (bevacizumab, V7/V8) + Keppra + Lamide.

| Sıra | İlaç | Açtığı zayıflık | Neden bu sırada | Basamak |
|------|------|------------------|------------------|---------|
| **1** | **Temozolomid** (veya Lomustin) | V5 + V2 (DNA-hasar zemini) | Omurga alkilleyici; diğer her şeyin üzerine eklendiği DNA-hasar kaynağı. Standart, tanıdık toksisite | ↓ |
| **2** | **Metformin** | V3 + V7 (OXPHOS) | En düşük toksisite, **QT-nötr** (Lamide ile tam uyumlu), güçlü metabolik duyarlılaştırma | ↓ |
| **3** | **Simvastatin** | V7 (mevalonat — farklı düğüm) | Yine düşük toksisite, QT-nötr; metforminden **ayrı** bir metabolik düğümü vurur | **← en güvenli çekirdek (ilk 3 ilaç; tamamen QT-nötr, Lamide ile uyumlu)** |
| **4** | **Hidroksiklorokin** | **V4 (NF-κB)** + V7 otofaji | Yeni bir zayıflık (V4) açar — ama **QT uzatır** → Lamide nedeniyle bazal + takip **EKG** ve yıllık **göz muayenesi** şart | **← +V4 basamağı (buradan itibaren EKG + göz takibi başlar)** |
| **5** | **Regorafenib** | V3 + V8 (multikinaz) | En güçlü erişilebilir-onkoloji kanıtı (REGOMA randomize) — ama **en yüksek toksisite**: karaciğer (kara kutu) + Altuzan ile hipertansiyon istifi | **← burası tam K3** |

**Okuma:** İlk **3 ilaç** (Temozolomid + Metformin + Simvastatin) güvenli, QT-nötr çekirdektir. Tolere edilince **Hidroksiklorokin** eklenir (V4 kapsamı açılır) — buradan itibaren EKG + göz takibi gerekir. En son, en güçlü ama en toksik ilaç **Regorafenib** eklenir; bu noktada aşağıdaki **K3** kombinasyonuna ulaşılır. Yani başlangıç, tek bir kademeli titrasyon yoludur.

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

![Minimum-toksisite kombinasyonları — kapsam vs toksisite]({{artifact:3de7ee78-e5be-4423-bada-0caef952a5a6}})


### K3 — Geniş hızlı omurga ⭐ BAŞLANGIÇ KOMBİNASYONU
**Kapsam:** 6/8 zayıflık (V2, V3, V4, V5, V7, V8) · Yukarıdaki öncelik sıralamasının **tam hâli** (5 ilaç eklendiğinde ulaşılan nokta). Deneme gerektirmez — hepsi hızlı/erişilebilir. Toksisite en yüksek olduğu için yukarıdaki gibi **basamaklı** ulaşılır, tek seferde değil.

| İlaç | Hangi zayıflığı/düğümü vuruyor | Yarattığı toksisite |
|------|-------------------------------|---------------------|
| _Mevcut ilaçlar (zaten kullanılıyor):_ | | |
| **Altuzan (bevacizumab)** | V7 + V8 — VEGF/anti-anjiyogenez düğümü (damar normalizasyonu, ödem/steroid azaltıcı) | Hipertansiyon, GİS perforasyon/kanama, yara iyileşme gecikmesi (ameliyat öncesi ≥28 gün kesilir), proteinüri |
| **Keppra (levetirasetam)** | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | Davranışsal/psikiyatrik etkiler, uyku hâli. Farmakokinetik olarak SESSİZ — diğer ilaçlarla minimal etkileşim (avantaj) |
| **Lamide (lakozamid)** | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | **Kardiyak iletim (PR/QT) etkisi** — QT-uzatan ilaç eklenirse EKG şart; baş dönmesi/ataksi |
| _Bu kombinasyonda eklenenler:_ | | |
| **Temozolomid** | V5 (MGMT/alkilleyici DNA-hasarı) + V2 (p53 — DNA hasar yükü) | Kemik iliği baskılanması (ana doz-kısıtlayıcı), bulantı, nadiren karaciğer toksisitesi |
| **Metformin** | V3 (PI3K/mTOR — AMPK üzerinden dolaylı) + V7 (OXPHOS/kompleks-I) | Laktik asidoz (kara kutu, böbrek yetmezliğinde), B12 eksikliği, GİS. Düşük genel toksisite |
| **Simvastatin** _(atorvastatin yerine)_ | V7 (mevalonat/kolesterol düğümü) | Miyopati/rabdomiyoliz (nadir), karaciğer enzim artışı, hafif hiperglisemi. **Beyin geçişi atorvastatinden daha iyi** (pano: ölçülmüş-iyi); ⚠ CYP3A4 substratı — itraconazol ile kontrendike (zaten kullanılmıyor) |
| **Hidroksiklorokin** | V4 (NF-κB) + V7 (otofaji/lizozom düğümü — hayatta-kalma kaçışını kapatır) | **QT uzaması** (Lamide ile EKG şart), **geri dönüşsüz retinopati** (yıllık göz muayenesi), kardiyomiyopati |
| **Regorafenib** | V3 (multikinaz) + V8 (anti-anjiyogenez) — REGOMA randomize kanıtı | **Hepatotoksisite (kara kutu)**, hipertansiyon (Altuzan ile istiflenir), el-ayak sendromu, GİS |

**Bu kombinasyonun toksisite tablosu:** dört ilaçlık hızlı çekirdeğe (Temozolomid + Metformin + Simvastatin + Hidroksiklorokin) **Regorafenib** eklenir (V3 multikinaz, REGOMA randomize kanıtı). **İki yeni risk istiflenir:** (1) **karaciğer** — Regorafenib kara kutu hepatotoksisite + simvastatin → karaciğer testleri sık; (2) **hipertansiyon** — Regorafenib + mevcut **Altuzan (bevacizumab)** kan basıncını üst üste bindirir. Hidroksiklorokin QT'si + Lamide nedeniyle **EKG** yine şart. Zayıflık kapsamı Regorafenibsiz hâle göre artmaz — ek fayda multikinaz gücünde, ek maliyet toksisitede.

### K4 — Deneme eklenmiş (sintetik-letal çekirdek)
**Kapsam:** 6/8 zayıflık (V2, V3, V4, V5, V7, V8) + V2'ye TEMİZ vuruş · **Toplam toksisite skoru:** 27 · Deneme ilaçları erişilebilirse en güçlü V2 hedeflemesi.

| İlaç | Hangi zayıflığı/düğümü vuruyor | Yarattığı toksisite |
|------|-------------------------------|---------------------|
| _Mevcut ilaçlar (zaten kullanılıyor):_ | | |
| **Altuzan (bevacizumab)** | V7 + V8 — VEGF/anti-anjiyogenez düğümü (damar normalizasyonu, ödem/steroid azaltıcı) | Hipertansiyon, GİS perforasyon/kanama, yara iyileşme gecikmesi (ameliyat öncesi ≥28 gün kesilir), proteinüri |
| **Keppra (levetirasetam)** | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | Davranışsal/psikiyatrik etkiler, uyku hâli. Farmakokinetik olarak SESSİZ — diğer ilaçlarla minimal etkileşim (avantaj) |
| **Lamide (lakozamid)** | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | **Kardiyak iletim (PR/QT) etkisi** — QT-uzatan ilaç eklenirse EKG şart; baş dönmesi/ataksi |
| _Bu kombinasyonda eklenenler:_ | | |
| **Metformin** | V3 (PI3K/mTOR — AMPK üzerinden dolaylı) + V7 (OXPHOS/kompleks-I) | Laktik asidoz (kara kutu, böbrek yetmezliğinde), B12 eksikliği, GİS. Düşük genel toksisite |
| **Simvastatin** _(atorvastatin yerine)_ | V7 (mevalonat/kolesterol düğümü) | Miyopati/rabdomiyoliz (nadir), karaciğer enzim artışı, hafif hiperglisemi. **Beyin geçişi atorvastatinden daha iyi** (pano: ölçülmüş-iyi); ⚠ CYP3A4 substratı — itraconazol ile kontrendike (zaten kullanılmıyor) |
| **Hidroksiklorokin** | V4 (NF-κB) + V7 (otofaji/lizozom düğümü — hayatta-kalma kaçışını kapatır) | **QT uzaması** (Lamide ile EKG şart), **geri dönüşsüz retinopati** (yıllık göz muayenesi), kardiyomiyopati |
| **Temozolomid** | V5 (MGMT/alkilleyici DNA-hasarı) + V2 (p53 — DNA hasar yükü) | Kemik iliği baskılanması (ana doz-kısıtlayıcı), bulantı, nadiren karaciğer toksisitesi |
| **Paxalisib** | V3 (PI3K/mTOR — beyin-geçişli, DİREKT) — deneme ilacı | Hiperglisemi (sınıf etkisi — Metformin ile kısmen dengelenir), mukozit, ruh hâli değişikliği |
| **WEE1 inhibitörü** | V2 (p53-null sintetik-letal — G2/M kontrol noktası) — deneme ilacı | **Kemik iliği baskılanması** (alkilleyici ile doz-kısıtlayıcı çakışma → sık kan sayımı), bulantı, yorgunluk |

**Bu kombinasyonun toksisite tablosu:** hızlı çekirdek zeminine (Temozolomid + Metformin + Simvastatin + Hidroksiklorokin) **Paxalisib + WEE1 inhibitörü** (deneme) eklenir. **Ana risk — kemik iliği:** Temozolomid (alkilleyici) + WEE1 inhibitörü aynı ekseni vurur → **doz-kısıtlayıcı miyelosupresyon**, sık tam kan sayımı ve aralıklı doz şart (bkz. TOXICITY_PROFILE Bölüm C). Paxalisib hiperglisemisi **Metformin** ile kısmen dengelenir (olumlu örtüşme). Hidroksiklorokin QT'si + **Lamide** → EKG şartı burada da geçerli. Sadece deneme erişimi sağlanırsa.

### K5 — Kanıt + beyin-konsantrasyonu optimize (PANO İNCELEMESİYLE GÜÇLENDİRİLMİŞ)
**Kapsam:** 6/8 zayıflık (V2, V3, V4, V5, V7, V8) + V2'ye TEMİZ vuruş · **V4 artık GÜÇLÜ ilaçla** (dolaylı HCQ değil) · Deneme/yurtdışı erişim gerekli.

> **Fark:** `PANO_INCELEME_kanit_ve_hucre_ici_duzey.md` çapraz-analizinde hem kanıt hem
> beyin-konsantrasyonu (hücre-içi yeterli düzey) kriterini geçen adaylarla kurulmuştur. İki
> kritik iyileştirme: (1) **V4/NF-κB'yi HCQ'nun *dolaylı* etkisi yerine Marizomib** (beyin-geçen
> proteazom inhibitörü, GBM insan çalışması) ile *doğrudan* hedefler; (2) **statin simvastatin**
> (beyin geçişi daha iyi). Marizomib **miyelosupresyon EKLEMEZ**, bu yüzden K4 kombinasyonundaki kemik
> iliği darboğazını büyütmez.

| İlaç | Hangi zayıflığı/düğümü vuruyor | Yarattığı toksisite |
|------|-------------------------------|---------------------|
| _Mevcut ilaçlar (zaten kullanılıyor):_ | | |
| **Altuzan (bevacizumab)** | V7 + V8 — VEGF/anti-anjiyogenez düğümü (damar normalizasyonu, ödem/steroid azaltıcı) | Hipertansiyon, GİS perforasyon/kanama, yara iyileşme gecikmesi (ameliyat öncesi ≥28 gün kesilir), proteinüri |
| **Keppra (levetirasetam)** | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | Davranışsal/psikiyatrik etkiler, uyku hâli. Farmakokinetik olarak SESSİZ — diğer ilaçlarla minimal etkileşim (avantaj) |
| **Lamide (lakozamid)** | Antiepileptik (nöbet kontrolü — tümör hedefi değil) | **Kardiyak iletim (PR/QT) etkisi** — QT-uzatan ilaç eklenirse EKG şart; baş dönmesi/ataksi |
| _Bu kombinasyonda eklenenler:_ | | |
| **Temozolomid** | V5 (MGMT/alkilleyici DNA-hasarı) + V2 (p53 — DNA hasar yükü) | Kemik iliği baskılanması (ana doz-kısıtlayıcı), bulantı, nadiren karaciğer toksisitesi |
| **Metformin** | V3 (PI3K/mTOR — AMPK üzerinden) + V7 (OXPHOS/kompleks-I) | Laktik asidoz (kara kutu, böbrek yetmezliğinde), B12 eksikliği, GİS. Düşük genel toksisite |
| **Simvastatin** _(atorvastatin yerine)_ | V7 (mevalonat/kolesterol düğümü) | Miyopati/rabdomiyoliz, karaciğer enzim artışı. **Beyin geçişi atorvastatinden daha iyi**; ⚠ CYP3A4 substratı |
| **Marizomib** _(deneme/yurtdışı)_ | **V4 (NF-κB) — DOĞRUDAN, beyin-geçen proteazom inhibitörü** (pano skor 86.7, insan çalışması) | **CNS etkileri** (ataksi, konfüzyon, yorgunluk) — ⚠ Keppra+Lamide üzerine binebilir, nörolojik izlem; periferik nöropati bortezomibden az |
| **Paxalisib** _(deneme)_ | V3 (PI3K/mTOR — beyin-geçişli, DİREKT) | Hiperglisemi (Metformin ile dengelenir), mukozit, ruh hâli |
| **WEE1 inhibitörü** _(deneme)_ | V2 (p53-null sintetik-letal — G2/M kontrol noktası) | **Kemik iliği baskılanması** (Temozolomid ile doz-kısıtlayıcı çakışma → sık kan sayımı) |

> **❌ Dordaviprone (ONC201) DIŞLANDI:** Hastanın **H3K27M testi NEGATİF** olduğu doğrulandı.
> ONC201'in onaylı/güçlü kanıtlı yolu H3K27M-mutant gliomlara özgüdür; bu hasta için uygun
> değildir ve bu kombinasyona dahil edilmemiştir. (İlgili panodaki yüksek skor yalnızca H3K27M-pozitif popülasyona aitti.)

**Bu kombinasyonun toksisite tablosu:** deneme çekirdekli K4 kombinasyonuna kıyasla iki iyileştirme — V4 artık *dolaylı HCQ* değil
*doğrudan Marizomib* ile vuruluyor (HCQ çıkarılırsa **QT/retinopati yükü de düşer**), ve statin
beyin-geçişli simvastatine çevrildi. **Ana risk yine kemik iliği** (Temozolomid + WEE1) → sık tam
kan sayımı; ancak Marizomib bu ekseni BÜYÜTMEZ. **Yeni izlem ekseni: CNS** —
Marizomib'in ataksi/konfüzyonu mevcut iki AEİ (Keppra+Lamide) üzerine binebilir. (Dordaviprone/
ONC201, hastanın **H3K27M-negatif** olması nedeniyle bu kombinasyondan çıkarıldı.) Erişim:
Marizomib/paxalisib/WEE1i deneme veya yurtdışı; simvastatin+metformin+temozolomid hızlı/ulaşılabilir.

**Özet:** V1 (TERT) ve V6 (Wnt) hızlı ilaçlarla kapanamaz (V1 sadece deneme — ATR-i / 6-thio-dG; V6 doğrudan güçlü ilaç yok, celecoxib sadece dolaylı). Diğer 6 zayıflık, mevcut üç ilaca **minimum ek toksisiteyle** hedeflenebilir. **En güvenli başlangıç, ilk üç ilaçlık QT-nötr çekirdektir** (Temozolomid + Metformin + Simvastatin; Lamide ile tam uyumlu). **Hidroksiklorokin eklendiğinde** V4 de kapsanır ve en iyi kapsam/toksisite dengesine ulaşılır (EKG + göz muayenesi şartıyla) — bu, tam **K3** kombinasyonuna giden yoldur. **K5, deneme/yurtdışı erişim sağlanırsa en güçlü kanıt-temelli seçenektir** — V4'ü doğrudan Marizomib ile vurur ve statin simvastatine çevrilir (pano incelemesi).

*Not: itraconazol bu kombinasyonların hiçbirinde yok — açtığı her düğüm zaten başka ilaçça kapsanıyor ve en ağır CYP3A4 + QT yükünü getiriyor (Lamide/lakozamid varken özellikle riskli).*

---

## İzlemedeki olası adaylar (deneysel — kanıt olgunlaşınca yükseltilir)

Bu bölüm, sistematik taramalarda **mekanizması uygun ve beyne girdiği gösterilmiş** ama henüz **erişkin GBM klinik kanıtı olmayan** adayları listeler. Bunlar başlangıç kombinasyonuna (K3) dahil DEĞİLDİR; onkoloğun bilmesi için, kanıt olgunlaştığında (erişkin GBM in-vivo veya glioma Faz 1+ verisi) değerlendirilmek üzere izlenir.

| Aday | Hedef | Mekanizma | Beyne giriş | GBM kanıt durumu | Kısıtlar | Durum |
|------|-------|-----------|-------------|------------------|----------|-------|
| **6-thio-dG** (ateganosine / THIO) | V1_TERT | Telomeraz-bağımlı substrat analoğu → telomer disfonksiyonu (gerçek TERT hedefi; hastanın **TERT promotör C250T** mutasyonuyla mekanistik uyumlu) | KBB geçişi gösterilmiş (ortotopik DIPG modeli, abstract düzeyi, DOI 10.1158/1535-7163.mct-17-0792) | Pediatrik beyin tümörü in-vivo (DIPG/HGG/medulloblastom); **erişkin GBM verisi yok**. Klinik: THIO-101 Faz 2 (NSCLC) | Erişkin GBM'de spesifik veri bekliyor | İZLEMEDE — V1 için en güçlü aday |
| **Eribulin** | V2 (mitotik kol) | Mikrotübül/mitotik inhibitör → TP53-null (G2/M-bağımlı) hücrelerde mitotik katastrofi | Beyin dokusuna penetrasyon ölçülmüş (DOI 10.1111/cas.14067) | İntraserebral GBM'de RT ile sağkalım artışı, in-vivo (DOI 10.1111/cas.13637); **klinik GBM verisi yok** (meme/liposarkomda onaylı) | **QT uzatır → Lamide/lakozamid ile bazal+takip EKG şart**; miyelosupresyon örtüşmesi (TMZ/lomustin) | İZLEMEDE — WEE1i altında öncelik |

**Önemli:** Bu adaylar için karar hekimindir. 6-thio-dG ve eribulin, doğrudan V1/V2 deneme adaylarının (WEE1i, ATRi, paxalisib) **altında** öncelikli deneysel seçeneklerdir — birinci basamak değil, deneme yolu için ek düşünülebilir alternatiflerdir.

---

## Önemli notlar — deneme çekirdeği, yedek plan ve erişim

Aşağıdaki üç not, yukarıdaki öncelik sıralaması ve kombinasyonların *çevresindeki* kararlar içindir.

### Not 1 — Deneme çekirdeği (paralel yürütülecek)
**Amaç:** yalnızca deneme ilaçlarının yapabildiği iki şeyi eklemek — **temiz p53-null sintetik-letal vuruş (V2)** ve **TERT/telomer ekseni (V1)** — Strateji 1'i durdurmadan.

| İlaç | Hedefler | Erişim yolu |
|------|----------|-------------|
| **Paxalisib** (beyin-geçişli PI3K/mTOR) | V3 | GBM AGILE **NCT03970447** (rekürren kolu; Avrupa dahil 63 merkez) |
| **WEE1 inhibitörü** (adavosertib / Debio 0123) | V2 (temiz sintetik letal) | Debio 0123 **NCT05765812** (IDH-yabanıl GBM; ABD/İspanya/İsviçre) |
| **ATR inhibitörü** (ceralasertib/berzosertib) | V2 + V1 | deneme / off-label — her iki truncal sürücüyü vurur |
| **6-thio-dG** | V1 | yalnızca deneysel — bkz. "İzlemedeki olası adaylar" (TERT promotör mut. ile mekanistik uyumlu, en güçlü V1 adayı) |

Tam mekanizma, kanıt ve deneme uyumu **sintetik-letal çekirdek derin-inceleme** dosyasında. Deneme kayıt görüşmelerine onkoloğunuzla **şimdi**, Strateji 1 ile paralel başlayın — deneme taraması haftalar sürer ve Strateji 1 bu süre boyunca sizi kapsar.

---

### Not 2 — Yedek plan (deneme yolu tıkanır veya reddedilirse)
Deneme ilaçları elde edilemezse (kayıt kapalı, uygun değil, coğrafya, finansman), **bekleme**. Hedefli çekirdeği erişilebilir ilaçlarla yaklaşık olarak kur ve Strateji 1'i yoğunlaştır:

1. **PI3K/mTOR çıpasını değiştir:** paxalisib yerine **everolimus (off-label)** — daha zayıf (daha kötü kan-beyin bariyeri geçişi, geri-besleme AKT aktivasyonu) ama şimdi elde edilebilir. Metformin üstüne AMPK tarafından mTOR baskısı ekler.
2. **p53-null / DNA-hasar sinerjisini yaklaşık kur:** alkilleyiciyi (metronomik TMZ veya lomustin) repurposing omurgasıyla eşle; **valproik asit** ve **mebendazol** mitotik/kromatin stresi ekler. Bu gerçek bir WEE1/ATR sintetik-letal vuruşu değildir, ama V2 ekseni üzerindeki baskıyı sürdürür.
3. **Regorafenib ekle** — erişilebilir hedefli-kinaz çıpası olarak (en iyi erişilebilir-onkoloji kanıtı).
4. **Metabolik/otofaji katmanını en üst düzeyde tut** (metformin + statin + HCQ + itraconazol) — erişilebilir ilaçların gerçekten güçlü olduğu yer burasıdır.

**Yedek plan kapsamı:** hâlâ 8'de 7 (temiz V1 TERT vuruşu hariç her şey). Hedefli sintetik-letal mekanizmanın *kalitesini* kaybedersiniz, ama **zaman kaybetmezsiniz** ve **zayıflık genişliği kaybetmezsiniz**.

---

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
3. İlk sorulacak iki deneme: **NCT05765812** (WEE1) ve **NCT03970447** (paxalisib).
4. **Mevcut antiepileptikler (Keppra + Lamide):** lakozamidin kardiyak iletim etkisi nedeniyle, QT-uzatan herhangi bir ilaç (hidroksiklorokin, itraconazol) eklenmeden önce **bazal + takip EKG** planlanmalı. Valproik asit üçüncü bir antiepileptik olacağından geri planda tutuldu — onkolog/nörolog birlikte değerlendirmeli. Levetirasetam (Keppra) farmakokinetik olarak "sessiz"dir (minimal etkileşim), bu bir avantajdır.
