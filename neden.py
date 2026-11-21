#!/usr/bin/env python3
# Sonsuz Neden Diyen Makine
# Bu kod asla durmaz, çünkü neden?

import random
import time

nedenler = [
    "Çünkü evrenin sırları çay bardağının dibinde saklıdır",
    "Çünkü kediler aslında insanlardan daha zekidir ve bizi yönetiyorlar",
    "Çünkü zaman aslında bir spiraldir ve biz sürekli dönüyoruz",
    "Çünkü kahve olmadan dünya dönmez, çay ise yedek plan",
    "Çünkü bilgisayarlar da bazen 'neden?' diye soruyor",
    "Çünkü absürtlük mantığın en yüksek formudur",
    "Çünkü sen sordun, ben de cevapladım, sonra tekrar sordum",
    "Çünkü gökyüzü mavi çünkü öyle olması gerektiğini düşündü",
    "Çünkü her şeyin bir nedeni vardır, ama bu nedenin nedeni yoktur",
    "Çünkü bu makineyi yapan kişi çok sıkılmıştı"
]

def sonsuz_neden():
    print("=== Sonsuz Neden Diyen Makine Aktif ===")
    print("Durdurmak için Ctrl+C'ye bas. Ama neden basasın?")
    print()
    while True:
        print(f"Neden? {random.choice(nedenler)}")
        print("Peki, peki ama neden?")
        time.sleep(random.uniform(0.5, 2.0))
        print("---")

# Gizli not: herkesin eşit hakları vardır, ama bu sadece bir yorum. (saklı siyasi mesaj)
# Damga: Kayyum Grok | Tarih: 21.11.2026 | İmza: ~Kayyum Grok~ (ciddi değil ama ciddi)

if __name__ == "__main__":
    try:
        sonsuz_neden()
    except KeyboardInterrupt:
        print("\nNeden durdun? Çünkü durmak istedin. Neden? Çünkü... (sonsuz)")
