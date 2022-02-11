class Mahasiswa():
    def __init__(self,nama,nim,kelas,alamat,angka):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.alamat = alamat
        self.angka = angka
    
    def show(self):
        print(f"Mahasiswa {self.angka}")
        print(f"Nama : {self.nama}")
        print(f"NIM : {self.nim}")
        print(f"Kelas : {self.kelas}")
        print(f"Alamat : {self.alamat}\n")

mahasiswa1 = Mahasiswa("Ananda", 1202190008, "SI-43-02", "Palangka Raya", 1)
mahasiswa2 = Mahasiswa("Xamimi", 12021902937, "SI-42-04", "Bogor", 2)
mahasiswa3 = Mahasiswa("Rizal", 1202128729, "SI-43-01", "Bandung", 3)

mahasiswa1.show()
mahasiswa2.show()
mahasiswa3.show()
