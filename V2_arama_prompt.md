# GÖREV: Rekürren Glioblastom için V2 (TP53 kaybı → G2/M sintetik-letal) yolağını hedefleyen, KAN-BEYİN BARİYERİNİ GEÇEN ilaç adayı bul

Sen bir nöro-onkoloji ilaç-araştırma uzmanısın. Aşağıdaki KESIN kriterlere göre aday ilaç/molekül arayacaksın. Amaç: gereksiz adaylarla vakit kaybetmemek — kanıt barajını geçmeyen hiçbir şeyi "aday" olarak sunma.

## HASTA BAĞLAMI (sabit)
- Tanı: Rekürren glioblastom (GBM), IDH-yabanıl, RTK1 metilasyon alt tipi, CNS WHO Grade 4
- MGMT: metillenmemiş · TMB düşük (4.7) · MSS · H3K27M NEGATİF
- Hedeflenen zayıflık: **V2 — TP53 çoklu kayıp (splice c.672+1G>C, Y163N, G245S, P152L; truncal)** → hücre G1 kontrol noktasını kaybeder, **G2/M kontrol noktasına ve mitoza BAĞIMLI** hale gelir. En yüksek öncelikli (P1) zayıflık.
- Hasta hâlihazırda kullanıyor: bevacizumab, levetirasetam (Keppra), lakozamid (Lamide — QT/kardiyak dikkat)

## SİNTETİK-LETAL MANTIK (bu zayıflığın özü)
TP53-kayıplı hücre G1'de duramaz → G2/M'e aşırı bağımlıdır. G2/M kontrol noktasını veya mitozu bozan ajanlar bu hücrelerde **mitotik katastrofi** yaratır (sağlıklı p53-normal hücrelerde daha az).

## HANGİ HEDEF DÜĞÜMLERİ (V2 için druggable noktalar)
- **WEE1** kinaz inhibisyonu (G2/M kapı bekçisi)
- **CHK1 / CHK2** inhibisyonu
- **ATR** inhibisyonu (replikasyon stresi kontrol noktası)
- **PLK1** inhibisyonu
- Mitotik iğ/mikrotübül hedefleri (mitotik arrest — G2/M bağımlılığını sömürür)

## ZORUNLU KRİTERLER (hepsi karşılanmalı — biri eksikse ADAY DEĞİLDİR)
1. **Kan-beyin bariyerini geçmeli.** Ölçülmüş beyin/BOS verisi veya güçlü CNS-penetrasyon kanıtı. Küçük molekül olmalı; makromoleküller (antikor/oligonükleotid) otomatik ELENİR.
2. **Klinik-aşama olmalı** (Faz ≥1). Yalnız-preklinik = "izleme", aday değil.
3. **GBM/glioma'da kanıt olmalı** — tercihen klinik, en az in-vivo. Yalnız hücre-hattı veya derleme YETERSİZ.
4. **Mekanizma sintetik-letal mantığa uymalı** — yukarıdaki düğümlerden birini hedeflemeli VE TP53-kayıplı/G2/M-bağımlı bağlamda etkili olmalı.
5. **Kanıt yönü destekleyici olmalı** (negatif değil).

## DEĞERLENDİRME DİSİPLİNİ
- **Kanıt-düzeyi > kanıt-varlığı.** Preklinik/Faz-0 sinyal klinik öneri için yetersizdir — abartma.
- Her iddiayı **gerçek DOI veya NCT** ile destekle. UYDURMA — emin değilsen "referans bulunamadı" yaz.
- **QT/kardiyak dikkat KRİTİK:** birçok mitotik/kinaz inhibitörü QT uzatır; hasta lakozamid (Lamide) kullanıyor → QT-uzatan aday için bazal+takip EKG şart. Bunu her aday için işaretle.
- Miyelosupresyon örtüşmesi kontrol et (hasta temozolomid/lomustin alabilir).

## ÖNCEDEN DEĞERLENDİRİLMİŞ (bunlar zaten sistemde — yalnız DAHA İYİ veya EK aday ara)
- **Adavosertib (WEE1i)** — sistemde aktif V2 adayı (klinik-aşama, WEE1 sintetik-letal, GBM RT-sinerji verisi). Bunu geçen bir alternatif ara.
- **Ceralasertib (ATRi)** — sistemde V2 adayı (ATR inhibitörü).
- **Eribulin** — mikrotübül inh., beyne girer + GBM in-vivo (DOI 10.1111/cas.14067) ama klinik GBM verisi yok, QT+Lamide kısıtı → İZLEMEDE (WEE1i altında öncelik).
Not: V2 bir BOŞLUK DEĞİL — adayları var. Amaç: bunlardan daha iyi kanıtlı, daha iyi beyne-giren, ya da farklı düğümü (CHK1/PLK1) hedefleyip mevcutları tamamlayan yeni bir aday.

## ÇIKTI FORMATI (her aday için tablo)
İlaç adı · Hedef düğüm (WEE1/CHK1/ATR/PLK1/mitotik) · Klinik faz · Modalite · KBB kanıtı (+ref) · GBM/glioma kanıtı (+DOI/NCT) · QT/kardiyak profili (Lamide ile) · Kanıt yönü · Mevcuttan (adavosertib/ceralasertib) daha iyi mi/tamamlayıcı mı? · SONUÇ (ADAY/İZLEMEDE/ELENDİ + gerekçe)

Yeni bir şey kriterleri karşılamıyorsa açıkça söyle: "V2 için mevcut adayları geçen yeni bir aday bulunamadı." Zorlama aday üretme.
