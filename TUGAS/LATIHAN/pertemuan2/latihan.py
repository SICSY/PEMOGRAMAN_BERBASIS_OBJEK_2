import os
os.system('cls')
print(f'{"PERTEMUAN KE - 2 LATIHAN INHERITANCE / PEWARISAN":^50}\n{"="*50:^50}')

# CONTOH
print(f'\n{"CONTOH":^50}\n{"="*50:^50}')
class bangunandatar:
    def __init__(self,sisi):
        self.sisi = sisi
    def luasarea(self):
        pass
class persegi(bangunandatar):
    def __init__(self,sisi):
        super().__init__(sisi)
    def nilaikeliling(self):
        return 4 * self.sisi
class lingkaran(bangunandatar):
    def __init__(self,jari_jari):
        super().__init__(jari_jari)
    def luasarea(self):
        return 3.14 * self.sisi * self.sisi
    def nilaikeliling(self):
        return 2 * 3.14 * self.sisi
Persegi = persegi(5)
Lingkaran = lingkaran(7)
print('luas persegi : ',Persegi.luasarea())
print('keliling persegi : ',Persegi.nilaikeliling())
print('luas lingkaran : ',Lingkaran.luasarea())
print('keliling lingkaran : ',Lingkaran.nilaikeliling())

print(f'\n{"SINGLE INHERITANCE":^50}\n{"="*50:^50}')

print(f'\nCONTOH 1\n')
class hewan:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama,'bergerak')
class kucing(hewan):
    def __init__(self,nama,umur,jenis):
        super().__init__(nama,umur)
        self.jenis = jenis
    def bersuara(self):
        print('meow')
kucing1 = kucing('kity',2,'persia')
kucing1.bergerak()
kucing1.bersuara()

print(f'\nCONTOH 2\n')
class manusia:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f'{self.nama} sedang berbicara')
class dosen(manusia):
    def __init__(self,nama,umur,nip):
        super().__init__(nama,umur)
        self.nip = nip
    def mengajar(self):
        print(f'{self.nama} dengan NIP {self.nip} sedang mengajar')
dosen1 = dosen('tono',34,'12349')
dosen1.berbicara()
dosen1.mengajar()

print(f'\nCONTOH 3\n')
class kendaran:
    def __init__(self,jenis,merek,warna):
        self.jenis = jenis
        self.merek = merek
        self.warna = warna
    def berkendara(self):
        print('Kendaran ini sedang berjalan')
class motor(kendaran):
    def __init__(self, jenis, merek, warna, cc):
        super().__init__(jenis,merek,warna)
        self.cc = cc
    def belok(self):
        print('Sepeda motor ini sedang belok')
motor1 = motor('Sepeda Motor','Honda','Merah',150)
motor1.berkendara()
motor1.belok()

print(f'\n{"MULTIPLE INHERITANCE":^50}\n{"="*50:^50}')
print(f'\nCONTOH 1\n')
class mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim
    def belajar(self):
        print(self.nama,'Sedang belajar')
class pekerja:
    def __init__(self,nama,pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama,'Sedang bersosialisasi')
class mahasiswapekerja(mahasiswa,pekerja):
    def __init__(self,nama,nim,pekerjaan):
        mahasiswa.__init__(self,nama,nim)
        pekerja.__init__(self,nama,pekerjaan)
    def bersosialisasi(self):
        print(self.nama,'sedang bersosialisasi')
mhspekerja = mahasiswapekerja('Rahma','139102','Programer')
mhspekerja.belajar()
mhspekerja.bekerja()
mhspekerja.bersosialisasi()

print(f'\nCONTOH 2\n')

class hewan:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def display_info (self):
        print(f'Nama : {self.nama}')
        print(f'Umur : {self.umur}')
class reptil:
    def __init__(self,jenis,habitat):
        self.jenis = jenis
        self.habitat = habitat
    def displayinfo(self):
        print(f'Jenis : {self.jenis}')
        print(f'Habitat : {self.habitat}')
class amphibi:
    def __init__(self,metamorfosis, habitat):
        self.metamorfosis = metamorfosis
        self.habitat = habitat
    def displayinfo(self):
        print(f'Metamorfosis : {self.metamorfosis}')
        print(f'Habitat : {self.habitat}')
class katak(reptil,amphibi):
    def __init__(self,nama,umur,jenis,habitat,metamorfosis):
        hewan.__init__(self,nama,umur)
        reptil.__init__(self,jenis,habitat)
        amphibi.__init__(self,metamorfosis,habitat)
    def displayinfo(self):
        super().displayinfo()
        print(f'Nama : {self.nama}')
        print(f'Umur : {self.umur}')
        print(f'Jenis : {self.jenis}')
        print(f'Habitat : {self.habitat}')
        print(f'Metamorfosis : {self.metamorfosis}')
katak1 = katak('Katak Hijau',2,'Reptile-Amphibi','Air','Telur')
katak1.displayinfo()

print(f'\nCONTOH 3\n')
class orang:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def displayinfo(self):
        print(f'Nama : {self.nama}')
        print(f'Umur : {self.umur}')
