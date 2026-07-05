# İlaçlarda Doz Hesabı — Yöntem ve Mantık

*Kapsam: `dose_estimates/` klasöründeki tüm ilaçlar — hem repurposing ilaçlar (doz-boşluk
analizi) hem klinik dozu tanımlı onkoloji/deneme/destek ilaçları (doz/rol notu). Ayrım
aşağıda "İki dosya tipi" bölümünde.*

## Neden "kan-beyin bariyerini geçiyor" yeterli değil

Bir ilacın etkili olması için üç eşiğin de aşılması gerekir:

1. **Kan-beyin bariyerini geçmek** (BBB penetrasyonu) — gerekli ama yeterli değil.
2. **Tümör hücresinde serbest (bağlanmamış) konsantrasyonun**, o ilacın hücreyi
   etkilediği **in-vitro etkili konsantrasyona (IC50/EC50)** ulaşması.
3. Bu düzeyin **tolere edilebilir bir sistemik dozla** sağlanabilmesi.

Repurposing ilaçların çoğunda kırılan halka **2. eşiktir**: laboratuvarda etkili olduğu
konsantrasyon, hastada güvenle ulaşılabilen beyin konsantrasyonunun çok üstündedir.

## Hesabın adımları

Her ilaç için şu zinciri kuruyoruz (literatürden gerçek sayılarla):

```
(1) In-vitro etkili konsantrasyon (glioma hücrelerinde IC50/EC50)      [µM]
(2) Standart klinik dozda plazma Cmax                                   [µM]
(3) Protein bağlanma → SERBEST plazma konsantrasyonu = Cmax × (1-PB)    [µM]
    (yalnızca serbest ilaç zara geçer ve etki eder)
(4) Beyin geçiş oranı (Kp,uu veya beyin:plazma veya BOS:plazma)
(5) Tahmini tümör SERBEST konsantrasyonu = (3) × (4)                    [µM]
(6) BOŞLUK ORANI = (5) ÷ (1)
       ≥ ~0.3  → etkili düzeye yaklaşır (gerçekçi)
       « 1     → in-vitro sitotoksik düzeye ulaşılamaz
                 (ilaç yalnızca DÜŞÜK-doz / sinerjik / modülatör rolde anlamlı)
```

## İki dosya tipi: hangi ilaca hangi analiz uygulanır?

Klasördeki (`dose_estimates/`) dosyalar iki tiptedir — çünkü tüm ilaçlara aynı "boşluk"
hesabı uygulanamaz:

- **A) Doz-boşluk analizi** — *repurposing ilaçlar* için. Bu ilaçların GBM'de onaylı bir
  "etkili doz"u yoktur; bu yüzden yukarıdaki 6-adımlı zincirle in-vitro etkili konsantrasyon
  ile tümörde ulaşılabilir konsantrasyonu karşılaştırırız. (Mebendazol, HCQ, valproik asit,
  metformin, simvastatin, atorvastatin, celecoxib, itraconazol.)

- **B) Doz/rol notu** — *onaylı onkoloji, deneme veya destek ilaçları* için. Bunların
  **klinik etkinlik dozu tanımlıdır** (faz çalışmalarında/etikette), yani "hücre-içi yeterli
  düzey" sorusu zaten klinik dozla yanıtlanmıştır. Bu ilaçlarda boşluk hesabı yerine
  **klinik doz + beyin geçişi + rol** çerçevesi kullanılır. (Temozolomid, regorafenib,
  paxalisib, adavosertib/WEE1i, marizomib, dordaviprone/ONC201, bevacizumab ve iki
  antiepileptik Keppra/Lamide.)

> **Özel durum — hedefi tümör hücresi içi olmayan ilaçlar:** Bevacizumab (Altuzan) BBB'yi
> geçmez ve etkisi damar/mikroçevre üzerindendir; bu ilaçta "hücre-içi düzey" kriteri
> **uygulanmaz** (hedefi dolaşımdaki VEGF). Antiepileptikler (Keppra, Lamide) tümör hedefi
> değildir; yalnızca destek tedavi ve etkileşim (Lamide → QT/EKG) açısından listelenir.

Klasördeki tüm dosyaların dizini: `INDEX.md`.

## Kritik ilke: "sitotoksik doz" ≠ "faydasız"

Boşluk oranı düşük olan bir ilaç **işe yaramaz demek değildir** — doğrudan tek-başına
tümör öldürücü doza ulaşamaz demektir. Birçok repurposing ilacın GBM'deki mantığı
sitotoksisite değil, **düşük konsantrasyonda bile işleyen modülatör etkilerdir**:

- **Metformin:** AMPK→mTOR baskısı, OXPHOS kısıtı (metabolik duyarlılaştırma)
- **Atorvastatin:** mevalonat/kolesterol kısıtı, anti-inflamatuar
- **Celecoxib:** COX-2/PGE2 baskısı (mikroçevre modülasyonu — nM düzeyde sağlanır)

