kaos = 25000
kemeja = 50000
jas = 100000
angka = 0
harga = 0

barang = ["KAOS", "KEMEJA", "JAS", "SELESAI"]
print("=== SELAMAT DATANG DI PROGRAM BUTIK ===")

for i in barang :
    angka = angka + 1
    print(f"{angka}. {i}")

while True :
    banyak_barang = int(input("Masukkan Barang Yang Ingin Dibeli (1/2/3/4) : "))
    if (banyak_barang == 1) :
        print("Kaos Ditambahkan")
        harga = harga + kaos
    elif (banyak_barang == 2) :
        print("Kemeja Ditambahkan")
        harga = harga + kemeja
    elif (banyak_barang == 3) :
        print("Jas Ditambahkan")
        harga = harga + jas
    elif (banyak_barang == 4) :
        print(f"Total : {harga}")
        break
    