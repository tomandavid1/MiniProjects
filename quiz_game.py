print("Jednoduchý kvíz napsaný v Pythonu!")

otazky = [
    "Pro jaký komponent se používá zkratka CPU? ",
    "Pro jaký komponent se používá zkratka GPU? ",
    "Kolik má kočka nohou? ",
    "Jaké domácí zvíře štěká? "
]
odpovedi = [
    "procesor",
    "grafická karta",
    "4",
    "pes"
]

score = 0

if len(otazky) != len(odpovedi):
    print("Nesedí počet otázek a odpovědí v systému!")
    quit()

playing = input("Chcete hrát? (ano/ne) ").lower().strip()

if playing != "ano":
    quit()

print("Dobře! Jdeme na to :)")

for x in range(len(otazky)):
    answer = input(otazky[x]).lower().strip()
    if answer == odpovedi[x]:
        print("Správná odpověď!")
        score += 1
    else:
        print("Špatná odpověď")

print("Celkové vaše skóre je " + str(int(100/len(otazky)*score)) + "%. (" + str(score) + "/" + str(len(otazky)) + ")")