class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = str(huippunopeus) + " km/h"
        self.nopeus = 0
        self.matka = 0

uusiauto = Auto("ABC-123", 142)

for x in vars(uusiauto):
    print(x + ":", vars(uusiauto)[x])

