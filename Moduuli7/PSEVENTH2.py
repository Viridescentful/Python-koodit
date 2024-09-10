nimitable = set()

while True:
    nimi = input("Anna nimi: ")

    if nimi == "":
        break

    if nimi in nimitable:
        print("Aiemmin syötetty nimi!")
    else:
        nimitable.add(nimi)
        print("Uusi nimi!")

for x in nimitable:
    print(x)