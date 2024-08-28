sukupuoli, hemogobliiniarvoinput = input("Anna sukupuoli ja hemogobliiniarvo (Erota välillä): ").split()

hemogobliiniarvo = int(hemogobliiniarvoinput)

mminarvo = 134
mmaxarvo = 195

fminarvo = 117
fmaxarvo = 175

alhainen = "Hemogobliiniarvo on Alhainen"
korkea = "Hemogobliiniarvo on Korkea"
normaali = "Hemogobliiniarvo on Normaali"

if sukupuoli.lower() == "mies":
    if mmaxarvo > hemogobliiniarvo > mminarvo:
        print(normaali)
    else:
        if mminarvo > hemogobliiniarvo:
            print(alhainen)
        if mmaxarvo < hemogobliiniarvo:
            print(korkea)

elif sukupuoli.lower() == "nainen":
    if fmaxarvo > hemogobliiniarvo > fminarvo:
        print(normaali)
    else:
        if fminarvo > hemogobliiniarvo:
            print(alhainen)
        if fmaxarvo < hemogobliiniarvo:
            print(korkea)
else:
    print("Who are you?")