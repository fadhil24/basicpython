jumlah = int(input("Masukkan Jumlah Angka : "))
angka = 0
list_angka = []

for i in range(jumlah):
    angka += 1
    masuk = int(input(f"Masukkan Angka ke-{angka} : "))
    list_angka.append(masuk)
    set_angka = set(list_angka)

print(list(set_angka))

