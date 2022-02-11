daftar = []

while True:
    print("\t===Just Code It===")
    print("\t1. Mendaftarkan Peserta")
    print("\t2. Menghapus Peserta")
    print("\t3. Mencetak Semua Peserta\n")
    print("\t0. Exit\n")

    pilih = int(input("Masukkan Pilihan Anda : "))
    if (pilih == 1 ):
        tambah_nama = input("Masukkan Nama Peserta : ")
        print()
        daftar.append(tambah_nama)
    elif (pilih == 2):
        hapus_nama = input("Nama yang dihapus : ")
        daftar.remove(hapus_nama)
    elif (pilih == 3 ):
        print(daftar)
        print()
    elif (pilih == 0 ):
        print("Terima Kasih")
        break
    else:
        print("Masukkan menu yang sesuai\n")