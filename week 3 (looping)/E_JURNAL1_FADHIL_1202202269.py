angka = 3

for i in range(angka) :
    username = input("Masukkan username anda : ")
    password = input("Masukkan password anda : ")
    if (username == "alpro") and (password == "daspro123") :
        print("Selamat, Anda berhasil login!")
        break
    else :
        angka = angka - 1
        print(f"Login gagal. Sisa percobaan login sebanyak {angka}")
else :
    print("Batas percobaan login anda habis")

   