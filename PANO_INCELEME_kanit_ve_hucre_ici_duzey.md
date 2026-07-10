# İki Panonun İncelemesi — "Hem Kanıt Hem Hücre-İçi Yeterli Düzey" Filtresi

**Kaynak:** Başka bir projede hazırlanan iki pano:
`GBM Genomik Profil — Aday & Çalışma Panosu` (78 genomik aday, 227 çalışma) ve
`GBM Repurposing — Aday Panosu` (207 ilaç; 151'i KBB-uygun, 56'sı beklemede).

**Soru:** Bu panolardaki etken maddeler arasında, kullanılan sistemin hedeflediği tümör
zayıflıklarına (V1–V8) etki eden, **hem kanıt düzeyi hem de tümör hücresi içi konsantrasyonu
yeterli** aday var mı?

**Yöntem:** Her iki panoyu ayrıştırdım. Filtre iki eşikli:
1. **KBB = "ölçülmüş–iyi"** → beyin/tümör konsantrasyonu deneysel ölçülmüş (sadece "geçer" değil).
2. **En iyi kanıt = "İnsan çalışması / vaka"** → klinik kanıt düzeyi.
Bu tam da doz-boşluk analizin ("BBB'yi geçmek yetmez, hücre içi düzey gerekir") pano
karşılığıdır: pano zaten KBB-zayıf ilaçları otomatik "beklemede" tablosuna düşürmüş.

---

## Ana bulgu: EVET — panolar hem boşlukları dolduran hem seçimlerimi doğrulayan adaylar içeriyor

![Pano adayları vs mevcut sistem]({{artifact:14ebb105-bc9d-4fb3-b552-754e4501d30b}})

### 1. ⭐ V4_NFKB — en önemli boşluk-doldurucu (proteazom inhibitörleri)
Mevcut sistemimde **V4 (NFKBIA delesyonu → NF-κB) için güçlü ilaç yoktu** — sadece HCQ (dolaylı)
ve celecoxib (zayıf) vardı. Panolar burada gerçek bir cevap sunuyor:
- **Marizomib** — skor 86.7, **beyin-ölçülmüş-iyi**, geri-dönüşsüz proteazom inhibitörü, GBM insan çalışması. Beyne geçen ilk proteazom inhibitörlerinden.
- **Bortezomib** (71.3), **ixazomib** (65.0), **CBL0137** (69.0, FACT/NF-κB) — hepsi beyin-ölçülmüş + insan kanıtlı.
→ Bu, sistemimin en zayıf düğümünü kanıtla dolduran gerçek bir kazanım.

### 2. ✓ V2_TP53 ve V3_PTEN — seçimlerim DOĞRULANDI (üstelik konsantrasyon ölçülmüş)
- **V2:** adavosertib (WEE1, 81.0), ceralasertib (ATR, 75.2), AZD1390 (ATM, 75.0) — hepsi **beyin-ölçülmüş-iyi + insan kanıtlı**. Sintetik-letal seçimim yalnızca "var" değil, "hücre içi yeterli düzeye ulaşıyor" kriterini de geçiyor.
- **V3:** paxalisib (80.2) beyin-ölçülmüş-iyi + insan çalışması ile en üstte. Alternatifler: temsirolimus (66), buparlisib (66) — hepsi ölçülmüş-iyi.

### 3. ⚠ V7_METABOLIC — bir DÜZELTME (atorvastatin → simvastatin)
Doz-boşluk analizim atorvastatini "geniş boşluk" olarak işaretlemişti. Pano bunu bağımsız
doğruluyor: **atorvastatin panonun KBB-ZAYIF 'beklemede' tablosunda.** Yerine pano
**simvastatin**'i (65.8, beyin-ölçülmüş-iyi, lipofilik) öneriyor. → Statin seçimini
simvastatine kaydırmak beyin geçişi açısından daha sağlam. Metformin beyin-ölçülmüş-iyi
(82.4) ama doz analizim gereği sinerjik/duyarlılaştırıcı rolde.

