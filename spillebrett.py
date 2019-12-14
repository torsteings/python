from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = self.lagListe() # Returnerer rutenett
        self._generasjonsnummer = 0
        self._generer() # Returnerer nulte generasjon

    # Metode for å skrive ut rutenettet med cellens status.
    def tegnBrett(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                print(self._nulte[i][j].hentStatusTegn(), end=" ")
            print()

    # Metode for å oppdatere rutenettet basert på antall levende naboer.
    def oppdatering(self):
        doede = []
        levende = []
        rutenett = self._nulte
        for i in range(self._rader):
            for j in range(self._kolonner):
                rad = i
                kol = j
                naboer = self.finnNabo(rad, kol)
                countLevende = 0
                countDoed = 0
                for nabo in naboer:
                    sjekkLevende = nabo.erLevende()
                    if sjekkLevende:
                        countLevende = countLevende + 1
                    else:
                        countDoed = countDoed + 1
                if countLevende < 2:
                    levende.append(nabo)
                elif countLevende == 2 or countLevende == 3:
                    doede.append(nabo)
                elif countLevende > 3:
                    levende.append(nabo)
                elif countDoed == 3:
                    doede.append(nabo)
        for celle in doede:
            blirLevende = celle.settLevende()
        for celle in levende:
            blirDoede = celle.settDoed()
        tegnLevende = self.tegnBrett()

    # Metode for å finne antall levende celler i rutenettet.
    def finnAntallLevende(self):
        antallLevende = 0
        for i in range(self._rader):
            for j in range(self._kolonner):
                if self._nulte[i][j].erLevende():
                    antallLevende = antallLevende + 1
        print("Antall levende celler:", antallLevende)

    # Metode for å fylle rutenettet med nulte generasjon celleobjekter.
    def _generer(self):
        self._nulte = self._rutenett
        for i in range(self._rader):
            for j in range(self._kolonner):
                tilfeldigTall = randint(0, 2)
                if tilfeldigTall == 0:
                    self._nulte[i][j].settLevende()
                else:
                    self._nulte[i][j]
        return self._nulte

    # Metode som tar inn to koordinator og returnerer en liste med cellens naboer.
    def finnNabo(self, rad, kol):
        naboer = []
        for i in range(rad - 1, rad + 2):
            if i >= 0 and i < self._rader:
                for j in range(kol - 1, kol + 2):
                    if not(i == rad and j == kol):
                        if j >= 0 and j < self._kolonner:
                            a = self._nulte[i][j]
                            naboer.append(a)
        return naboer

    # Metode som oppretter et rutenett i form av en todimensjonal (nøstet) liste.
    def lagListe(self):
        self._rutenett = []
        for i in range(self._rader):
            b = []
            for j in range(self._kolonner):
                nyCelle = Celle()
                b.append(nyCelle)
            self._rutenett.append(b)
        return self._rutenett

    # Metode som oppdaterer instansvariablen self._generasjonsnummer.
    def generasjonsnummer(self):
        self._generasjonsnummer = self._generasjonsnummer + 1
        print("Generasjon:", self._generasjonsnummer)
