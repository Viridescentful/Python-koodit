vuodenaikatable = ((2, "Talvi"), (5, "Kevät"), (8, "Kesä"), (11, "Syksy"), (12, "Talvi"))
import math
kuukausi = int(input("Anna kuukausi luku: "))

for x in vuodenaikatable:
    if x[0] >= kuukausi:
        print(x[1])
        break

math.floor