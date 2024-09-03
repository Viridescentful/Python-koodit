def galmuutos(galmäärä):
    litramuutos = galmäärä * 3.785

    return litramuutos

while True:
    galmäärä = float(input("Anna gallomäärä: "))

    if galmäärä < 0:
        break
    litramuutos = round(galmuutos(galmäärä), 0)

    print(litramuutos)