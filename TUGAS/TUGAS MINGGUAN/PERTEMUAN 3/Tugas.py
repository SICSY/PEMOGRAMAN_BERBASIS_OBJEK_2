import pygame
import os
os.system('cls')

hewan = [
    {
        "nama": "Anjing Bertengkar",
        "suara": "pertemuan3/Tugas/abertengkar.mp3",
    },
    {
        "nama": "Anjing Galak",
        "suara": "pertemuan3/Tugas/abetinagalak.mp3",
    },
    {
        "nama": "Anjing Lucu dan Imut",
        "suara": "pertemuan3/Tugas/alucuimut.mp3",
    },
    {
        "nama": "Anjing Memanggil Temannya",
        "suara": "pertemuan3/Tugas/amemanggiltemannya.mp3",
    },
    {
        "nama": "Anjing Menggonggong",
        "suara": "pertemuan3/Tugas/amenggonggong.mp3",
    },


    {
        "nama": "Anak Kucing",
        "suara": "pertemuan3/Tugas/kanakkucing.mp3",
    },
    {
        "nama": "Kucing Berkelahi",
        "suara": "pertemuan3/Tugas/kberantem.mp3",
    },
    {
        "nama": "Kucing Kawin",
        "suara": "pertemuan3/Tugas/kkawin.mp3",
    },
    {
        "nama": "Kucing Marah",
        "suara": "pertemuan3/Tugas/kmarah.mp3",
    },
    {
        "nama": "Kucing Minta Makan",
        "suara": "pertemuan3/Tugas/kmintamakan.mp3",
    },
   
]
def mainkan_suara(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        clock = pygame.time.Clock()
        clock.tick(0.2)
        pygame.mixer.music.stop()

# loop untuk menampilkan daftar hewan dan memainkan suara saat hewan tersebut dipilih
while True:
    # tampilkan daftar hewan
    for i, data_hewan in enumerate(hewan):
        print(f"{i+1}. {data_hewan['nama']}")
    
    # minta pengguna memilih hewan yang ingin didengar suaranya
    pilihan = input("Pilih hewan (1-10), atau ketik 'exit' untuk keluar: ")
    if pilihan.lower() == 'exit':
        break
    
    # validasi input pengguna
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > 10:
        print("Input tidak valid. Silakan pilih angka antara 1-10 atau ketik 'exit' untuk keluar.")
        continue
    
    # mainkan suara hewan yang dipilih
    data_hewan = hewan[int(pilihan)-1]
    print(f"Anda memilih {data_hewan['nama']}.")
    mainkan_suara(data_hewan['suara'])
    print('\n')
