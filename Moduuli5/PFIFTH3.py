
numero = input("Anna numero: ")
alkuluku = True


for i in range(2, int(numero)):
    if int(numero) % i == 0 :
        alkuluku = False
        break


if alkuluku:
   print("Numero on alkuluku")
else:
   print("Numero ei ole alkuluku")