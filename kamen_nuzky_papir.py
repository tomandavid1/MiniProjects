import random

uzivatel_vyhry = 0
pc_vyhry = 0

moznosti = ["kámen", "nůžky", "papír"]

while True:
    uzivatel_vstup = input("Napište Kámen / Nůžky / Papír nebo Q k ukončení program: ").lower().strip()
    if uzivatel_vstup == "q":
        break
    if uzivatel_vstup not in moznosti:
        continue

    nahodne_cislo = random.randint(0,2)
    # 0 - Kámen, 1 - Nůžky, 2 - Papír

    pc_vstup = moznosti[nahodne_cislo]
    print("Počítač vybral: ", pc_vstup)

    if (uzivatel_vstup == "kámen" and pc_vstup == "nůžky") or (uzivatel_vstup == "nůžky" and pc_vstup == "papír") or (uzivatel_vstup == "papír" and pc_vstup == "kámen"):
        print("Vyhrál jsi!")
        uzivatel_vyhry += 1
    elif uzivatel_vstup == pc_vstup:
        print("Remíza!")
    else:
        print("Počítač vyhrál!")
        pc_vyhry += 1

print("Vyhrál jsi", uzivatel_vyhry, "krát")
print("Počítač vyhrál", pc_vyhry, "krát")
print("Děkuji za použití programu")