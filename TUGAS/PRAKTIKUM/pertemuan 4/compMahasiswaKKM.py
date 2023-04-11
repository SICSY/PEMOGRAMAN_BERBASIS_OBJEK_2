class Mahasiswa:
    def __init__(self,nama,nim,):
        self.nama = nama
        self.nim = nim
    def prodi(self,jurusan):
        print(f'{self.nama} dengan nim {self.nim} prodi {jurusan}')
    def penelitian(self,hasil):
        print(f'{self.nama} telah memilih judul penelitian {hasil}')
class Kkm:
    def __init__(self,nama,alamat):
        self.nama = nama
        self.alamat = alamat
    def laporan(self,topik):
        print(f'{self.nama} telah melakukan KKM di daerah {self.alamat} dan memilih topik {topik}')
    def hasilakhir(self,hasil):
        print(f'{self.nama} memilih KKM di daerah {self.alamat} dinyatakan di {hasil} oleh dosen')
mahasiswa1 = Mahasiswa('udin','210394')
mahasiswa1.prodi('Teknik Informatika')
mahasiswa1.penelitian('Membuat aplikasi e-Commers')

kkm1 = Kkm('udin','Duku Puntang')
kkm1.laporan('membangun ekosistem perdagangan berbasis digital')
kkm1.hasilakhir('terima')