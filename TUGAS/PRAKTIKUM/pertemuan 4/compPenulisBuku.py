class penulis:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
        self.buku = []
    def tambahbuku (self,judul,tahun):
        buku = Buku(judul,tahun)
        self.buku.append(buku)

    def tampilkanbuku(self):
        print(f'nama penulis : {self.nama} \nUmur : {self.umur} \nKategori Buku diterbitkan :')
        for buku in self.buku:
            print(buku.judul)
class Buku:
    def __init__(self,judul,tahun):
        self.judul = judul
        self.tahun = tahun

data = penulis('jajang',49)
data.tambahbuku('pelangi indah',1923)
data.tambahbuku('menyesal di akhir',1938)
data.tambahbuku('mengenang indahnya dunia',1958)

data.tampilkanbuku()
