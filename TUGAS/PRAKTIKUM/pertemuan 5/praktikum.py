try :
    angka1 = int(input('masukan angka pertama :'))
    angka2 = int(input('masukan angka kedua :'))

    hasil = angka1 / angka2
    print('hasil pembagian :', hasil)

except ZeroDivisionError:
    print('terjadi kesalahan : pembagian dengan nol tidak diizinkan !')