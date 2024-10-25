from xmlrpc.client import boolean
import math
import random
import time

matkasaavutettu = 0

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
        self.matka += float(self.nopeus) * aika

class Kilpailu:
    def __init__(self, kilpailunnimi, kilpailevatautot, kilpailunkilometrit):
        self.kilpailunnimi = kilpailunnimi
        self.kilpailevatautot = kilpailevatautot
        self.kilpailunkilometrit = kilpailunkilometrit

    def tunti_kuluu(self):
        for auto in kilpailevatautot:
            auto.kiihdytä(random.randint(-10, 15))

        for auto in kilpailevatautot:
            auto.kulje(1.0)

    def tulosta_tilanne(self):
        for auto in kilpailevatautot:
            for x in vars(auto):
                if x == "rekisteritunnus":
                    print(vars(auto)[x])
                elif x == "matka":
                    print(x + ":", vars(auto)[x], "km")
                else:
                    print(x + ":", vars(auto)[x], "km/h")

            print("---")

    def kilpailu_ohi(self):
        onkoohi = False

        for auto in kilpailevatautot:
            if auto.matka >= self.kilpailunkilometrit:
                onkoohi = True

        return onkoohi



kilpailevatautot = []
tuntienmäärä = 0

for auto in range(10):
    kilpailevatautot.append(Auto("ABC-" + str(auto + 1), random.randint(100, 200)))

uusikilpailu = Kilpailu("Suuri romuralli", kilpailevatautot, 8000)
uusikilpailu.tulosta_tilanne()

while True:
    uusikilpailu.tunti_kuluu()
    tuntienmäärä += 1

    if tuntienmäärä >= 10:
        print("")
        print("10 TUNTIA KULUNUT")
        print("")

        uusikilpailu.tulosta_tilanne()
        tuntienmäärä = 0

    if uusikilpailu.kilpailu_ohi() == True:
        break

print("")
print("KILPAILU ON OHI!")
print("")

uusikilpailu.tulosta_tilanne()





