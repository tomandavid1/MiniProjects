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
pokusy = 0
while True:
    try:
        uzivatelsky_vstup = int(input("Uhádněte číslo od 1 do " + str(horni_hranice) + ": ").strip())
    except:
        print("Neplatný vstup!")
        continue
    pokusy += 1
    if uzivatelsky_vstup == nahodne_cislo:
        print("Správná odpověď!\nCelkový počet pokusů:", pokusy)
        break
    elif uzivatelsky_vstup > nahodne_cislo:
        print("Zkuste menší číslo")
    else:
        print("Zkuste větší číslo")