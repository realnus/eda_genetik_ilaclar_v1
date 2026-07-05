# İteratif İlerleme Raporu — Sürveyans Çalıştırması #2
**Tarih:** 2026-07-05 13:32:16 · **Taranan aday:** 19 · **Öneri:** 12 · **Not:** v2 — erişim-track + rol kısıtı eklendi

Bu rapor otomatik üretildi. Öneriler **terfi edilmedi** — onkolog onayına kadar TWO_TRACK_STRATEGY değişmez.

## 1) İkame önerileri (mevcut ilacı daha iyisiyle değiştir)

| Kombinasyon | Düğüm | Mevcut | → Öneri | Neden daha iyi (regresyonsuz) |
|---|---|---|---|---|
| K2 | V7_METABOLIC mevalonat/kolesterol | Atorvastatin | **Simvastatin** [F] | BBB olculmus-zayif→olculmus-iyi, dose-gap 0.002→0.01, toksisite 3→2 |
| K3 | V7_METABOLIC mevalonat/kolesterol | Atorvastatin | **Simvastatin** [F] | BBB olculmus-zayif→olculmus-iyi, dose-gap 0.002→0.01, toksisite 3→2 |
| K5 | V7_METABOLIC mevalonat/kolesterol | Atorvastatin | **Simvastatin** [F] | BBB olculmus-zayif→olculmus-iyi, dose-gap 0.002→0.01, toksisite 3→2 |

## 2) Boşluk-doldurma önerileri (kapanmayan düğümü doğrudan vur)

| Kombinasyon | Zayıflık/Düğüm | + Aday | Erişim | Gerekçe |
|---|---|---|---|---|
| K2 | V2_TP53 mitotik-mikrotübül | **Mebendazol** | F | V2_TP53::mitotik-mikrotübül düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K2 | V3_PTEN_PI3K PI3K/mTOR-direkt | **Everolimus** | A | V3_PTEN_PI3K::PI3K/mTOR-direkt düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K3 | V2_TP53 mitotik-mikrotübül | **Mebendazol** | F | V2_TP53::mitotik-mikrotübül düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K3 | V3_PTEN_PI3K PI3K/mTOR-direkt | **Everolimus** | A | V3_PTEN_PI3K::PI3K/mTOR-direkt düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V2_TP53 mitotik-mikrotübül | **Mebendazol** | F | V2_TP53::mitotik-mikrotübül düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V4_NFKB proteazom→NF-κB (DOĞRUDAN) | **Marizomib** | O | V4_NFKB::proteazom→NF-κB (DOĞRUDAN) düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V4_NFKB proteazom→NF-κB (DOĞRUDAN) | **Bortezomib** | O | V4_NFKB::proteazom→NF-κB (DOĞRUDAN) düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V2_TP53 ATR-replication-stress | **Ceralasertib (ATRi)** | T | V2_TP53::ATR-replication-stress düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |
| K5 | V1_TERT telomerase-catalytic | **6-thio-2-deoxyguanosine** | T | V1_TERT::telomerase-catalytic düğümü doğrudan kapanmıyor → doğrudan vurur, düşük toksisite |

## 3) Kanıt doğrulama durumu

Öneriler yapısal (düğüm+eksen) mantıkla üretildi. Terfiden önce her aday için **kanıt doğrulama kapısı** çalışmalı (OpenAlex DOI + yön kontrolü, klinik çalışma durumu, FDA etiketi). Bu, deploy paketindeki `verify.py`'nin işi.

## 4) Önerilen sonraki adım

Onkolog onaylarsa: ilgili `proposal.status='approved'` → `promote.py` çalışır → TWO_TRACK_STRATEGY.html + _doz.md güncellenir, `proposal.status='promoted'`.
