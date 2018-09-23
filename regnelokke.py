# Tid: 1 time
# Et program som bruker en while-løkke for å lese inn tall fra brukeren,
# helt brukeren taster 0. For hver gjennomkjøring legges tallene etter
# hverandre i en liste.
tall = 1
minListe = []
while tall > 0:
    tall = int(input("Tast inn et tall:"))
    minListe.append(tall)

# Skriver ut hele lista.
print(minListe)

# Skriver ut hvert element i lista.
for index in minListe:
    print(index)

# Summerer alle elementene i lista og skriver ut summen.
minSum = 0
for index in minListe:
    minSum = minSum + index
print("Sum:", minSum)

# Finner og skriver ut den minste verdien i lista.
minste = minListe[0]
for index in minListe:
    if index < minste:
        minste = index
print("Minste:", minste)

# Finner og skriver ut det størst elementet  lista.
storste = minListe[0]
for i in range(1, len(minListe)):
    if minListe[i] > storste:
        storst = minListe[i]
print("Største:", storste)
