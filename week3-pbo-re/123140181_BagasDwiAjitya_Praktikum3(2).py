def tampilkan_menu():
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def tambah_tugas(tasks):
    tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
    if not tugas:
        raise ValueError("Input kosong. Harap masukkan tugas yang valid.")
    tasks.append(tugas)
    print("Tugas berhasil ditambahkan!")

def hapus_tugas(tasks):
    if not tasks:
        raise Exception("Daftar tugas kosong. Tidak ada tugas yang dapat dihapus.")
    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
    except ValueError:
        raise ValueError("Input tidak valid. Harap masukkan nomor tugas yang valid.")
    
    # Indeks list dimulai dari 0, sedangkan tampilan nomor tugas mulai dari 1
    if nomor < 1 or nomor > len(tasks):
        raise Exception(f"Error: Tugas dengan nomor {nomor} tidak ditemukan.")
    
    # Hapus tugas berdasarkan nomor (menyesuaikan dengan index)
    tugas_dihapus = tasks.pop(nomor - 1)
    print(f"Tugas '{tugas_dihapus}' berhasil dihapus!")

def tampilkan_tugas(tasks):
    if not tasks:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for idx, tugas in enumerate(tasks, start=1):
            print(f"- {tugas}")

def main():
    tasks = []
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
        try:
            if pilihan not in ["1", "2", "3", "4"]:
                raise ValueError("Pilihan tidak valid. Harap masukkan pilihan antara 1 hingga 4.")
            
            if pilihan == "1":
                tambah_tugas(tasks)
            elif pilihan == "2":
                hapus_tugas(tasks)
            elif pilihan == "3":
                tampilkan_tugas(tasks)
            elif pilihan == "4":
                print("Keluar dari program.")
                break
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
