class animal :
    def __init__(self,nama,warna):
        self.nama = nama 
        self.warna = warna
    def getnama(self):
        return self.nama
    def getwarna(self):
        return self.warna
    def layar(self):
        print(f'Nama hewan : {self.nama}')
        print(f'Warna hewan : {self.warna}')
    
class mamal(animal):
    def __init__(self,nama,warna,bulu):
        super().__init__(nama,warna)
        self.bulu = bulu
    def getbulu(self):
        return self.bulu
    def layar(self):
        super().layar()
        print(f'Bulu : {self.bulu}')

class burung(animal):
    def __init__(self, nama, warna, sayap):
        super().__init__(nama, warna,)
        self.sayap = sayap
    def getsayap(self):
        return self.sayap
    def layar(self):
        super().layar()
        print(f'Sayap : {self.sayap}')

class reptile(mamal):
    def __init__(self, nama, warna, bulu,ukuran):
        super().__init__(nama, warna, bulu)
        self.ukuran = ukuran
    def get_scale(self):
        return self.ukuran
   
    def layar(self):
        super().layar()
        print(f'Ukuran : {self.ukuran}')
       
y = burung('parkit', 'kuning','pendek')
z = mamal('gajah','abu-abu','tidak punya')
x = reptile('python', 'kuning','berisik','penjang',)

y.layar()
print('\n')
z.layar()
print('\n')