'''
nama = Muhammad Hilman Humaini 
Nim = 21051031
Kelas = Reguler 1
Matakuliah Pbo 2
Semester = 4
'''
import os
os.system('cls')

print("CELCIUS OOP")
class suhu:
    def __init__(self,celcius):
        self.celcius = celcius
    def fahreinheit(self):
        return (self.celcius * 9/5) + 32
    def reamur(self):
        return (self.celcius * 4/5)
    def kelvin(self):
        return (self.celcius + 273.15)
Suhu1 = suhu(75)
Suhu2 = suhu(60)
Suhu3 = suhu(90)
print(f'Konversi dari celcius ke fahreinheit: {suhu.fahreinheit(Suhu1)}')
print(f'Konversi dari celcius ke reamur: {suhu.reamur(Suhu2)}')
print(f'Konversi dari celcius ke kelvin: {suhu.kelvin(Suhu3)}')