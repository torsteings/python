from spillebrett import Spillebrett

def main():
    rader = int(input("Skriv inn antall rader:"))
    kolonner = int(input("Skriv inn antall kolonner:"))
    nyttSpillebrett = Spillebrett(rader, kolonner)
    nyttSpillebrett.tegnBrett()
    print()
    print()

    fortsette = True
    while fortsette:
        nyttSpillebrett.oppdatering()
        nyttSpillebrett.generasjonsnummer()
        nyttSpillebrett.finnAntallLevende()
        fortsette = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte:")


main()
