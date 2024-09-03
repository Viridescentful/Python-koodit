import random

def noppaluku(tahkot):
    return random.randint(1, tahkot)

tahkojenmäärä = int(input("Anna nopan tahkojen määrä: "))

while True:
    saatuluku = noppaluku(tahkojenmäärä)
    print(saatuluku)

    if saatuluku == tahkojenmäärä:
        break