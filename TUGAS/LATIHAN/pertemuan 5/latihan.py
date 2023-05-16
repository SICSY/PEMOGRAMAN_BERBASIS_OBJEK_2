# 1. BLOK TRY - EXCEPT

try:
    my_list = [1,2,3]
    my_list.remove(4)
except ValueError:
    print('error : element tidak ada dalam list !')

# 2. exception specific

try:
    #buka file dan baca isi nya
    with open ('file.txt','r' )as file:
        data = file.read()
    #ubah teks menjadi bilangan bulat 
    num = int(data)
    #bagi dengan angka yang diinputkan oleh user
    divisor = int(input('masukan angka pembagi :'))
    result = num /divisor

    #tampilkan hasil bagi
    print('hasil bagi adalah :',result)

#tangani beberapa jenis exception
except FileNotFoundError:
    print('file tidak ditemukan ')
except ValueError:
    print('isi file harus berupa bilangan bulat !')
except ZeroDivisionError:
    print('angka pembagi tidak boleh nol !')
except Exception as e:
    print('terjadi kesalahan :',str(e))

# 3. BLOK ELSE
try:
    #buka file dan baca isinya
    with open ('file.txt','r') as file:
        data = file.read()
    #ubah teks menjadi bilangan bulat 
    num = int(data)

except FileNotFoundError:
    print('file tidak ditemukan !')
except ValueError:
    print('isi file harus berupa bilangan bulat !')
else:
    #jika tidak ada terjadi kesalahan , tampilkan hasil konversi
    print('isi file berhasil dikonversi menjadi bilangan bulat :', num)

# 4. BLOK FINALLY

try: 
    file = open('file.txt','r')
    num = int(file.readline())
except ValueError:
    print('error : input tidak valid !')
finally:
    file.close()

# berikut berupa contoh penggunaan exception handling:
# mengatasi type error

try:
    x = 'hello'
    y = x + 5
except TypeError:
    print('terjadi kesalahan tipe data, pastikan variable yang digunakan sudah benar !')

# mengatasi zero division error
try:
    x = 10
    y = x/0
except ZeroDivisionError:
    print('terjadi kesalahan saat pembagian dengan nol !')

# mengatasi file not found error 
try:
    with open ('file yang tidak ada.txt') as file :
        data = file.read()
except FileNotFoundError:
    print('file yang diminta tidak di temukan ')

# mengatasi key error
dictrionary = {'satu': 1, 'dua': 2, 'tiga': 3}
try:
    value = dictrionary['empat']
except KeyError:
    print('key yang diminta tidak ditemukan pada dictionary')

# 5. index error

list_angka = [1,2,3]
try:
    value  = list_angka[4]
except IndexError:
    print('index yang diminta melebihi jumlah elemen dalam list')

# 6. attribute error

class manusia :
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
Manusia = manusia('andi',20)
try:
    print(manusia.alamat)
except AttributeError:
    print('objek tidak memiliki attribut yang dimintai')

# 7. Value Error
try :
    angka = int('bukan angka')
except ValueError:
    print('terjadi kesalahan konversi nilai ke dalam tipe data yang diinginkan !')

# 8. Name error
try: 
    print('nama')
except NameError:
    print('variable yang diminta beleum didefinisikan')

# 9. keyboard interrupt 

try:
    while True:
        pass
except KeyboardInterrupt:
    print('program dihentikan oleh pengguna')

# 10. memory error
except MemoryError:
    print('memori tidak cukup untuk menampung data yang diminta !')
