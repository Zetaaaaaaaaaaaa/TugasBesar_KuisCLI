from kuis import mulai_kuis
from leaderboard import tampilkan_leaderboard, cari_peserta

def menu():
    while True:
        print("\n=== Aplikasi Kuis Edukasi CLI ===")
        print("1. Mulai Kuis")
        print("2. Lihat Leaderboard")
        print("3. Cari Peserta")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            mulai_kuis()
        elif pilihan == "2":
            tampilkan_leaderboard()
        elif pilihan == "3":
            cari_peserta()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()
