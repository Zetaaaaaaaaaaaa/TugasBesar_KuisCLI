import tkinter as tk
from tkinter import messagebox
from kuis import mulai_kuis
from leaderboard import tampilkan_leaderboard_gui, cari_peserta_gui

class AplikasiKuis:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kuis Edukasi")
        self.nama = ""
        self.halaman_menu()

    def halaman_menu(self):
        self.clear()
        tk.Label(self.root, text="Selamat Datang di Aplikasi Kuis Edukasi", font=('Arial', 16)).pack(pady=10)
        tk.Button(self.root, text="Mulai Kuis", command=self.halaman_nama, width=30).pack(pady=5)
        tk.Button(self.root, text="Lihat Leaderboard", command=tampilkan_leaderboard_gui, width=30).pack(pady=5)
        tk.Button(self.root, text="Cari Peserta", command=cari_peserta_gui, width=30).pack(pady=5)
        tk.Button(self.root, text="Keluar", command=self.root.quit, width=30).pack(pady=5)

    def halaman_nama(self):
        self.clear()
        tk.Label(self.root, text="Masukkan Nama Anda", font=('Arial', 14)).pack(pady=10)
        self.ent_nama = tk.Entry(self.root)
        self.ent_nama.pack(pady=5)
        tk.Button(self.root, text="Mulai", command=self.mulai_kuis_gui).pack(pady=10)

    def mulai_kuis_gui(self):
        self.nama = self.ent_nama.get()
        if not self.nama:
            messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
        else:
            mulai_kuis(self.root, self.nama, self.halaman_menu)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiKuis(root)
    root.mainloop()
