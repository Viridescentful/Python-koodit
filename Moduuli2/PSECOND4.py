first, second, third = input("Anna kolme lukua (Erota välillä): ").split()

firstint = int(first)
secondint = int(second)
thirdint = int(third)

summa = firstint + secondint + thirdint
erotus = firstint - secondint - thirdint
keskiarvo = (firstint + secondint + thirdint) / 3

print("Lukujen Summa on: ", summa, ", Erotus on: ", erotus, "Ja Keskiarvo, ", keskiarvo)