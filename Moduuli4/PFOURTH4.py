import random

tietokoneenluku = random.randint(1, 10)

while True:
    käyttäjännumero = int(input("Arvaa minun satunnainen luku (1-10): "))

    if käyttäjännumero == tietokoneenluku:
        print("HUIJARI!, sait lukuni oikein!")
        break
    else:
        if käyttäjännumero > tietokoneenluku:
            print("HAH, liian suuri luku!")
        if käyttäjännumero < tietokoneenluku:
            print("HEH, liian pieni luku!")