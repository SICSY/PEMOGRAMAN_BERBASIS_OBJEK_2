class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        
    def tampil_data(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        
    def tampil_data(self, prodi):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Program Studi:", prodi)

mhs = Mahasiswa("John Doe", "123456789")
mhs.tampil_data('teknik ') # akan memanggil fungsi pertama