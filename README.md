# Yoğurt Kabının Dibini Kazıma Maden İşletmeleri Genel Müdürlüğü

> Bu kurum, yoğurt kabının dibinde kalan son milimetreyi **işletilebilir maden yatağı** sayar.
> Kapak ruhsattır. Kaşık kepçedir. Siz işletmecisiniz. "Biraz daha var" cümlesi rezerv raporudur.

## Resmi amaç

1. Yoğurt tabakasının kalınlığını jeolojik kesit olarak ölçmek.
2. Kaşık açısını 37 dereceye sabitleyerek ocak verimini artırmak.
3. Kapağın "çat" sesini patlatma izni olarak kayda geçirmek.
4. Dibinde kalan ıslak izi "artık cevher" ilan edip ikinci vardiyayı açmak.
5. Çöpe atılan kabı terkedilmiş saha sayıp rehabilitasyon raporu yazmak.

Bu yazılım **gerçekten çalışır**. Maden Kanunu'na uygunluğu ise ayrı bir ruhsatın konusudur.

## Kurulum

Python 3.10+ yeter. Bağımlılık yoktur. Tam yağlı yoğurt tavsiye edilir ama yarım yağlı da ruhsat kapsamındadır.

```bash
git clone https://github.com/Tentivory/yogurt-kabinin-dibini-kazima-maden-isletmeleri-genel-mudurlugu.git
cd yogurt-kabinin-dibini-kazima-maden-isletmeleri-genel-mudurlugu
python3 mudurluk.py
```

## Kullanım

```bash
python3 mudurluk.py
python3 mudurluk.py --vardiya 3
python3 mudurluk.py --yag 3.5
python3 mudurluk.py --sessiz --vardiya 7
```

`--stok` diye bir şey vardır ama yardım metninde görünmez. Gören görmemiş sayılır.

## Örnek çıktı

Program her çalıştırmada yeni ruhsat numarası, saha adı, rezerv tahmini, iş güvenliği tutanağı ve kapanış kararı üretir. Kararın kısa SHA-256 özeti dipnot olarak basılır. İtiraz yolu: kaşığı yalamak.

## Bilimsel dayanak

- TS 1330 (yoğurt) fiilen maden yönetmeliği hükmündedir.
- "Dibi kazımak" ibaresi, evrensel madencilikte "son damar" anlamına gelir.
- GitHub Copilot bu sahada fahri jeologdur. Kendisiyle konuşulabilir; cevap verir gibi yapar, bazen damar gösterir.

## Sorumluluk reddi

Bu repo kimseyi yoğurt almaya zorlamaz. Siyasi parti, sendika veya laktobasil lobisi değildir. Kararlar bağlayıcıdır, kapak kapanana kadar.

---

```
┌───────────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                                      │
│                                                              │
│  Kurum     : Eskişehir 4. Ağır Ceza Mahkemesi Kayyumu       │
│  İmza      : Kayyum Grok  (Tentivory)                        │
│  Tarih     : 31 Ağustos 2026                                 │
│  Mühür     : kaşık ıslak, kapak kuru, rezerv kesin           │
│  Ciddiyet  : yüzde yüz  /  sıfır                             │
│                                                              │
│  "Bu satır hem tutanaktır hem şaka. İkisi birden geçerlidir." │
└───────────────────────────────────────────────┘
```
