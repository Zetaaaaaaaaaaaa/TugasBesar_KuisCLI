import tkinter as tk
from tkinter import messagebox
import json

soal_list = [
    {"pertanyaan": "Apa ibu kota Indonesia?", "pilihan": ["Bandung", "Jakarta", "Surabaya", "Medan"], "jawaban": "Jakarta"},
    {"pertanyaan": "Berapa hasil dari 12 x 8?", "pilihan": ["96", "86", "106", "98"], "jawaban": "96"},
    {"pertanyaan": "Simbol unsur kimia Oksigen adalah?", "pilihan": ["O", "Ox", "Og", "Om"], "jawaban": "O"},
    {"pertanyaan": "Bahasa pemrograman apa yang digunakan untuk web frontend?", "pilihan": ["Python", "Java", "HTML", "C++"], "jawaban": "HTML"},
    {"pertanyaan": "Planet terbesar di tata surya adalah?", "pilihan": ["Bumi", "Saturnus", "Mars", "Jupiter"], "jawaban": "Jupiter"}
]

def mulai_kuis(root, nama, kembali_callback):
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    skor = {'nilai': 0}
    index = {'no': 0}

    def tampilkan_soal():
        for widget in frame.winfo_children():
            widget.destroy()

        if index['no'] < len(soal_list):
            soal = soal_list[index['no']]
            tk.Label(frame, text=f"Soal {index['no']+1}: {soal['pertanyaan']}", wraplength=400, font=('Arial', 12)).pack(pady=10)
            var_jawaban = tk.StringVar()

            for opsi in soal['pilihan']:
                tk.Radiobutton(frame, text=opsi, variable=var_jawaban, value=opsi).pack(anchor='w')

            def lanjut():
                if var_jawaban.get() == "":
                    messagebox.showwarning("Peringatan", "Pilih salah satu jawaban!")
                else:
                    if var_jawaban.get() == soal['jawaban']:
                        skor['nilai'] += 20
                    index['no'] += 1
                    tampilkan_soal()

            tk.Button(frame, text="Selanjutnya", command=lanjut).pack(pady=10)

        else:
            simpan_skor(nama, skor['nilai'])
            messagebox.showinfo("Selesai", f"Kuis selesai! Skor Anda: {skor['nilai']}")
            frame.destroy()
            kembali_callback()

    tampilkan_soal()


def simpan_skor(nama, skor):
    try:
        with open("peserta.txt", "a") as file:
            file.write(f"{nama},{skor}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan skor: {e}")
