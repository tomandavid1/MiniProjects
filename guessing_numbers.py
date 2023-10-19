import random

while True:
    try:
        horni_hranice = int(input("Napište celé kladné číslo: ").strip())
        if horni_hranice > 0:
            break
        else:
            print("Vstup musí být větší než 0!")
    except:
        print("Neplatný vstup!")

nahodne_cislo = random.randint(1,horni_hranice)
