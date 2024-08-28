käyttäjätunnus = "Kuhanalainen"
käyttäjäsalasana = "Kuhaonparas123"

yritykset = 0
tunnusoikein = False

while True:
    if yritykset > 4:
        break

    käyttäjätunnusinput = input("Anna käyttäjän tunnus: ")
    käyttäjäsalasanainput = input("Anna käyttäjän salasana: ")

    if käyttäjätunnusinput == käyttäjätunnus and käyttäjäsalasanainput == käyttäjäsalasana:
        tunnusoikein = True
        break
    else:
        yritykset += 1

        if käyttäjätunnusinput != käyttäjätunnus or käyttäjäsalasanainput != käyttäjäsalasana:
           print("Käyttäjä tunnus tai salasana on väärin! Syötä käyttäjä tunnus ja salasana uudelleen.")


if tunnusoikein:
    print("Tervetuloa!")
else:
    print("Pääsy evätty!")