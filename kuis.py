def mulai_kuis():
    print("\n--- Mulai Kuis ---")
    nama = input("Masukkan nama Anda: ")
    skor = 0

    soal = [
        {"pertanyaan": "Apa ibu kota Indonesia?", "jawaban": "Jakarta"},
        {"pertanyaan": "Hasil dari 5 + 7 adalah?", "jawaban": "12"},
        {"pertanyaan": "Siapa presiden pertama Indonesia?", "jawaban": "Soekarno"},
        {"pertanyaan": "Bumi mengelilingi?", "jawaban": "Matahari"},
        {"pertanyaan": "2 x 6 = ?", "jawaban": "12"},
    ]

    for i, s in enumerate(soal):
        print(f"\nSoal {i+1}: {s['pertanyaan']}")
        jawaban = input("Jawab: ")
        if jawaban.strip().lower() == s["jawaban"].lower():
            print("✅ Benar!")
            skor += 10
        else:
            print(f"❌ Salah. Jawaban: {s['jawaban']}")

    print(f"\nSkor akhir {nama}: {skor}")
    simpan_data(nama, skor)

def simpan_data(nama, skor):
    with open("peserta.txt", "a") as f:
        f.write(f"{nama},{skor}\n")
