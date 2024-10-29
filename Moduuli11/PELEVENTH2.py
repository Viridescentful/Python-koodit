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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = kapasiteetti

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Nopeus: {self.rekisteritunnus}")
        print(f"Matka: {self.matka}")
        print(f"Kapasiteetti: {self.akkukapasiteetti} kWh")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankkikapasiteetti = kapasiteetti

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Nopeus: {self.rekisteritunnus}")
        print(f"Matka: {self.matka}")
        print(f"Kapasiteetti: {self.tankkikapasiteetti} l")


autot = []

autot.append(Sähköauto("ABC-15", 180, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))

for auto in autot:
    auto.kiihdytä(random.randint(60, 100))

for auto in autot:
    auto.kulje(3)
    auto.tulosta_tiedot()








