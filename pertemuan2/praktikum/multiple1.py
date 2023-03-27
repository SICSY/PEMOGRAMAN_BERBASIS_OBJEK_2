class Negara:
    def __init__(self,nama,benua):
        self.nama = nama
        self.benua = benua
    def belajar(self):
        print('Negara :',self.nama,'Benua :',self.benua)
class presiden:
    def __init__(self,nama,pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama,'Sedang bersosialisasi')
class wakilpresiden(Negara,presiden):
    def __init__(self,nama,benua,pekerjaan):
        Negara.__init__(self,nama,benua)
        presiden.__init__(self,nama,pekerjaan)
    def bersosialisasi(self):
        print(self.nama,'sedang bersosialisasi')
mhspekerja = wakilpresiden('Indonesia','Asean','Presiden')
mhspekerja.belajar()
