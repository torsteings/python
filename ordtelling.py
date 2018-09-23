# Tid: 3 timer.
# Dette programmet kan ta inn en setning fra brukeren og returnere
# antall ord i setningen, hvor mange ganger hvert ord forekommer og
# antall bokstaver i hvert ord.

# Lager en funksjon som finner antall bokstaver i ett enkelt ord.
def antallBokstaver(ord):
    # Returnerer lengden på argumentet (stringen) som tas inn.
    return len(ord)

# Lar brukeren skrive en valgfri setning.
str = input("Skriv en setning:\n")
# Oppretter en tom ordbok som senere skal ha plass til str.
ordbok = {}
# Lager en funksjon som tar inn setningen fra brukeren som argument og
# deler senere denne opp i en liste der hvert ord er separert med et komma.
def antallOrd(str):
    liste = str.split()
    print("Det er ", len(liste), " ord i setningen din.")
    # Sjekker om hvert ord i lista finnes i ordboka.
    # Hvis det finnes der fra før, økes innholdsverdien med 1.
    # Hvis det ikke finnes, lages det en ny nøkkelverdi med innholdsverdi 1.
    for ord in liste:
        if ord in ordbok:
            ordbok[ord] = ordbok[ord] + 1
        else:
            ordbok[ord] = 1
    for nokkel in ordbok:
        print("Ordet '" ,nokkel, "' forekommer", ordbok[nokkel],
        "ganger, og har", antallBokstaver(nokkel), "bokstaver.")

antallOrd(str)
