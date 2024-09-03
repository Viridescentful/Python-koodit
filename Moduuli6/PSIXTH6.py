import math

def pizzaneliöhinta(halkaisija, hinta):
    pintala = math.pi * (float(halkaisija) / 2) * (float(halkaisija) / 2)

    return float(hinta) / pintala

pizza1, hinta1 = input("Anna ensimmäisen pizzan halkaisija ja hinta: ").split()
pizza2, hinta2 = input("Anna toisen pizzan halkaisija ja hinta: ").split()

yksikkohinta1 = pizzaneliöhinta(pizza1, hinta1)
yksikkohinta2 = pizzaneliöhinta(pizza2, hinta2)



if yksikkohinta1 > yksikkohinta2:
    print("Toisen pizzan yksikköhinta on pienempi, eli toinen pizza on ensimmäiseen pizzaan verrattuna rahansa arvoinen!")
else:
    print("Ensimmäinen pizzan yksikköhinta on pienempi, eli ensimmäinen pizza on toiseen pizzaan verrattuna rahansa arvoinen!")

