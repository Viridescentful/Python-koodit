import random

lukulista = []

def poistaparittomat(lista):
    parillinenlista = []

    for i in lista:
        if i % 2 == 0:
            parillinenlista.append(i)

    return parillinenlista

for x in range(random.randint(4, 9)):
    lukulista.append(random.randint(1, 100))

print(lukulista)
print(poistaparittomat(lukulista))