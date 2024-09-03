import random

lukulista = []

def listasumma(lista):
    summaluku = 0

    for i in lista:
        summaluku += i

    return summaluku

for x in range(random.randint(4, 9)):
    lukulista.append(random.randint(1, 100))

print(lukulista)
print(listasumma(lukulista))