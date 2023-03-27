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