# Gereksiz Tekrar mı, Çok-Düğümlü Saldırı mı? — İlaç Örtüşme Analizi

**Sorunuzun cevabı — kombinasyon onkolojisinin temel prensibi:**

> Aynı zayıflığı birden çok ilaçla hedeflemek, ancak ilaçlar **farklı mekanizma
> düğümlerinden** vuruyorsa değerlidir (buna "dikey/çok-düğümlü blokaj" denir — bir yolu
> tek noktadan değil, birkaç noktadan aynı anda kapatmak kaçış yollarını azaltır). Ama iki
> ilaç **aynı düğümü aynı şekilde** vuruyorsa, ikincisi çoğu zaman ek fayda getirmeden
> **sadece toksisite ekler.** İşte sizin sezginiz burada doğru.

> **Tıbbi tavsiye değildir.** Bu, hangi ilaçların gerçekten benzersiz katkı yaptığını, hangi
> ilaçların birbirinin yerine geçebileceğini gösteren bir *karar-destek* analizidir. Nihai
> seçim onkoloğundur.

![Zayıflık → düğüm → ilaç haritası]({{artifact:art_fd9ac817-5ae5-43c5-8aa5-3d6f24e50e9f}})

---

## 1. Anahtar fark: "zayıflık" değil, "düğüm" düzeyinde düşünmek

Her zayıflık (V1–V8) tek bir hedef değil; içinde **birden çok druggable mekanizma düğümü**
barındırır. Örneğin V7 (metabolik) en az 4 ayrı düğüme ayrılır: OXPHOS, mevalonat, otofaji,
anti-anjiyogenez. İki ilaç "ikisi de V7'yi hedefliyor" olabilir ama **farklı düğümlere**
vuruyorlarsa gerçek bir çok-düğümlü saldırıdır, tekrar değildir.

> **V6 hakkında bir düzeltme notu.** İlk iterasyonda V6 (Wnt/TCF7L2) **"boşluk — 0 ilaç"**
> olarak işaretlenmişti. Bu düğüm haritasında celecoxib'i V6'ya dolaylı bir COX-2/Wnt-β-katenin
> mekanizmasıyla bağladım — ama bu **zayıf ve dolaylı** bir bağdır; önceki "boşluk" bulgusu
> pratikte hâlâ geçerlidir. V6'yı "artık kapsandı" saymayın: doğrudan güçlü bir Wnt/GSK3 ilacı
> hâlâ yok. Bu, tabloda düşük öncelikli/keşifsel olarak işaretlenmiştir.

**Bevacizumab örneğiniz tam da bunu gösteriyor:** hasta zaten bevacizumab kullanıyor ve bu,
V7/V8'in **VEGF/damar** düğümünü kapsıyor. Ama V7'nin OXPHOS düğümü (metformin), mevalonat
düğümü (statin), otofaji düğümü (HCQ) **hâlâ boş** — yani V7'yi "tekrar hedeflemek" değil,
V7'nin *farklı düğümlerini* kapatmaktır. Bu gereksiz değildir.

---

## 2. Analizin sonucu: her ilaç benzersiz mi?

Her ilacın dokunduğu tüm düğümleri başka bir ilaç da kapsıyorsa, o ilaç "tekrar adayı"dır.

### ✓ Benzersiz katkı yapan ilaçlar (her biri en az bir düğümün TEK sahibi)
Metformin (OXPHOS), Atorvastatin (mevalonat), Hidroksiklorokin (otofaji/NF-κB), Celecoxib
(COX2→NF-κB, Wnt, myeloid), Mebendazol (mitotik), Valproik asit (HDAC), Regorafenib
(multikinaz), Bevacizumab (VEGF — **zaten kullanılıyor**), WEE1-i (G2/M), ATR-i (replikasyon
stresi), 6-thio-dG (telomeraz). → **Bunlar birbirinin yerine geçmez; her biri ayrı bir kapıyı
kapatır.**

