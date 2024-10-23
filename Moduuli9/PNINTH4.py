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

kilpailevatautot = []

for auto in range(10):
    kilpailevatautot.append(Auto("ABC-" + str(auto + 1), random.randint(100, 200)))

for auto in kilpailevatautot:
    for x in vars(auto):
        print(x + ":", vars(auto)[x])

    print("---")


while True:
    for auto in kilpailevatautot:
        auto.kiihdytä(random.randint(-10, 15))

    for auto in kilpailevatautot:
        auto.kulje(1.0)
        if auto.matka >= 10000:
            matkasaavutettu = 1

    if matkasaavutettu == 1:
        break

    #time.sleep(0.1)

print("")
print("FIN")
print("")

for auto in kilpailevatautot:
    for x in vars(auto):
        print(x + ":", vars(auto)[x])

    print("---")