class pekerja:
    def __init__(self,pekerjaan,gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji
    def displayinfo(self):
        print(f'Pekerjaan : {self.perkerjaan}')
        print(f'Gaji : {self.gaji}')
class penulis:
    def __init__(self,buku,genre):
        self.buku = buku
        self.genre = genre
    def displayinfo(self):
        print(f'Buku : {self.buku}')
        print(f'Genre : {self.genre}')
class penulispekerja(orang,pekerja,penulis):
    def __init__(self,nama,umur,pekerjaan,gaji,buku,genre):
        orang.__init__(self,nama,umur)
        pekerja.__init__(self,pekerjaan,gaji)
        penulis.__init__(self,buku,genre)
    def displayinfo(self):
        super().displayinfo()
        print(f'Pekerjaan : {self.pekerjaan}')
        print(f'Gaji : {self.gaji}')
        print(f'Buku : {self.buku}')
        print(f'Genre : {self.genre}')
penulispekerja1 = penulispekerja('Jane Doe',30,'Penulis','Rp 8jt','The book','Fisika')  
penulispekerja1.displayinfo()  

print(f'\nCONTOH 4\n')
class hewan:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def displayinfo(self):
        print(f'Nama Hewan : {self.nama}')
        print(f'Umur Hewan : {self.umur}')
class mamalia(hewan):
    def __init__(self,jenis):
        self.jenis = jenis
    def displayinfo(self):
        super().displayinfo()
        print(f'Jenis Hewan : {self.jenis}')
class karnivora(hewan):
    def __init__(self,makanan):
        self.makanan = makanan
    def displayinfo(self):
        super().displayinfo()
        print(f'Makanan Hewan : {self.makanan}')
class harimau(mamalia,karnivora):
    def __init__(self,nama,umur,jenis,makanan):
        hewan.__init__(self,nama,umur)
        mamalia.__init__(self,jenis)
        karnivora.__init__(self,makanan)
    def displayinfo(self):
        super().displayinfo() 
        
harimau1 = harimau('mamalia',12,'harimau sumatera','daging')
harimau1.displayinfo()

print(f'\nCONTOH 5\n')
class person:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def displayinfo(self):
        print(f'Nama : {self.nama}')
        print(f'Umur : {self.umur}')
class mahasiswa(person):
    def __init__(self,jurusan):
        self.jurusan = jurusan
    def displayinfo(self):
        super().displayinfo()
        print(f'Jurusan : {self.jurusan}')
class alumni(person):
    def __init__(self,tahunlulus):
        self.tahunlulus = tahunlulus
    def displayinfo(self):
        super().displayinfo()
        print(f'Tahun lulusan : {self.tahunlulus}')
    
class mahasiswaalumni(mahasiswa,alumni):
    def __init__(self,nama,umur,jurusan,tahunlulus):
        person.__init__(self,nama,umur)
        mahasiswa.__init__(self,jurusan)
        alumni.__init__(self,tahunlulus)
    
        
mahasiswa1 = mahasiswaalumni('Melinda', 17, 'Farmasi',2023)
mahasiswa1.displayinfo()    

print(f'\n{"HIERARCHICAL INHERITANCE":^50}\n{"="*50:^50}')
print(f'\nCONTOH 1\n')
class animal :
    def __init__(self,nama,warna):
        self.nama = nama 
        self.warna = warna
    def getnama(self):
        return self.nama
    def getwarna(self):
        return self.warna
    def layar(self):
        print(f'Nama hewan : {self.nama}')
        print(f'Warna hewan : {self.warna}')
    
class mamal(animal):
    def __init__(self,nama,warna,bulu):
        super().__init__(nama,warna)
        self.bulu = bulu
    def getbulu(self):
        return self.bulu
    def layar(self):
        super().layar()
        print(f'Bulu : {self.bulu}')

class burung(animal):
    def __init__(self, nama, warna, sayap):
        super().__init__(nama, warna,)
        self.sayap = sayap
    def getsayap(self):
        return self.sayap
    def layar(self):
        super().layar()
        print(f'Sayap : {self.sayap}')


class reptile(mamal):
    def __init__(self, nama, warna, bulu,ukuran):
        super().__init__(nama, warna, bulu)
        self.ukuran = ukuran
    def get_scale(self):
        return self.ukuran
   
    def layar(self):
        super().layar()
        print(f'Ukuran : {self.ukuran}')
       
y = burung('parkit', 'kuning','pendek')
z = mamal('gajah','abu-abu','tidak punya')
x = reptile('python', 'kuning','berisik','penjang',)

y.layar()
print('\n')
z.layar()
print('\n')
print(f'{"Dibawah ini merupakan Contoh Hierarchical Inheritance":^70}\n{"="*70:^70}')
x.layar()

print(f'\nCONTOH 2\n')
class karyawan:
    def __init__(self,nama,umur,gaji):
        self.nama = nama
        self.umur = umur
        self.gaji = gaji
    def getnama(self):
        return self.nama
    def getage(self):
        return self.umur
    def getsalary(self):
        return self.gaji
    def layar(self):
        print(f'Nama : {self.nama}')
        print(f'Umur : {self.umur}')
        print(f'Gaji : {self.gaji}')
class manager(karyawan):
    def __init__(self,nama,umur,gaji,departement):
        super().__init__(nama,umur,gaji)
        self.departement = departement
    def getdepartement(self):
        return self.departement
    def layar(self):
        super().layar()
        print(f'Departement : {self.departement}')
class programmer(karyawan):
    def __init__(self,nama,umur,gaji,bahasa):
        super().__init__(nama,umur,gaji)
        self.bahasa = bahasa
    def getbahasa(self):
        return self.bahasa
    def layar(self):
        super().layar()
        print(f'Bahasa: {self.bahasa}')

class seniorprogramer(programmer):
    def __init__(self,nama,umur,gaji,bahasa,level):
        super().__init__(nama,umur,gaji,bahasa)
        self.level = level
    def getlevel(self):
        return self.level
    
    def layar(self):
        super().layar()
        print(f'Level : {self.level}')
y = manager('Hilman','19','10 juta','Keuangan')
x = seniorprogramer('Hilman','19','5 juta','Python','Pro')
x.layar()
print('\n')
y.layar()
    
print(f'\nCONTOH 3\n')