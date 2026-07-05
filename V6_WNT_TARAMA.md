# V6 (Wnt/TCF7L2) Boşluk — Odaklı Tarama Raporu
_Tarih: 2026-07-05 · Kapsam: klinik-aşama Wnt/β-katenin inhibitörleri, GBM/glioma kanıtı + KBB_

## Amaç
V6_WNT_TCF7L2, sistemin uzun süredir en zayıf noktası: "beyne giren, klinik-aşama, güçlü Wnt ilacı yok".
Bu tarama, o boşluğu kapatacak bir aday olup olmadığını sistematik olarak test etti.

## Taranan druggable düğümler (ChEMBL)
- **Porcupine (PORCN)** — WNT salgısı · CHEMBL1255163
- **Tankyrase 1/2 (TNKS/TNKS2)** — Axin stabilizasyonu · CHEMBL6164 / CHEMBL6154
- **β-katenin (CTNNB1) + TCF4/β-katenin kompleksi** · CHEMBL5866 / CHEMBL3038511
- **CK1α (CSNK1A1)** · CHEMBL2793

## Bulunan klinik-aşama Wnt inhibitörleri
| Aday | Hedef | Faz | Modalite | GBM/glioma kanıtı |
|---|---|---|---|---|
| WNT-974 (LGK-974) | Porcupine | 2 | küçük molekül | Yok (derleme + in-vitro germ hücre) |
| PRI-724 (foscenvivint) | CBP/β-katenin | 2 | küçük molekül | Yok (derleme) |
| E-7386 | CBP/β-katenin | 1 | küçük molekül | Yok (kolorektal organoid) |
| Vantictumab | FZD reseptör | 2 | **antikor** | Yok — makromolekül, KBB geçemez |
| Ipafricept | FZD-8 tuzak | 2 | **füzyon proteini** | Yok — makromolekül, KBB geçemez |
| Curcumin | Wnt (dolaylı, pleiotropik) | 3 | doğal bileşik | GBM-Wnt'e özgü klinik kanıt yok; düşük biyoyararlanım/KBB sorunu; spesifik olmayan çok-hedefli |
| Dimethylcurcumin | Wnt (dolaylı) | 2 | doğal bileşik türevi | Aynı — GBM-Wnt spesifik klinik kanıt yok |

## Sonuç — DÜRÜST DEĞERLENDİRME
**V6 boşluğunu kapatacak, kanıt barajını geçen bir aday BULUNAMADI.**

1. **Küçük moleküller (WNT-974, PRI-724, E-7386):** Hiçbirinin GBM/glioma'da klinik etkinlik kanıtı yok.
   Literatür tamamen derleme + in-vitro (germ hücre, kolorektal). Klinik dokümana giremezler.
2. **Antikorlar (vantictumab, ipafricept):** Makromolekül — kan-beyin bariyerini geçemezler; GBM için
   yapısal olarak uygunsuz. Elenmiştir.
3. **Tankyrase inhibitörleri:** GBM in-vivo literatürü yalnız preklinik/derleme; klinik-aşama beyne-giren
   tankyrase ilacı yok.

## Karar
- V6 klinik dokümanda **GAP olarak kalır** — bu bir arama eksikliği değil, alanın gerçeği:
  beyne giren, klinik-aşama, GBM-kanıtlı bir Wnt ilacı **henüz mevcut değil**.
- WNT-974, DB'de **izlemede** tutulur (en umut verici küçük molekül); klinik glioma verisi çıkarsa yeniden değerlendirilir.
- Aylık sürveyans bu düğümü izlemeye devam eder.

## Yöntem notu
Bu, projenin kanıt-düzeyi disiplininin doğru çalıştığının kanıtıdır: geniş bir Wnt-hedef taraması yapıldı,
adaylar bulundu, ama hiçbiri onkoloğa gidecek klinik dokümana eklenmeyi hak edecek kanıta sahip değil.


---

## EK: Gevşetilmiş-kural denemesi ve nihai karar (2026-07-05)

V6 için standart kriterlerle aday çıkmayınca, hangi kriterin **güvenle** gevşetilebileceği değerlendirildi:
- **Gevşetilemez:** KBB geçişi (fiziksel engel) ve kanıt-yönü (negatif olmama) — gevşetmek kendimizi kandırmaktır.
- **Gevşetilebilir:** "GBM klinik kanıtı" → "güçlü ortotopik/intrakraniyal glioma in-vivo etkinliği".

**Gevşetilmiş kuralla in-vivo glioma taraması yapıldı** (WNT-974, PRI-724, tankiraz inhibitörleri, XAV939 için ortotopik/intrakraniyal sağkalım verisi arandı). **Sonuç:** temiz bir in-vivo glioma etkinlik profili olan Wnt küçük molekülü yine bulunamadı — kanıt hücre-hattı seviyesinde takılı.

### Nihai karar: V6 KABUL EDİLEN BOŞLUK
- V6, en düşük öncelikli zayıflık (priority=3, TCF7L2 delesyonu — truncal sürücü değil).
- Kanıtı in-vitro seviyede kalan bir ilacı eklemek toksisite + DDI yükü getirir (örn. WNT-974'ün bevacizumab ile GI toksisite örtüşmesi), net fayda belirsizdir.
- **Karar:** V6 bilinçli olarak hedeflenmeden bırakılır; ilaç bütçesi kanıtı güçlü zayıflıklara (V2 sintetik-letal, V4 proteazom) ayrılır.
- WNT-974 DB'de izlemede kalır; klinik/in-vivo glioma verisi çıkarsa aylık sürveyans yeniden değerlendirir.
- `vulnerability.is_gap=1` olarak DB'ye işlendi.
