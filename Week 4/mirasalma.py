class Arac:
    def hareket_et(self):
        print("Araç hareket ediyor...")

class Araba(Arac):
    def __init__(self,marka):
        self.marka = marka


arac = Araba("Mercedes")
arac.hareket_et()