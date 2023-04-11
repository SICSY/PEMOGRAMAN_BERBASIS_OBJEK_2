class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang

    def melakukan_penelitian(self, topik):
        print(f"{self.nama} sedang melakukan penelitian tentang {topik} dalam bidang {self.bidang}.")

    def publikasi(self, hasil_penelitian):
        print(f"{self.nama} telah mempublikasikan hasil penelitiannya tentang {hasil_penelitian}.")

class Jurnalis:
    def __init__(self, nama, media):
        self.nama = nama
        self.media = media

    def laporan_terkini(self, topik):
        print(f"{self.nama} dari {self.media} melaporkan berita terkini tentang {topik}.")

    def wawancara(self, narasumber):
        print(f"{self.nama} dari {self.media} telah melakukan wawancara dengan {narasumber}.")
peneliti1 = Peneliti("Dr. John Doe", "Kesehatan")
peneliti1.melakukan_penelitian("Pengobatan penyakit jantung")
peneliti1.publikasi("Terapi baru untuk penyakit jantung")

jurnalis1 = Jurnalis("Jane Smith", "Koran XYZ")
jurnalis1.laporan_terkini("Peningkatan angka kecelakaan lalu lintas")
jurnalis1.wawancara("Kepala Satuan Lalu Lintas Polisi XYZ")
