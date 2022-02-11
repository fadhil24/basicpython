list_nama = []
list_pilih = []

def pilih1(pilihan):
    if (pilihan == 1):
        return "XAX"
    elif (pilihan == 2):
        return "ADV"
    elif (pilihan == 3):
        return "NOP"
    elif (pilihan == 4):
        return "HAS"
    elif (pilihan == 5):
        return "IAN"
    else:
        return "Tidak Memilih"

while True:
    print("\t=== DASPRO VOTING ===")
    print("\t1. Voting")
    print("\t2. Database\n")
    print("\t0. Exit\n")

    pilih = int(input("Masukkan Pilihan Anda : "))

    if (pilih == 1):
        nama = input("Masukkan Nama Anda : ")
        print()
        list_nama.append(nama)
        print("\tKANDIDAT ASPRAK TERIMUT")
        print("\t1. XAX")
        print("\t2. ADV")
        print("\t3. NOP")
        print("\t4. HAS")
        print("\t5. IAN\n")
        pilihan = int(input("Masukkan Pilihan (1/2/3/4/5) : "))
        list_pilih.append(pilih1(pilihan))
    elif (pilih == 2):
        token = input("Masukkan Token : ")
        if (token == "d4spr0"):
            for i in range(len(list_nama)):
                print(f"{list_nama[i]} memilih {list_pilih[i]}")
        else:
            print("Token Salah")
    elif (pilih == 0):
        print("Terima Kasih")
        break
    else:
        print("Pilih menu yang sesuai")


            