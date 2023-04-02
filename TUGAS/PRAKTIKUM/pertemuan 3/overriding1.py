class lemari:
    def tipe(self):
        print('lemari satu pintu')
class lemari2(lemari):
    def tipe(self):
        print('lemari dua pintu')
class lemari3(lemari):
    def tipe(self):
        print('lemari tiga pintu')
Lemari = lemari()
Lemari2 = lemari2()
Lemari3 = lemari3()

Lemari.tipe()
Lemari2.tipe()
Lemari3.tipe()