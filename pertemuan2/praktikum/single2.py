print(f'\n{"SINGLE INHERITANCE":^50}\n{"="*50:^50}')

print(f'\nJAWABAN 2\n')
class Handphone:
    def __init__(self,baterai,processor):
        self.baterai = baterai
        self.processor = processor
        print(f'Baterai : ',self.baterai)
        print(f'Processor : ',self.processor)
        return baterai,processor
class Merek(Handphone):
    def __init__(self,baterai,processor,merek,harga):
        super().__init__(baterai,processor)
        self.merek=merek
        self.harga = harga
        print('Merek barang:',self.merek)
        print('Harga :',self.harga)  
    def displayinfo(self):
        print('Merek',self.merek,'Spesifikasinya, Baterai =',self.baterai,'Processornya =',self.processor,'\nMelalakukan Transaksi Pembelian dengan harga' ,self.harga)

konsumen1 = Merek('Lippo','Snapdragon','xiaomi','50555')
konsumen1.displayinfo()

