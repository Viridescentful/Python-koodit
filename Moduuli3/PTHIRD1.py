#Senttimetreinä
kuhanminpituus = 38

kuhanpituus = int(input("Anna kalastetun kuhan pituus (cm): "))

if kuhanpituus > kuhanminpituus:
    print("Saalis on kuhainen")
else:
    print("Kuha on liian pieni, palauta kuha takaisin järveen. Kuhan pituudesta puuttuu", kuhanminpituus-kuhanpituus, "cm")