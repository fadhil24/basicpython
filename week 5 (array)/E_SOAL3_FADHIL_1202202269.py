print("\tNOTES TEMAN BARU")
list_nama = []

while True:
    nama = input("Masukkan Nama Teman Baru : ")
    list_nama.append(nama)
    if (nama == "selesai"):
        list_nama.remove("selesai")
        break

print("\tTeman-teman Baru!")
print(list_nama)