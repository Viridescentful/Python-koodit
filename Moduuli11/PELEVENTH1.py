class Julkaisu:

    def __init__(self, julkaisunimi):
        self.nimi = julkaisunimi


class Kirja(Julkaisu):

    def __init__(self, julkaisunimi, kirjoittaja, sivumäärä):
        super().__init__(julkaisunimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}, Kirjoitaaja: {self.kirjoittaja}, Sivujenmäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, julkaisunimi, päätoimittaja):
        super().__init__(julkaisunimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}, Päätoimittaja: {self.päätoimittaja}")


uusilehti = Lehti("Aku Ankka", "Aki Hyyppä")
uusikirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

uusilehti.tulosta_tiedot()
uusikirja.tulosta_tiedot()