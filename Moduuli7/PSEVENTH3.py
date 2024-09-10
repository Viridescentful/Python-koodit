lentoasemat = []

def uusiasema():
    icaokoodi = str(input("Anna ICAO koodi: "))[:4]
    asemannimi = str(input("Anna Aseman nimi:"))

    for x in lentoasemat:
        if x[0].upper() == icaokoodi or x[1].upper() == asemannimi:
            return

    lentoasemat.append({"ICAO" : icaokoodi.upper(), "Asema" : asemannimi.upper()})

def haeasema():
    icaokoodi = str(input("Anna ICAO koodi: "))[:4]

    for x in lentoasemat:
        #print(x)

        if x["ICAO"] == icaokoodi.upper():
            print("Lentoasema:", x["Asema"])

while True:
    komento = input("Haluatko lisätä uuden aseman, vai löytää aseman? (Lisää tai Hae) ")

    if komento.lower() == "lisää":
        uusiasema()
    elif komento.lower() == "hae":
        haeasema()
    elif komento == "":
        break

