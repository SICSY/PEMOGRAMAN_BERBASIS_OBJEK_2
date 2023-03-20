'''
nama = Muhammad Hilman Humaini 
Nim = 21051031
Kelas = Reguler 1
Matakuliah Pbo 2
Semester = 4
'''
print("CELCIUS PRO")
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