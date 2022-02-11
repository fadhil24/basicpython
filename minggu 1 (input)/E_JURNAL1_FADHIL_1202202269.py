nama = input("masukkan nama : ")
kelas = input("masukkan kelas : ")
nim = int(input("masukkan nim : "))

kuis1 = float(input("nilai kuis 1 : "))
kuis2 = float(input("nilai kuis 2 : "))
kuis3 = float(input("nilai kuis 3 : "))
rata2 = int((kuis1 + kuis2 + kuis3) / 3)

print("Nama: " + nama)
print("Kelas: " + kelas)
print("NIM: " + str(nim))
print("Masukkan nilai Kuis 1: " + str(kuis1))
print("Masukkan nilai Kuis 2: " + str(kuis2))
print("Masukkan nilai Kuis 3: " + str(kuis3))
print("Rata-rata Kuis: " + str(rata2))