### ⚠ Tekrar adayları (tüm düğümleri başka ilaçlarca da kapsanan)
| İlaç | Paylaşılan düğüm | Yorum — gerçekten gereksiz mi? |
|------|------------------|-------------------------------|
| **Temozolomid ↔ Lomustin** | alkilleyici-DNA-hasarı | **SEÇ-BİRİNİ.** İkisi de alkilleyici; aynı anda ikisini birden vermek nadiren gerekir, kemik iliğini iki katına yükler. Onkolog **birini** seçer. |
| **Paxalisib ↔ Everolimus** | PI3K/mTOR-direkt | **SEÇ-BİRİNİ.** İkisi de PI3K/mTOR ekseni. Paxalisib beyin-geçişli ve daha güçlü; everolimus sadece paxalisib erişilemezse **yedek** (Strateji 3). Birlikte kullanılmaz. |
| **İtraconazol** | otofaji (HCQ ile), anti-anjiyogenez (bevacizumab/regorafenib ile) | **EN ÖNEMLİSİ — aşağıda.** |

---

## 3. İtraconazol: sizin işaret ettiğiniz asıl vaka

İtraconazolün dokunduğu **her** düğüm başka bir ilaçça zaten kapsanıyor:
- **Otofaji düğümü** → zaten **hidroksiklorokin** var (daha kanıtlı otofaji inhibitörü).
- **Anti-anjiyogenez düğümü** → zaten **bevacizumab** (hasta kullanıyor) + **regorafenib** var.

Yani itraconazol **benzersiz bir kapı açmıyor.** Buna karşılık en ağır **CYP3A4 etkileşim
yükünü** ve kalp/karaciğer toksisitesini getiriyor (toksisite raporunda "etkileşim tuzağı"
olarak işaretlenmişti). 

**Sonuç:** itraconazol, fayda/zarar dengesi en zayıf ilaçtır — çünkü kattığı her mekanizma
zaten kapsanıyorken, en yüksek etkileşim riskini ekliyor. **Çıkarılması veya en sona
bırakılması** en mantıklı adaydır. Sizin sezginiz doğru.

---

## 4. Önerilen alt-strateji yapısı (sorduğunuz gibi)

Her ana strateji, **düğüm-başına-tek-ilaç** ilkesiyle sadeleştirilmiş alt-stratejilere ayrılır:

### Strateji 1 → Alt-strateji 1A (yalın çekirdek — düğüm başına tek ilaç)
Hastanın **mevcut bevacizumabı** (VEGF/anti-anjiyogenez) + **bir alkilleyici** (TMZ *veya*
lomustin, ikisi birden değil) + **metformin** (OXPHOS) + **atorvastatin** (mevalonat) +
**hidroksiklorokin** (otofaji) + **celecoxib** (NF-κB/Wnt/myeloid). → 7 düğüm, minimum örtüşme,
**itraconazol yok**.

### Strateji 1 → Alt-strateji 1B (yoğunlaştırılmış)
1A + **regorafenib** (multikinaz — REGOMA randomize kanıtı) + **valproik asit** (HDAC +
radyoduyarlılaştırma). Daha geniş, ama karaciğer/kemik iliği izlemi artmalı.

### Strateji 2 → Alt-strateji 2A (temiz sintetik-letal)
**Paxalisib** (PI3K/mTOR) + **WEE1-i** *veya* **ATR-i** (V2 için — ATR ayrıca V1/telomer stresini
de vurduğundan çift-truncal avantajı var). Paxalisib erişilemezse → everolimus (yedek).

### Strateji 2 → Alt-strateji 2B (telomer eklentisi)
2A + **6-thio-dG** (V1 telomeraz — deneysel; sadece erişilebilirse).

---

## 5. "Birden fazla ilaç aynı zayıflığı hedeflese daha mı iyi?" — net cevap

- **Farklı düğümlerden hedefliyorsa: EVET, daha iyi.** Tümörün kaçış yollarını azaltır
  (örn. V7'yi OXPHOS + mevalonat + otofaji + damar düğümlerinden aynı anda kapatmak).
- **Aynı düğümü aynı şekilde hedefliyorsa: HAYIR.** Ek fayda yok, toksisite iki katına çıkar
  (örn. TMZ+lomustin ikisi birden, ya da paxalisib+everolimus birlikte).
- **Uygulama kuralı:** her mekanizma düğümüne **bir güçlü ilaç** koy; ikinci ilacı ancak
  *farklı bir düğüm* açıyorsa ekle. İtraconazol bu testi geçemiyor.

Bu prensip artık makine-okunur (`vulnerability_nodes.json`, `drug_redundancy_class.json`) —
kombinasyon motoruna bağlanıp her rejim için otomatik "bu iki ilaç aynı düğümde çakışıyor"
uyarısı üretebilir.
