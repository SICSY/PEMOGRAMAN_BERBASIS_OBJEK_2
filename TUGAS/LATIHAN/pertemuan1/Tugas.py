'''
nama = Muhammad Hilman Humaini 
Nim = 21051031
Kelas = Reguler 1
Matakuliah Pbo 2
Semester = 4
'''
import os
os.system("cls")

print('soal 1 =')
class Mobil:
    def __init__(self, merek,warna):
        self.merek = merek
        self.warna = warna
    def info(self):
        print(f'Mobil {self.merek} berwarna {self.warna}')
mobil1 = Mobil('toyota','hitam')
mobil1.info()

print('\nsoal 2 =')
class Mahasiswa:
    def __init__(self,nama,npm):
        self.nama = nama
        self.npm = npm
    def info(self):
        print(f'Nama: {self.nama}\nNPM : {self.npm}')
mahasiswaB = Mahasiswa('m.hilman.h','210511031')
mahasiswaB.info()

print('\nsoal 3 =')
class Lingkaran:
    def __init__(self,jari_jari):
        self.jari_jari = jari_jari
    def luas(self):
        return 3.14 * (self.jari_jari ** 2)
LingkaranA = Lingkaran(7)
print(f'luas lingkaran : {LingkaranA.luas()}')

print('\nsoal 4 =')
class buku:
    def __init__(self,judul,penulis):
        self.judul = judul
        self.penulis = penulis
    def info(self):
        print(f'Judul : {self.judul}\nPenulis : {self.penulis}')
Buku = buku('hayang kawin','Bpk.Udin')
Buku.info()

print('\nsoal 5 =')
class Pesawat:
    def __init__(self,maskapai,tujuan):
        self.maskapai = maskapai
        self.tujuan = tujuan
    def info(self):
        print(f'Maskapai : {self.maskapai}\nTujuan : {self.tujuan}')
pesawatA = Pesawat('Garuda','Majalengka-Jakarta')
pesawatA.info()

print('\nsoal 6 =')
class Kalkulator:
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def substract(x,y):
        return x-y
    @staticmethod
    def multiply(x,y):
        return x*y
    @staticmethod
    def devide(x,y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol')
        return x/y
print(f'Hasil penambahan 3 + 5 adalah : {Kalkulator.add(3,5)}')
print(f'Haisl penguranagan 10 - 7 adalah : {Kalkulator.substract(10,7)}')
print(f'Hasil perkalian 4 * 6 adalah : {Kalkulator.multiply(4,6)}')
print(f'Hasil pembagian 12 / 4 adalah : {Kalkulator.devide(12,4)}')

print('\nsoal 7 =')
class Celcius:
    @staticmethod
    def ke_fahreinheit(celcius):
        return(celcius * 9/5) + 32
    @staticmethod
    def ke_kelvin(celcius):
        return celcius + 273.15
    @staticmethod
    def ke_reamur(celcius):
        return celcius * 4/5
suhu1 = 75
mycelcius = Celcius.ke_fahreinheit(suhu1)
print(f'Konversi suhu dari celcius(75 derajat) ke fahreinheit adalah : {mycelcius} f')

print('\nLatihan =\n')
class Celcius:
    @staticmethod
    def ke_fahreinheit(celcius):
        return(celcius * 9/5) + 32
    @staticmethod
    def ke_kelvin(celcius):
        return celcius + 273.15
    @staticmethod
    def ke_reamur(celcius):
        return celcius * 4/5

class Fahreinheit:
    def __init__(self,fahreinheit):
        return 5/9 * (fahreinheit - 32 )
    
suhu1 = 75
suhu2 = 60
suhu3 = 90
myfahreinheit = Celcius.ke_fahreinheit(suhu1)
mykelvin = Celcius.ke_kelvin(suhu2)
myreamur = Celcius.ke_reamur(suhu3)
print(f'Konversi suhu dari celcius(75 derajat) ke fahreinheit adalah : {myfahreinheit} f\nKonversi suhu dari celcius(60 derajat) ke kelvin adalah : {mykelvin} k\nKonversi suhu dari celcius(90 derajat) ke reamur adalah : {myreamur} r')