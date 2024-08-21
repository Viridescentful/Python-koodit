import math
import random

ensimmäinenkoodi = ""
toinenkoodi = ""

for x in range(3):
    ensimmäinenkoodi = ensimmäinenkoodi + str(random.randint(0, 9))

for x in range(4):
    toinenkoodi = ensimmäinenkoodi + str(random.randint(1, 6))

print("Ensimmäinen numerolukkon koodi: ", ensimmäinenkoodi, "\nToinen numerolukkon koodi: ", toinenkoodi)