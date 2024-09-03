lukulista = []

while True:
    annettuluku = input("Anna luku listaan: ")

    if annettuluku == "":
        break
    else:
        lukulista.append(int(annettuluku))

lukulista.sort(reverse = True)

for x in range(5):
    print(lukulista[x])