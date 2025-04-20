def baca_data():
    try:
        with open("peserta.txt", "r") as f:
            data = [line.strip().split(",") for line in f.readlines()]
            return [[x[0], int(x[1])] for x in data]
    except FileNotFoundError:
        return []

def tampilkan_leaderboard():
    data = baca_data()
    data = selection_sort(data)
    print("\n--- Leaderboard ---")
    for i, (nama, skor) in enumerate(data, 1):
        print(f"{i}. {nama} - {skor} poin")

def selection_sort(data):
    for i in range(len(data)):
        max_idx = i
        for j in range(i+1, len(data)):
            if data[j][1] > data[max_idx][1]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]
    return data

def cari_peserta():
    nama_dicari = input("Masukkan nama peserta: ")
    data = baca_data()

    for nama, skor in data:
        if nama.lower() == nama_dicari.lower():
            print(f"Ditemukan! {nama} - {skor} poin")
            return
    print("Peserta tidak ditemukan.")