### 4. ⚠ İtraconazol — pano da beklemede tablosunda (ortak sonuç)
İtraconazolü zaten deprioritize etmiştim (P-gp beyin çıkışı + CYP3A4 yükü). Pano bunu
bağımsız teyit ediyor: **itraconazol KBB-zayıf 'beklemede' tablosunda.** İki ayrı analiz
aynı sonuca varıyor → çıkarma kararı sağlam.

### 5. ⭐ V1_TERT — beyin-ölçülmüş adaylar VAR (değerlendirmemi kısmen yumuşatıyor)
"V1 yalnızca deneme ile ulaşılır, gerçekçi değil" demiştim. Pano daha iyimser:
- **ateganosine** (71.0) ve **6-thio-2-deoxyguanosine** (68.0) — beyin-ölçülmüş-iyi + insan vaka.
→ Hâlâ deneysel/erişimi zor ama "tamamen ulaşılamaz" değil.

### 6. ⭐ YENİ EKSEN — dordaviprone (ONC201): sistemimde hiç yoktu
Panonun **EN YÜKSEK skorlu adayı** (94.0): DRD2 antagonisti / mitokondriyal ClpP agonisti,
beyin-geçişli, GBM insan çalışması. Bu benim genomik-eksenli (V1–V8) çerçevemde yoktu çünkü
ClpP/DRD2 ekseni profildeki alterasyonlardan türemiyor. **Önemli:** ONC201 özellikle
**H3K27M-mutant** gliomlarda onaylı yola sahip — hastanın profili IDH-wt/RTK1, H3K27M durumu
raporda belirtilmemiş. → Onkoloğa sorulacak: H3K27M test edildi mi?

---

## Özet tablo: hangi aday iki filtreyi de geçiyor?

| Zayıflık | Pano en iyi (beyin-ölçülmüş + insan) | Skor | Sistemime etkisi |
|----------|--------------------------------------|------|------------------|
| V4_NFKB | **Marizomib** (proteazom) | 86.7 | ⭐ Boşluk dolduruldu |
| V2_TP53 | adavosertib, ceralasertib | 81.0 | ✓ Seçim doğrulandı |
| V3_PTEN | paxalisib | 80.2 | ✓ Seçim doğrulandı |
| V7_METAB | metformin, **simvastatin** | 82.4 | ⚠ Statini simvastatine çevir |
| V1_TERT | ateganosine, 6-thio-dG | 71.0 | ⭐ Ulaşılabilir aday var |
| V8_IMMUNE | celecoxib | 63.0 | Zayıf (değişiklik yok) |
| V5_MGMT | valproik asit (CNS-aktif) | 60.0 | Değişiklik yok |
| (yeni) | **dordaviprone/ONC201** | 94.0 | ⭐ H3K27M kontrol et |

---

## Sonuç ve öneri

**Bu sorunun cevabı: EVET.** Panolar üç tür kazanım getiriyor:
1. **Gerçek boşluk-doldurucu:** V4_NFKB için Marizomib (beyin-ölçülmüş proteazom inhibitörü) —
   sistemimin en zayıf noktasını klinik kanıtla dolduruyor.
2. **Bağımsız doğrulama:** V2 (WEE1/ATR) ve V3 (paxalisib) seçimlerim yalnızca "var" değil,
   "hücre içi yeterli düzeye ulaşıyor" kriterini de geçiyor — bu güçlü bir teyit.
3. **İki düzeltme:** atorvastatin→simvastatin (beyin geçişi), itraconazol çıkarma kararı teyit.
4. **Bir yeni eksen:** dordaviprone/ONC201 — H3K27M durumu netleştirilmeli.

**Onkoloğa götürülecek üç somut soru:**
- Marizomib (veya bortezomib) V4/NF-κB düğümü için erişilebilir/uygun mu?
- Statin tercihini simvastatine kaydırmak beyin geçişi açısından mantıklı mı?
- H3K27M test edildi mi? (dordaviprone/ONC201 yolu için belirleyici)

*Not: Pano skorları otomatik derlemedir; her sayı kaynağından doğrulanmalıdır. Beyin-konsantrasyonu
"ölçülmüş-iyi" etiketi preklinik/klinik ölçümü gösterir ama hasta-özel tümör düzeyini garanti etmez.*
