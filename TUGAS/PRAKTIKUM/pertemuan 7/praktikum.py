import math
''' APLIKASI 1 '''
class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_volume(self):
        return self.sisi ** 3

    def hitung_luas_permukaan(self):
        return 6 * (self.sisi ** 2)

    @classmethod
    def dari_input(cls):
        sisi = float(input("Masukkan panjang sisi kubus: "))
        return cls(sisi)

    def tampilkan_output(self):
        print(f"Volume kubus:  {self.hitung_volume():.2f}")
        print(f"Luas permukaan kubus:  {self.hitung_luas_permukaan():.2f}")

kubus = Kubus.dari_input()
kubus.tampilkan_output()

''' APLIKASI 2 '''


class Silinder:
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def hitung_volume(self):
        return math.pi * (self.jari_jari ** 2) * self.tinggi

    def hitung_luas_permukaan(self):
        luas_alas = math.pi * (self.jari_jari ** 2)
        luas_selimut = 2 * math.pi * self.jari_jari * self.tinggi
        return 2 * luas_alas + luas_selimut

    @classmethod
    def dari_input(cls):
        jari_jari = float(input("Masukkan jari-jari silinder: "))
        tinggi = float(input("Masukkan tinggi silinder: "))
        return cls(jari_jari, tinggi)

    def tampilkan_output(self):
        print(f"Volume silinder: { self.hitung_volume():.2f}")
        print(f"Luas permukaan silinder: { self.hitung_luas_permukaan():.2f}")

silinder = Silinder.dari_input()
silinder.tampilkan_output()


''' APLIKASI 3 '''


class Bola:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_volume(self):
        return (4/3) * math.pi * (self.jari_jari ** 3)

    def hitung_luas_permukaan(self):
        return 4 * math.pi * (self.jari_jari ** 2)

    @classmethod
    def dari_input(cls):
        jari_jari = float(input("Masukkan jari-jari bola: "))
        return cls(jari_jari)

    def tampilkan_output(self):
        print(f"Volume bola: {self.hitung_volume():.2f}")
        print(f"Luas permukaan bola: {self.hitung_luas_permukaan():.2f}")

bola = Bola.dari_input()
bola.tampilkan_output()
