import threading
import tkinter as tk

def aplikasi_1():
    def __init__(self, root):
        self.root = root
        self.root.title("aplikasi_1")
        

        self.nama_label = tk.Label(root, text="Nama:")
        self.nama_label.pack()

        self.nama_entry = tk.Entry(root)
        self.nama_entry.pack()

        self.nim_label = tk.Label(root, text="NIM:")
        self.nim_label.pack()

        self.nim_entry = tk.Entry(root)
        self.nim_entry.pack()

        self.kelas_label = tk.Label(root, text="Kelas:")
        self.kelas_label.pack()

        self.kelas_entry = tk.Entry(root)
        self.kelas_entry.pack()

        self.simpan_button = tk.Button(root, text="Simpan Data", command=self.simpan_data)
        self.simpan_button.pack()

    # Fungsi untuk aplikasi 1
    def simpan_data():
        nama = entry_nama.get()
        nim = entry_nim.get()
        kelas = entry_kelas.get()

        # Kirim data ke aplikasi 2
        aplikasi_2.data_baru(nama, nim, kelas)

        # Reset input fields
        entry_nama.delete(0, tk.END)
        entry_nim.delete(0, tk.END)
        entry_kelas.delete(0, tk.END)

    root = tk.Tk()
    root.title("Aplikasi 1")
    root.geometry("300x150")

    # Buat input fields
    label_nama = tk.Label(root, text="Nama:")
    label_nama.pack()
    entry_nama = tk.Entry(root)
    entry_nama.pack()

    label_nim = tk.Label(root, text="NIM:")
    label_nim.pack()
    entry_nim = tk.Entry(root)
    entry_nim.pack()

    label_kelas = tk.Label(root, text="Kelas:")
    label_kelas.pack()
    entry_kelas = tk.Entry(root)
    entry_kelas.pack()

    # Tombol simpan data
    tombol_simpan = tk.Button(root, text="Simpan Data", command=simpan_data)
    tombol_simpan.pack()

    root.mainloop()

def aplikasi_2():
    # Fungsi untuk aplikasi 2
    def update_data(data):
        output.delete(1.0, tk.END)
        output.insert(tk.END, data)

    root = tk.Tk()
    root.title("Aplikasi 2")

    # Output GUI
    output = tk.Text(root, width=40, height=10)
    output.pack()

    def data_baru(nama, nim, kelas):
        # Menggabungkan data baru dengan data yang ada di output
        existing_data = output.get(1.0, tk.END).strip()
        new_data = f"\nNama: {nama}\nNIM: {nim}\nKelas: {kelas}\n\n"
        updated_data = existing_data + new_data

        # Update data di output GUI
        update_data(updated_data)

    # Menambahkan metode data_baru sebagai atribut pada fungsi aplikasi_2
    aplikasi_2.data_baru = data_baru

    root.mainloop()

if __name__ == "__main__":
    # Buat thread untuk menjalankan aplikasi 1 dan 2 secara bersamaan
    thread_1 = threading.Thread(target=aplikasi_1)
    
    thread_2 = threading.Thread(target=aplikasi_2)
    
    # Jalankan thread-thread tersebut
    
   
thread_1.start()
thread_2.start()