# Et program som lar brukeren legge planer for en reise.

# Lager en tom liste hvor brukeren kan fylle inn 5 reisemål.
steder = []
for tall in range(1,6):
    elem = input("Skriv inn et reisemål:")
    steder.append(elem)

# Lager en tom liste hvor brukeren kan fylle inn 5 klesplagg.
klesplagg = []
for tall in range(1,6):
    elem = input("Skriv inn et klesplagg:")
    klesplagg.append(elem)

# Lager en tom liste hvor brukeren kan fylle inn 5 avreisedatoer.
avreisedatoer = []
for tall in range(1,6):
    elem = input("Skriv inn en avreisedato:")
    avreisedatoer.append(elem)

# Skriver ut de tre listene.
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)
for i in range(0, len(reiseplan)):
    print(reiseplan[i])

# Lar brukeren oppgi en plass i reiseplan og skriver ut elementet på
# den oppgitte plssen.
i1 = int(input("Skriv inn et tall mellom 0 og 2:"))
i2 = int(input("Skriv inn et tall mellom 0 og 4:"))
# Sjekker om input er gyldig.
if i1 >= 0 and i1 < 3 and i2 >=0 and i2 < 5:
    # Skriver ut elementet på plassen som brukeren har valgt.
    print(reiseplan[i1][i2])
else:
    print("Ugyldig input!")
