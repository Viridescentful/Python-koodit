class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = 0

    def kerros_ylös(self):
        if self.kerros + 1 > self.ylinkerros:
            self.kerros = self.ylinkerros
        else:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros - 1 < self.alinkerros:
            self.kerros = self.alinkerros
        else:
            self.kerros -= 1

    def siirry_kerrokseen(self, haluttavakerros):
        if haluttavakerros > self.kerros:
           for i in range(haluttavakerros - self.kerros):
               self.kerros_ylös()
               print(self.kerros)

               if self.kerros >= self.ylinkerros:
                   break
        elif haluttavakerros < self.kerros:
            for i in range(self.kerros - haluttavakerros):
                self.kerros_alas()
                print(self.kerros)

                if self.kerros <= self.alinkerros:
                    break
        else:
            print("Olet jo kerroksessa!")

class Talo:
    def __init__(self, alinkerros, ylinkerros, hissit):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissit = []

        for i in range(hissit):
            self.hissit.append(Hissi(alinkerros, ylinkerros))

    def aja_hissiä(self, hissinumero, kerros):
        if self.hissit[hissinumero - 1]:
            self.hissit[hissinumero - 1].siirry_kerrokseen(kerros)
        else:
            print("Hissiä ei ole!")

    def palohälytys(self):
        for i in self.hissit:
           i.siirry_kerrokseen(self.alinkerros)

uusitalo = Talo(-4, 10, 7)
uusitalo.aja_hissiä(1, 7)
uusitalo.palohälytys()