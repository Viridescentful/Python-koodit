import random

def noppaluku():
    return random.randint(1, 6)

while True:
    saatuluku = noppaluku()
    print(saatuluku)

    if saatuluku == 6:
        break