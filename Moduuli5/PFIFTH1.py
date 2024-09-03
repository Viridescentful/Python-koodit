import random

noppasumma = 0
arpakuutiomäärä = int(input("Anna arpakuutioiden määrä: "))

for i in range(arpakuutiomäärä):
    noppasumma += random.randint(1, 6)

print("Arpakuutioiden summa on", noppasumma)