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
        elif haluttavakerros < self.kerros:

            for i in range(self.kerros - haluttavakerros):
                self.kerros_alas()
                print(self.kerros)
        else:
            print("Olet jo kerroksessa!")

uusihissi = Hissi(-4, 10)

uusihissi.siirry_kerrokseen(5)
