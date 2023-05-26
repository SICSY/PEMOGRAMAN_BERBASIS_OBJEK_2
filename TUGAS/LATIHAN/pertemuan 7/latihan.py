# DYNAMIC ATTRIBUTES
class Person:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
person = Person('jhon', 20)

'''menambah atribut address secara dinamis'''
person.address = '123 main St.'
''' mengubah nilai atribut age secara dinamis'''
person.age = 35

print(person.nama)
print(person.umur)
print(person.address)


# DYNAMIC CLASSES


'''contoh 1'''
class PersegiPanjangMeta(type):
    def __init__(cls,nama,bases,attrs):
        super().__init__(nama,bases,attrs)

        def luas(cls,panjang,lebar):
            return panjang * lebar
        cls.luas = classmethod(luas)

        def keliling(cls,panjang,lebar):
            return 2 * (panjang + lebar)
        cls.keliling = classmethod(keliling)

class PersegiPanjang(metaclass = PersegiPanjangMeta):
     pass

A = PersegiPanjang()
B = A.luas(3,5)
C = A.keliling (5,6)
print('luas persegi panjang :',B)
print('keliling persegi panjang : ',C)

'''contoh 2'''
class SegitigaMeta(type):
    def __init__(cls,nama,bases,attrs):
        super().__init__(nama,bases,attrs)

        #tambahan method untuk menghitung luas dan keliling segetiga
        def luas(cls, alas, tinggi):
            return (alas * tinggi)
        cls.luas = classmethod(luas)

        def keliling(cls,sisi1,sisi2,sisi3):
            return sisi1 + sisi2 + sisi3
        cls.keliling = classmethod(keliling)
class Segitiga(metaclass = SegitigaMeta):
    pass
S = Segitiga()

#menghitung luas segitiga dengan alas = 4 dan tinggi = 5
luas_segitiga = Segitiga.luas(4,5)
print('luas segitiga = ', luas_segitiga)

#menghitung keliling segitiga dengan sisi1 =3, sisi2 = 4, sisi3 = 5
keliling_segitiga = Segitiga.keliling(3,4,5)
print('keliling segitiga = ', keliling_segitiga)

'''contoh 3'''
class CelciusMeta (type):
    def __init__(cls,nama,bases,attrs):
        super().__init__(nama,bases,attrs)
        cls.suhu_standar = ""
    def to_fahreinheit(cls, suhu):
        return (suhu * 9/5 ) + 32
    
    def to_reamur(cls, suhu):
        return suhu * 4/5
    
    def to_kelvin (cls,suhu):
        return suhu + 273.15
class Celcius(metaclass = CelciusMeta):
    def __init__(self,suhu):
        self.suhu = suhu
    def ke_unit(self,unit):
        if unit == 'Fahrenheit':
            self.suhu = self.__class__.to_fahreinheit(self.suhu)
            self.__class__.suhu_standar = 'Fahrenheit'
        
        elif unit == 'Reamur':
            self.suhu = self.__class__.to_reamur(self.suhu)
            self.__class__.suhu_standar = 'Reamur'

        elif unit == 'Kelvin':
            self.suhu = self.__class__.to_kelvin(self.suhu)
            self.__class__.suhu_standar = 'Kelvin'
        
        elif unit == 'Celcius':
            pass # do nothing
        else:
            raise ValueError(f'unit {unit} tidak dikenal')
        
    def __repr__(self):
        return f'{self.suhu:.2f} {self.__class__.suhu_standar}'
    
#Membuat objek suhu dengan nilai 100 celcius
c = Celcius(100)

#mengubah objek suhu menjadi fahrenheit
c.ke_unit('Fahrenheit')
print(c)