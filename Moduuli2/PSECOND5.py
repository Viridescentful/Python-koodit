luotipaino = 13.3
naulapaino = luotipaino * 32
leviskäpaino = naulapaino * 20

leviskät = float(input("Anna Leviskät: "))
naulat = float(input("Anna Leviskät: "))
luodit = float(input("Anna Leviskät: "))

yhteispainog = round(leviskät * leviskäpaino + naulat * naulapaino + luodit * luotipaino, 2)
yhteispainokg = round(yhteispainog / 1000, 2)

print("Massa nykymittojen mukaan: \n", yhteispainokg, " Kilogrammaa ja ", yhteispainog, " Grammaa")