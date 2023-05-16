class Pencipta:
    def __init__(self, nama, tahun_lahir):
        self.nama = nama
        self.tahun_lahir = tahun_lahir

class Lagu:
    def __init__(self, judul, pencipta):
        self.judul = judul
        self.pencipta = pencipta

    def tampilkan_info(self):
        print("Judul lagu:", self.judul)
        print("Pencipta:", self.pencipta.nama)
        print("Tahun lahir pencipta:", self.pencipta.tahun_lahir)

# Membuat objek Pencipta
pencipta = Pencipta("John Lennon", 1940)

# Membuat objek Lagu dengan menggunakan objek Pencipta sebagai argumen
lagu = Lagu("Imagine", pencipta)

# Menampilkan informasi lagu
lagu.tampilkan_info()
