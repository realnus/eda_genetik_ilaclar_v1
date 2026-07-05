# Doz Dosyaları Dizini (dose_estimates/)

Bu klasör, `TWO_TRACK_STRATEGY.md`'deki K1–K5 kombinasyonlarında geçen **her ilaç** için
doz/beyin-konsantrasyon analizini içerir. İki dosya tipi:
- **Doz-boşluk analizi** (repurposing ilaçlar): in-vitro etkili konsantrasyon vs tümörde
  ulaşılabilir serbest konsantrasyon — "hücre-içi yeterli düzey" sorusu.
- **Doz/rol notu** (onaylı/deneme/destek ilaçlar): klinik etkinlik dozu + beyin geçişi + rol.

Yöntem: `00_YONTEM_doz_hesabi.md` · Karşılaştırma görseli: `dose_gap.png`

## İçindekiler

| # | İlaç | Zayıflık | Tip |
|---|------|----------|-----|
| 01 | mebendazol | V2-kısmi/V7 | boşluk — EN DAR |
| 02 | hidroksiklorokin | V4/V7 | boşluk — sınırda |
| 03 | valproik_asit | V5 (HDAC) | boşluk — orta; 3. AEİ |
| 04 | metformin | V7 | boşluk — çok geniş (sinerjik) |
| 05 | atorvastatin (→simvastatin) | V7 | boşluk — zayıf KBB → simvastatin |
| 06 | celecoxib | V4/V8 | boşluk — geniş (COX-2 nM yeterli) |
| 07 | itraconazol (deprioritize) | V7/V8 | boşluk — çıkarıldı (P-gp+CYP3A4) |
| 08 | temozolomid | V5 (alkilleyici) | standart — GBM omurga |
| 10 | regorafenib | V3/V8 | standart — REGOMA kanıtı |
| 11 | simvastatin | V7 | boşluk — atorvastatin yerine, beyin daha iyi |
| 12 | paxalisib | V3 | standart — deneme, beyin-penetran |
| 13 | adavosertib (WEE1) | V2 sintetik-letal | standart — deneme |
| 15 | marizomib | V4 (NF-κB) | standart — ⭐ yeni, beyin-geçen proteazom |
| 16 | dordaviprone (ONC201) | yeni eksen | standart — koşullu (H3K27M) |
| 17 | bevacizumab (Altuzan) | V7/V8 | standart — hasta kullanıyor, damar hedefi |
| 18 | levetirasetam (Keppra) | — (AEİ) | destek — PK-sessiz |
| 19 | lakozamid (Lamide) | — (AEİ) | destek — ⚠ QT/EKG kısıtı |

## Özet — hangi ilaç hücre-içi yeterli düzeye ulaşır?

- **Doğrudan sitotoksik düzeye en yakın (repurpose):** mebendazol (en dar boşluk), HCQ (sınırda).
- **Beyin-ölçülmüş-iyi + kanıtlı (deneme/onaylı):** paxalisib, adavosertib, marizomib, dordaviprone, temozolomid.
- **Sinerjik/modülatör (sitotoksik doza ulaşmaz ama yolak baskısı değerli):** metformin, simvastatin, celecoxib.
- **Çıkarılan/deprioritize:** itraconazol (zayıf beyin + ağır CYP3A4), atorvastatin (zayıf beyin → simvastatin).

*Kararlar nöro-onkologla birlikte alınmalıdır; sayılar literatür/pano derlemesidir.*
