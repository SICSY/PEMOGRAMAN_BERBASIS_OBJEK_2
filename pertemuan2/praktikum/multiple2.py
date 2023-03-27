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