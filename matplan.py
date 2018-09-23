# lager en ordbok hvor hver nøkkelverdi er navnet til en beboer,
# og innholdsverdien er en liste med tre måltider.
beboere = { "Kari Nordmann": ["brød", "egg","pølser"],
            "Ola Nordmann": ["brød", "egg", "lompe"],
            "Nord Olakarimann": ["kaffe", "egg", "lompe"] }

# lager en prosedyre hvor brukeren kan skrive navnet til en beboer i terminalen
# og få skrevet ut matplanen til den beboeren. Den skriver også ut
# en melding dersom beboeren ikke er registrert
def matplan():
    print("Skriv inn navnet til en beboer:")
    navn = input()
    if navn in beboere:
        maaltider = beboere[navn]
        print(maaltider)
    else:
        print("Beboeren er ikke registrert.")

matplan()
