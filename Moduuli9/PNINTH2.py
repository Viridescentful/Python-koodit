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

uusiauto = Auto("ABC-123", 142)

kiihdytysluvut = [30, 70, 50, -200]

for x in vars(uusiauto):
    print(x + ":", vars(uusiauto)[x])

for kiihdytys in kiihdytysluvut:
    uusiauto.kiihdytä(kiihdytys)
    print(uusiauto.nopeus)
