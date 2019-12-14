class Celle:
# Konstruktør
    def __init__(self):
        self._status = "doed"

    # Endre status
    def settDoed(self):
        self._status = "doed"
        return self._status

    def settLevende(self):
        self._status = "levende"
        return self._status

    # Hente status
    def erLevende(self):
        if self._status == "levende":
            return True
        else:
            return False

    def hentStatusTegn(self):
        if self._status == "levende":
            #print("O")
            return "O"
        else:
            return "."


#nyCelle = Celle()
#nyCelle.settLevende()
#nyCelle.hentStatusTegn()
