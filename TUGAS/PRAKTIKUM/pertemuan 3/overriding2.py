class Mobil:
    def kecepatan(self):
        print("Mobil dapat berjalan dengan kecepatan maksimum 120 km/jam")

class MobilSport(Mobil):
    def kecepatan(self):
        print("Mobil sport dapat berjalan dengan kecepatan maksimum 300 km/jam")

class MobilTruk(Mobil):
    def kecepatan(self):
        print("Mobil truk dapat berjalan dengan kecepatan maksimum 80 km/jam")

mobil = Mobil()
mobil_sport = MobilSport()
mobil_truk = MobilTruk()

mobil.kecepatan()
mobil_sport.kecepatan()
mobil_truk.kecepatan()