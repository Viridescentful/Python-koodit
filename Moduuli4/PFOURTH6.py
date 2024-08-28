import random

pisteidenmäärä = int(input("Anna pisteiden määrä: "))
pisteitäympyrässä = 0

for i in range(pisteidenmäärä):
    x = random.uniform(1, -1)
    y = random.uniform(1, -1)

    if y * y + x * x < 1:
        pisteitäympyrässä += 1

piilikiarvo = 4 * pisteitäympyrässä / pisteidenmäärä

print("Piin likiarvo on:", piilikiarvo)
