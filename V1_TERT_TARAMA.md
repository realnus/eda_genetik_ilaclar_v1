# V1_TERT Boşluk — Gevşetilmiş-Kural Odaklı Tarama Raporu
_Tarih: 2026-07-05 · Zayıflık: V1_TERT (TERT promotör C250T, truncal — P1 en yüksek öncelik)_
_Kural: KBB + kanıt-yönü gevşetilemez; "klinik kanıt" → "in-vivo glioma etkinliği" gevşetildi_

## Neden bu tarama V6'dan daha değerli
V1_TERT, tümörün **truncal sürücüsü** (her hücrede, VAF %23) ve en yüksek öncelikli (P1) zayıflık.
Haritada "riskli bölge"deydi: çok önemli ama erişilebilir ilaç yok. V6 (P3) için harcanan çabanın
buraya yöneltilmesi çok daha yüksek getirili.

## Bulunan adaylar (gevşetilmiş kural: in-vivo glioma etkinliği)

| Aday | Mekanizma | Modalite | KBB | GBM in-vivo kanıtı | SONUÇ |
|---|---|---|---|---|---|
| **6-thio-dG (THIO / ateganosine)** | Telomeraz substrat öncüsü → telomer disfonksiyonu (GERÇEK TERT-bağımlı) | küçük molekül nükleozit | tahmini (nükleozit) | Telomeraz-pozitif kanserde telomer disfonksiyonu; GBM-spesifik in-vivo sınırlı | **İZLEMEDE — en umut verici mekanizma** |
| **Imetelstat** | Telomeraz template antagonisti (GERÇEK TERT hedefi) | **oligonükleotid (büyük molekül)** | ZAYIF — oligonükleotid, KBB doğal geçişi düşük | GBM tümör-başlatıcı hücrede in-vivo etkinlik (DOI 10.1158/1078-0432.ccr-09-2850, 2010) | **ELENDİ — KBB engeli (makromolekül)** |
| **Eribulin** | **Mikrotübül inhibitörü — TERT DEĞİL** | küçük molekül | ÖLÇÜLMÜŞ — beyin dokusuna penetre (DOI 10.1111/cas.14067, 2019) | İntraserebral GBM'de RT ile sağkalım artışı (DOI 10.1111/cas.13637, 2018) | **YANLIŞ DÜĞÜM — V1 değil (mitotik, V2'ye yakın)** |

## Dürüst mekanizma ayrımı (kritik)
- **6-thio-dG** ve **imetelstat** GERÇEK telomeraz/TERT hedefli. Ama imetelstat oligonükleotid →
  KBB'yi geçemez (V6'daki antikorlarla aynı fiziksel engel) → elenir.
- **Eribulin** GBM'de beyne girip in-vivo sağkalım gösteriyor — GÜÇLÜ bir veri — AMA mekanizması
  mikrotübül inhibisyonu, TERT DEĞİL. V1_TERT için "TERT hedefliyor" diye sunmak yanıltıcı olur.
  Eribulin'i V1 adayı saymıyoruz; ayrı bir mitotik-hedef (V2 komşusu) fırsatı olarak NOT ediyoruz.

## Sonuç
- **V1_TERT için beyne-giren, gerçek-TERT-hedefli, klinik-aşama aday:** yok. En yakın olan
  **6-thio-dG** (küçük molekül, gerçek telomer-disfonksiyon mekanizması) — ama GBM in-vivo verisi
  henüz sınırlı → **İZLEMEDE**, klinik dokümana terfi YOK.
- **Imetelstat** gerçek TERT hedefi ama makromolekül → KBB engeli, elendi.
- **Eribulin** ilginç bir yan bulgu: beyne giren, GBM in-vivo etkinlikli küçük molekül — ama
  TERT değil mitotik. Ayrı değerlendirilebilir (bu V1 taramasının kapsamı dışında).

## Karar
- V1_TERT klinik dokümanda **boşluk olarak kalır** — ama V6'dan farklı olarak bu YÜKSEK öncelikli
  bir boşluk; izleme aktif tutulmalı.
- 6-thio-dG DB'de izlemede; GBM ortotopik in-vivo veya Faz 1 verisi çıkarsa yeniden değerlendir.
- Eribulin'in mitotik/beyin-penetran profili ayrı bir not olarak kaydedildi (V1 değil).


---

## EK: 6-thio-dG derin inceleme (2026-07-05) — durum yükseldi

İlk taramada OpenAlex abstract'ları boş döndüğü için "GBM in-vivo sınırlı" demiştim. Makalenin ABSTRACT'ı (DOI 10.1158/1535-7163.mct-17-0792, 2018; fetch_article_fulltext ile — tam metin PDF açık erişimde bulunamadı, found=false, ancak yayıncı abstract'ı döndü) çekilince beyin tümörlerinde doğrudan in-vivo kanıt bulundu (aşağıdaki bulgular abstract'ta birebir yer alıyor):
- **KBB geçişi DOĞRULANMIŞ:** ortotopik DIPG modelinde 6-thio-dG kan-beyin bariyerini geçip tümör hücrelerini spesifik hedefliyor.
- **Beyin tümörü in-vivo etkinlik:** medulloblastom ksenograftında tümör büyümesi gecikmesi; DIPG/HGG kök hücrelerinde hücre ölümü; ATR/ATM → G2-M arrest.
- **Gerçek TERT mekanizması:** telomeraz-bağımlı substrat analoğu, telomere katılım → telomer disfonksiyonu. Hastanın TERT promotör C250T mutasyonu (telomeraz-pozitif) ile mekanistik olarak tam uyumlu.
- **Klinik-aşama:** THIO-101 Faz 2 (ateganosine + ICI, NSCLC, 2025).

**KISIT (dürüstlük):** beyne-in-vivo veri PEDİATRİK beyin tümörlerinde (DIPG, HGG, medulloblastom); klinik çalışma NSCLC'de. **Erişkin GBM'de spesifik in-vivo/klinik veri henüz yok.**

**Güncellenmiş sonuç:** 6-thio-dG artık **V1 için en güçlü aday** — gevşetilmiş kuralı (in-vivo glioma + klinik-aşama) geçiyor. Eribulin (V2) ile aynı seviye: deneysel, izlemede, onkoloğa sunulmaya değer. Erişkin GBM verisi çıkarsa klinik dokümana terfi. Terfi için baraj: erişkin GBM ortotopik in-vivo VEYA glioma Faz 1+ verisi.


### Kaynak doğrulama (abstract'tan birebir alıntılar)
Aşağıdaki in-vivo bulgular, makalenin yayıncı abstract'ında (DOI 10.1158/1535-7163.mct-17-0792) birebir şu cümlelerden alınmıştır — okuyucu DOI'den doğrulayabilir:
- "In vivo treatment of mice bearing medulloblastoma xenografts with 6-thio-dG delays tumor growth and increases in-tumor TIFs and apoptosis."
- "6-thio-dG crosses the blood–brain barrier and specifically targets tumor cells in an orthotopic mouse model of DIPG."
- "Treatment with 6-thio-dG elicits a sequential activation of ATR and ATM pathways and induces G2–M arrest."
- "cell growth inhibition, and cell death of primary stem-like cells derived from patients with DIPG, HGG, and medulloblastoma."

Not: Bu cümleler makale ABSTRACT'ından; tam metin (deney dozları, hayvan sayıları, sağkalım eğrileri) açık erişimde bulunamadı. Kanıt düzeyi = abstract.