Bu ilaçların değeri **kombinasyon içindeki sinerji** ve **yolak baskısıdır**, tek-başına
sitotoksisite değil. Boşluk analizi, hangi ilaçtan ne beklemek gerektiğini netleştirir.

## Belirsizlik ve sınırlar

- Sayılar **literatür-tipik aralıklardır**; hasta-özel farmakokinetik (böbrek/karaciğer
  fonksiyonu, ilaç etkileşimleri, P-gp aktivitesi) bunları kaydırabilir.
- **Tümör dokusu ≠ sağlıklı beyin:** GBM'de BBB kısmen bozuktur (kontrast tutulumu),
  bu bazı ilaçların tümör konsantrasyonunu artırabilir — ama heterojen ve öngörülemez.
- Terapötik ilaç izlemi (TDM) mümkün olan ilaçlarda (valproik asit) gerçek plazma düzeyi
  ölçülebilir; çoğunda ölçülemez, tahmine dayanır.
- Bu belge **doz hesabının bilimsel iskeletidir**; kesin doz, hasta durumu ve
  etkileşimler onkolog/klinik farmakolog tarafından belirlenir.

## A tipi — repurposing ilaç boşluk özeti

| İlaç | In-vitro etkili | Tümör ulaşılabilir (tahmini) | Boşluk | Rol |
|------|-----------------|------------------------------|--------|-----|
| Mebendazol | ~0.3 µM | ölçülebilir beyin düzeyi | **DAR** ✓ | En gerçekçi doğrudan etki |
| Hidroksiklorokin | ~15 µM | lizozomal birikimle yaklaşır | **SINIRDA** | Otofaji blokajı (değişken) |
| Valproik asit | ~1000 µM (HDAC) | ~15–70 µM serbest beyin | orta | Kısmi epigenetik + radyoduyarlılaştırma |
| Simvastatin | ~5 µM | <0.05 µM serbest (atorvastatinden yüksek) | geniş | Mevalonat kısıtı; **beyin geçişi atorvastatinden iyi** → tercih |
| İtraconazol | ~3 µM | <0.05 µM (P-gp atar) | geniş | Zayıf beyin geçişi + CYP3A4 yükü → çıkarıldı |
| Celecoxib | ~30 µM (apoptoz) | <0.1 µM | geniş | COX-2 baskısı (nM) yeterli; sitotoksik değil |
| Metformin | ~5000 µM | ~5–8 µM | çok geniş | Metabolik duyarlılaştırıcı (sinerji) |
| Atorvastatin | ~5 µM | <0.01 µM serbest | geniş | ⚠ Zayıf beyin geçişi → **simvastatine kaydırıldı** |

## B tipi — klinik dozu tanımlı ilaçlar (boşluk hesabı uygulanmaz)

| İlaç | Beyin geçişi | Erişim | Rol |
|------|--------------|--------|-----|
| Temozolomid | BOS/plazma ~0.20 | Türkiye onkoloji | V5 alkilleyici omurga; DNA-hasar zemini |
| Regorafenib | orta/sınırlı | Türkiye onkoloji | V3/V8; REGOMA randomize kanıtı |
| Paxalisib | ölçülmüş-iyi (beyin-penetran) | deneme | V3 direkt PI3K/mTOR |
| Adavosertib (WEE1i) | ölçülmüş-iyi | deneme | V2 p53-null sintetik-letal |
| Marizomib | ölçülmüş-iyi (beyin-geçen proteazom) | deneme/yurtdışı | ⭐ V4/NF-κB doğrudan |
| Dordaviprone (ONC201) | ölçülmüş-iyi | deneme/yurtdışı | Yeni eksen; koşullu (H3K27M) |
| Bevacizumab (Altuzan) | geçmez (damar hedefi) | hasta kullanıyor | V7/V8; hücre-içi düzey kriteri uygulanmaz |
| Keppra / Lamide | CNS-aktif | hasta kullanıyor | Destek (tümör hedefi değil); Lamide → QT/EKG kısıtı |

**Sonuç:** *Repurposing (A tipi)* ilaçlar arasında doğrudan tek-başına tümör-öldürücü doza
gerçekçi biçimde en yakın olan **mebendazol**; **HCQ** sınırda. Diğer repurposing ilaçlar
(metformin, statin, celecoxib) **sinerjik/modülatör** rolde değerlidir — kombinasyon mantığı
(bkz. `TWO_TRACK_STRATEGY.md`) tam da bu yüzden önemlidir: tek ilaç sitotoksik düzeye ulaşamasa
da, farklı düğümlere aynı anda düşük-doz baskı uygulanır. *Klinik dozu tanımlı (B tipi)*
ilaçlarda (paxalisib, marizomib, adavosertib, dordaviprone, temozolomid) "hücre-içi yeterli
düzey" sorusu zaten klinik/faz dozuyla yanıtlanmıştır; bunlarda kritik soru beyin geçişi ve
erişimdir — pano incelemesi (`PANO_INCELEME_kanit_ve_hucre_ici_duzey.md`) bunları
"beyin-ölçülmüş-iyi + insan kanıtlı" olarak doğruladı.
