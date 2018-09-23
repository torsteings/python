# oppretter en ordbok med nøkkel- og innholdsverdier som
# beskriver navn og pris på varer i en butikk.
# varer er nøkkelverdi.
# melk, brød, osv. er innholdsverdier.
varer = {
        "melk": 14.90,
        "brød": 24.90,
        "yoghurt": 12.90,
        "pizza": 39.90
        }
print(varer)

# leser inn to varenavn og priser fra brukeren og legger disse til i ordboken
def nyVare():
    print("Legg inn varenavn og pris:")
    vareNavn = input()
    varePris = float(input())
    varer[vareNavn] = varePris

nyVare()
print(varer)
