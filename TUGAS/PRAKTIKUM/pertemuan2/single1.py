print(f'\n{"SINGLE INHERITANCE":^50}\n{"="*50:^50}')

print(f'\nJAWABAN 1\n')
class konsumen:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
        print(f'Nama : ',self.nama)
        print(f'Umur : ',self.umur)
        return nama,umur
class jenisbarang(konsumen):
    def __init__(self,nama,umur,jb):
        super().__init__(nama,umur)
        self.jb = jb
        print('Merek Sabun :',self.jb)
    def sabun(self,barang):
        self.barang = barang
        print('Tipe Barang :',self.barang)
        return self.barang
    def displayinfo(self):
        print('Atas Nama',self.nama,'melalakukan Transaksi Pembelian Sabun' ,self.jb)

konsumen1 = jenisbarang('Udin',29,'sunlight')
konsumen1.sabun(barang= 'alat mandi'),konsumen1.displayinfo()
