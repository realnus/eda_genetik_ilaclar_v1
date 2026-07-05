# "Beklemede" Tablosu Taraması — 56 KBB-zayıf/bilinmeyen İlaç

**Kaynak:** `GBM Repurposing — Aday Panosu`, alt tablo (56 ilaç). Bunlar panonun
**KBB geçişi zayıf veya bilinmeyen** olduğu için otomatik olarak öncelikli listeden
düşürdüğü ilaçlar. Sorunuz: bu tabloda gözden kaçmış güçlü bir aday var mı?

![Skor dağılımları — öncelikli vs beklemede]({{artifact:58547679-3719-467d-aafe-80fe1c685013}})

## Ana sonuç: filtre çalışıyor — beklemede ilaçların HİÇBİRİ iki eşiği geçmiyor

Skor dağılımları neredeyse tamamen ayrık:
- **Öncelikli tablo (KBB-uygun):** medyan skor **62**, tavan 94.
- **Beklemede tablo (KBB-zayıf):** medyan skor **11**, **tavan yalnızca 18.2**.

En yüksek skorlu beklemede ilaç (AZD7762, 18.2) bile öncelikli tablonun en alt ucundan
düşük. Bunun tek nedeni skorun beyin-konsantrasyonunu ağırlıklandırması: bu ilaçların
**hücre içi yeterli düzey** kriteri kanıtlanmamış. Yani "gözden kaçmış güçlü aday" yok —
ama iki mekanik gözlem stratejik olarak değerli:

## Gözlem 1 — ⭐ V6_WNT gap: mekanizma VAR, beyin geçişi kanıtı YOK

Benim sistemimde V6 (WNT/TCF7L2 delesyonu) **kalıcı gap** idi (doğrudan güçlü Wnt ilacı yok).
Beklemede tabloda tam da bu düğüm için **11 mekanik aday** birikmiş:
- **Porcupine inhibitörleri:** LGK-974 (16.7), ETC-159 (16.0), G007-LK, cirtuvivint
- **β-katenin/kondensat:** DPTX3186 (16.2)
- **niclosamide** (14.4, Wnt/STAT3)

**Ama hepsi KBB:bilinmeyen.** Yani V6 için ilaç sınıfı mevcut, fakat hiçbirinin beyne
ulaştığı kanıtlanmamış. → V6 gap'i "ilaç yok" değil, **"beyne giren ilaç yok"** olarak
güncellenmeli. Bu, gap'in doğasını netleştiriyor (kapsam sorunu değil, iletim sorunu).

## Gözlem 2 — V4_NFKB: doğrudan NF-κB inhibitörleri (ama zayıf KBB)

Öncelikli tablo V4 için proteazom inhibitörlerini (Marizomib vb.) sunmuştu. Beklemede
tabloda **doğrudan NF-κB yolu** inhibitörleri var: NIK/MAP3K14 inhibitörleri (13.5, 12.2),
BAY 11-7082 (10.9), IKKβ inhibitörü. Mekanik olarak daha spesifik ama beyin geçişleri
kanıtsız → Marizomib hâlâ V4 için en gerçekçi yol.

## Gözlem 3 — bilinen isimlerin teyidi

- **everolimus** (17.4, KBB:ölçülmüş-**zayıf**): benim V3 yedek seçimim. Pano "ölçülmüş ama
  zayıf beyin geçişi" diyor → paxalisib'in neden birincil tercih olduğunu doğruluyor.
- **atorvastatin** (14.0, KBB:ölçülmüş-zayıf): önceki bulguyu üçüncü kez teyit — simvastatine
  kaydırma önerisi sağlam.
- **disulfiram** (15.5): zaten DIRECT randomize denemesi negatif olduğu için çıkarmıştım;
  pano da beklemede tabloda + zayıf KBB → çıkarma kararı üç yönden destekli.
- **sulfasalazine** (13.7, system xc−/SLC7A11): ferroptoz/glutamat ekseni — ilginç ama
  düşük skor + zayıf KBB.

## Sonuç ve öneri

**Sorunuzun cevabı: Beklemede tabloda öncelikli listeye yükseltilecek "gizli güçlü aday" yok** —
ve bu iyi haber, çünkü panonun KBB-filtresinin sağlam çalıştığını gösteriyor. Ancak tarama
V6_WNT gap'inin doğasını netleştirdi: sorun ilaç sınıfının olmaması değil, mevcut Wnt
ilaçlarının (Porcupine/β-katenin inhibitörleri) beyne ulaştığının kanıtlanmamış olması.

**Onkoloğa/araştırmaya not:** V6 için beyin-penetran bir Wnt inhibitörü çıkarsa (veya
mevcutların intratümöral/konveksiyon-destekli iletimi), bu gap kapanabilir — ama bugün
kanıtlı bir seçenek yok. Düşük öncelikli/keşif ekseni olarak kalmalı.

*Not: Skorlar otomatik derlemedir; "bilinmeyen KBB" ilacın beyne geçmediğini kanıtlamaz,
yalnızca geçtiğine dair ölçüm bulunmadığını gösterir. Yeni veriyle değişebilir.*
