import tkinter as tk
from tkinter import messagebox

def tampilkan_leaderboard_gui():
    try:
        with open("peserta.txt", "r") as file:
            data = [line.strip().split(',') for line in file.readlines() if line.strip()]
        data.sort(key=lambda x: int(x[1]), reverse=True)
    except FileNotFoundError:
        messagebox.showinfo("Info", "Belum ada data peserta.")
        return

    window = tk.Toplevel()
    window.title("Leaderboard")
    tk.Label(window, text="Leaderboard Peserta", font=('Arial', 14)).pack(pady=10)

    for i, (nama, skor) in enumerate(data[:10], start=1):
        tk.Label(window, text=f"{i}. {nama} - {skor}").pack(anchor='w')

def cari_peserta_gui():
    def cari():
        nama_dicari = entry.get().strip().lower()
        if not nama_dicari:
            messagebox.showwarning("Peringatan", "Masukkan nama terlebih dahulu.")
            return

        try:
            with open("peserta.txt", "r") as file:
                data = [line.strip().split(',') for line in file.readlines() if line.strip()]
            hasil = [f"{nama} - {skor}" for nama, skor in data if nama_dicari in nama.lower()]
        except FileNotFoundError:
            messagebox.showinfo("Info", "Belum ada data peserta.")
            return

        if hasil:
            hasil_text.set("\n".join(hasil))
        else:
            hasil_text.set("Tidak ditemukan.")

    window = tk.Toplevel()
    window.title("Cari Peserta")
    tk.Label(window, text="Masukkan Nama Peserta", font=('Arial', 12)).pack(pady=5)
    entry = tk.Entry(window)
    entry.pack(pady=5)
    tk.Button(window, text="Cari", command=cari).pack(pady=5)
    hasil_text = tk.StringVar()
    tk.Label(window, textvariable=hasil_text, justify='left').pack(pady=10)