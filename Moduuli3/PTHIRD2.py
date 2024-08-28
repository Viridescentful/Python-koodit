
LUX = "LUX on parvekkeellinen hytti yläkannella"
A = "A on ikkunallinen hytti autokannen yläpuolella",
B = "B on ikkunaton hytti autokannen yläpuolella",
C = "C on ikkunaton hytti autokannen alapuolella"

hyttiinput = input("Anna hyttiluokka (LUX, A, B, C): ")

if hyttiinput == "LUX":
    print(LUX)
elif hyttiinput == "A":
    print(A)
elif hyttiinput == "B":
    print(B)
elif hyttiinput == "C":
    print(C)
else:
    print("Virheellinen hyttiluokka")





