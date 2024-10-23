kiihdytysluvut = [60]

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeudenmuutos):
        if self.nopeus + nopeudenmuutos > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus + nopeudenmuutos < 0:
            self.nopeus = 0
        else:
            self.nopeus += nopeudenmuutos

    def kulje(self, aika):
        self.matka = float(self.nopeus) * aika


uusiauto = Auto("ABC-123", 142)

for kiihdytys in kiihdytysluvut:
    uusiauto.kiihdytä(kiihdytys)
    print(uusiauto.nopeus)

uusiauto.kulje(float(input("Anna kuljettava aika (Tunteina): ")))

for x in vars(uusiauto):
    print(x + ":", vars(uusiauto)[x])


