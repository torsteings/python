# Tid: 1 time.
# Programmet lager en funksjon som tar inn to tall og adderer disse.
def adder(tall1, tall2):
    return tall1 + tall2
print(adder(1,1))

# Programmet oppretter en funksjon som tar inn to parametere, minTekst og
# minBokstav fra brukeren.
# Undersøker deretter om minBokstav finnes i minTekst.
# Tilslutt skriver programmet ut antall forekomster av av minBokstav.

# Tar inn to parametere fra brukeren og lagrer disse i hver sin variabel.
minTekst  = input("Skriv inn en tekststreng:")
minBokstav = input("Skriv inn en bokstav:")

# Skriver en funksjon tellForekomst som tar inn de to parameterene.
def tellForekomst(minTekst, minBokstav):
    # Oppretter en tellevariabel for å lagre antall forekomster av minBokstav.
    teller = 0
    # Lager en for-løkke som går like lenge som lengden på minTekst.
    for i in minTekst:
        # Sjekker om minBokstav forekommer i minTekst.
        if i == minBokstav:
            # Hvis minBokstav forekommer i minTekst øker teller med 1.
            teller = teller + 1
    # Skriver ut antall forekomster av minBokstav.
    print(teller)

# Kaller funksjonen.
tellForekomst(minTekst, minBokstav)
