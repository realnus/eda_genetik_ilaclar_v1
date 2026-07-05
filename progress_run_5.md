# İteratif İlerleme Raporu — Çalıştırma #5
**Tarih:** 2026-07-05 13:44:06 · **Taranan aday:** 22 · **Öneri:** 15 · **Not:** dogrulama-farkinda rapor testi

Otomatik üretildi. Yalnız **✅ doğrulanmış** öneriler terfi edilebilir; **⚠/⛔** etiketliler onkolog değerlendirmesi öncesi kanıt doğrulaması bekler. Klinik dosyalar onay olmadan değişmez.

## 1) İkame önerileri (mevcut → daha iyi)

| Kombinasyon | Düğüm | Mevcut | → Öneri | Kanıt | Neden (regresyonsuz) |
|---|---|---|---|---|---|
| K2 | V7_METABOLIC mevalonat/kolesterol | Atorvastatin | **Simvastatin** [F] | ⚠ kanıt yok | BBB olculmus-zayif→olculmus-iyi, dose-gap 0.002→0.01, toksisite 3→2 |
| K3 | V7_METABOLIC mevalonat/kolesterol | Atorvastatin | **Simvastatin** [F] | ⚠ kanıt yok | BBB olculmus-zayif→olculmus-iyi, dose-gap 0.002→0.01, toksisite 3→2 |
| K5 | V7_METABOLIC mevalonat/kolesterol | Atorvastatin | **Simvastatin** [F] | ⚠ kanıt yok | BBB olculmus-zayif→olculmus-iyi, dose-gap 0.002→0.01, toksisite 3→2 |

## 2) Boşluk-doldurma önerileri (kapanmayan düğümü doğrudan vur)

| Kombinasyon | Zayıflık/Düğüm | + Aday | Erişim | Kanıt | Gerekçe |
|---|---|---|---|---|---|
| K2 | V2_TP53 mitotik-mikrotübül | **Mebendazol** | F | ⚠ kanıt yok | V2_TP53::mitotik-mikrotübül düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K2 | V3_PTEN_PI3K PI3K/mTOR-direkt | **Everolimus** | A | ⚠ kanıt yok | V3_PTEN_PI3K::PI3K/mTOR-direkt düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K3 | V2_TP53 mitotik-mikrotübül | **Mebendazol** | F | ⚠ kanıt yok | V2_TP53::mitotik-mikrotübül düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K3 | V3_PTEN_PI3K PI3K/mTOR-direkt | **Everolimus** | A | ⚠ kanıt yok | V3_PTEN_PI3K::PI3K/mTOR-direkt düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V2_TP53 mitotik-mikrotübül | **Mebendazol** | F | ⚠ kanıt yok | V2_TP53::mitotik-mikrotübül düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V4_NFKB proteazom→NF-κB (DOĞRUDAN) | **Marizomib** | O | ⚠ kanıt yok | V4_NFKB::proteazom→NF-κB (DOĞRUDAN) düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V4_NFKB proteazom→NF-κB (DOĞRUDAN) | **Bortezomib** | O | ⚠ kanıt yok | V4_NFKB::proteazom→NF-κB (DOĞRUDAN) düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V2_TP53 ATR-replication-stress | **Ceralasertib (ATRi)** | T | ⚠ kanıt yok | V2_TP53::ATR-replication-stress düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V1_TERT telomerase-catalytic | **6-thio-2-deoxyguanosine** | T | ⚠ kanıt yok | V1_TERT::telomerase-catalytic düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V4_NFKB proteazom→NF-κB (DOĞRUDAN) | **Ixazomib** | O | ✅ doğrulandı (faz1-2, 2020) | V4_NFKB::proteazom→NF-κB (DOĞRUDAN) düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V4_NFKB proteazom→NF-κB (DOĞRUDAN) | **Carfilzomib** | O | ⚠ kanıt var ama doğrulanmadı | V4_NFKB::proteazom→NF-κB (DOĞRUDAN) düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V6_WNT_TCF7L2 COX/Wnt-β-katenin (ZAYIF/DOLAYLI — önceki 'GAP' bulgusu geçerli) | **WNT-974 (LGK-974)** | T | ⚠ kanıt var ama doğrulanmadı | V6_WNT_TCF7L2::COX/Wnt-β-katenin (ZAYIF/DOLAYLI — önceki 'GAP' bulgusu geçerli) düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |

## 3) Terfi edilebilir (kanıtı doğrulanmış) öneriler: 1

- **Ixazomib** → K5 / V4_NFKB (✅ doğrulandı (faz1-2, 2020))

## 4) Sonraki adım
Onkolog ✅ önerileri onaylarsa → promote.py klinik dosyaları (TWO_TRACK_STRATEGY.html, _doz.md) günceller.
