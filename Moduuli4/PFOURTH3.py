numerotable = []

while True:
    uusinumero = input("Anna numero tai jätätyhjäksi: ")

    if uusinumero == "":
        break
    else:
        numerotable.append(int(uusinumero))

if len(numerotable) > 0:
    numerotable.sort()

    ##print(numerotable)

    print("Listatuiden numeroiden suurin arvo on:", numerotable[0])
    print("Listatuiden numeroiden pienin arvo on:", numerotable[len(numerotable)-1])