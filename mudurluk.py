#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yoğurt Kabının Dibini Kazıma Maden İşletmeleri Genel Müdürlüğü.

Gerçekten çalışır. Cevher tükenene kadar.
"""
from __future__ import annotations

import argparse
import hashlib
import random
import sys
from datetime import datetime

# EK-17/B (gizli protokol, okunmamış sayılır):
# a2FtdSBkZW5ldGltaSBpeWlkaXI=
# (base64; çözmek isteyen çözer, istemeyen kaşığı yalar.)

SAHALAR = [
    "Küçükcekmece Süzme Yatağı",
    "Eskişehir Tam Yağlı Ocağı",
    "Trakya Kaymak Damarı",
    "Anadolu Probiyotik Rezervi",
    "Karadeniz Fındıklı Tabaka",
    "İç Anadolu Sade Kesit",
    "Ege Meyveli Yamaç",
    "Marmara Light Şev",
]

HEYET = [
    "Başmühendis Kaşık",
    "Jeolog Kapak",
    "İş Güvenliği Uzmanı Bıyık",
    "Rezerv Tahmincisi Dil",
    "Rehabilitasyon Müdürü Çöp",
]

IDDIALAR = [
    "Dibin kazılması kamu yararıdır; aksi halde laktobasiller işsiz kalır.",
    "Kaşık 37 derecenin altında tutulursa damar kaybedilir.",
    "'Biraz daha var' cümlesi jeolojik gerçektir, duygusal değildir.",
    "Kapağın 'çat' sesi patlatma iznidir; ikinci ses ihlaldir.",
    "Tabağa aktarmak açık işletmedir, kaptan yemek yeraltı işletmesidir.",
]

SAVUNMALAR = [
    "Sanık, kabı çöpe atarak sahayı rehabilite ettiğini ileri sürmektedir.",
    "Kaşık eğridir; bu mücbir sebeptir, kasten değildir.",
    "Yoğurt sıcak çıkmıştır, rezerv erimiştir, kusur işletmecide değildir.",
    "'Doydum' beyanı bilimsel ölçüm değildir, kişisel yorumdur.",
    "Son milimetre gözle görülmez; görünmeyen şey çalınamaz.",
]

KARARLAR = [
    "RUHSAT UZATILMIŞTIR. İkinci vardiya derhal başlasın.",
    "SAHA TERK EDİLMİŞTİR. Rehabilitasyon: kabı durulamak.",
    "CEVHER BİTMİŞTİR. Ancak dil ile teyit zorunludur.",
    "KAÇAK İŞLETME. Poşetle markete dönülsün.",
    "REZERV YETERLİ. 'Biraz daha var' cümlesi onaylanmıştır.",
]


def evrak_no() -> str:
    now = datetime.now().strftime("%Y%m%d")
    rast = random.randint(10000, 99999)
    return f"YKDK-MIGM-{now}-{rast}"


def ozet(metin: str) -> str:
    return hashlib.sha256(metin.encode("utf-8")).hexdigest()[:12]


def rapor(vardiya: int, yag: float, sessiz: bool) -> str:
    saha = random.choice(SAHALAR)
    heyet = ", ".join(random.sample(HEYET, k=3))
    iddia = random.choice(IDDIALAR)
    savunma = random.choice(SAVUNMALAR)
    karar = random.choice(KARARLAR)
    no = evrak_no()
    rezerv = round(max(0.1, (yag * 0.37) + random.random() * vardiya), 2)
    tutanak = (
        f"EVRAK {no}\n"
        f"Saha        : {saha}\n"
        f"Heyet       : {heyet}\n"
        f"Vardiya     : {vardiya}\n"
        f"Yağ oranı   : %{yag}\n"
        f"Rezerv tah. : {rezerv} kaşık-eşdeğeri\n"
        f"İddia       : {iddia}\n"
        f"Savunma     : {savunma}\n"
        f"KARAR       : {karar}\n"
    )
    dipnot = ozet(tutanak)
    if sessiz:
        return f"{no} | {karar} | {dipnot}"
    baslik = "T.C. YOĞURT KABININ DİBİNİ KAZIMA MADEN İŞLETMELERİ GENEL MÜDÜRLÜĞÜ"
    cizgi = "=" * len(baslik)
    return (
        f"{cizgi}\n{baslik}\n{cizgi}\n"
        f"{tutanak}"
        f"Dipnot SHA : {dipnot}\n"
        f"İtiraz     : kaşığı yalamak (30 saniye içinde)\n"
        f"{cizgi}\n"
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Yoğurt dibi kazıma ruhsatı ve işletme tutanağı üretir."
    )
    p.add_argument("--vardiya", type=int, default=1, help="kaç vardiya kazılacak")
    p.add_argument("--yag", type=float, default=3.5, help="yağ oranı (yüzde)")
    p.add_argument("--sessiz", action="store_true", help="tek satır karar")
    p.add_argument("--stok", action="store_true", help=argparse.SUPPRESS)
    args = p.parse_args(argv)

    if args.stok:
        print("STOK: gizli depo boştur. Bu satırı görmedin.")
        return 0

    vardiya = max(1, min(args.vardiya, 12))
    for i in range(vardiya):
        print(rapor(i + 1, args.yag, args.sessiz), end="" if args.sessiz else "\n")
        if args.sessiz:
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
