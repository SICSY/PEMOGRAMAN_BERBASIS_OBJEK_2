class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print("Nama hewan:", self.nama)
        print("Umur hewan:", self.umur)

class Kucing(Hewan):
    def __init__(self, nama, umur, ras):
        super().__init__(nama, umur)
        self.ras = ras

    def info(self):
        super().info()
        print("Ras kucing:", self.ras)

class Anjing(Hewan):
    def __init__(self, nama, umur, jenis):
        super().__init__(nama, umur)
        self.jenis = jenis

    def info(self):
        super().info()
        print("Jenis anjing:", self.jenis)

kucing = Kucing("Tom", 2, "Persia")
kucing.info()

anjing = Anjing("Spike", 3, "Bulldog")
anjing.info()