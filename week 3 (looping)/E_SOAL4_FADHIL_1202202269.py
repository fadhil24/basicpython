banyak = int(input("Masukkan banyak barang belanjaan: "))
angka = 0

for i in range(banyak) :
    harga = int(input("Masukkan harga barang: "))
    angka = angka + harga
else :
    if (angka > 75000) :
        print(f"Total belanjaan sebelum diskon Rp. {angka}")
        angka = angka - (angka * (20/100))
        print(f"Total belanjaan setelah diskon Rp. {angka}")
    else :
        print(f"Total belanjaan yang harus dibayar Rp. {angka}")