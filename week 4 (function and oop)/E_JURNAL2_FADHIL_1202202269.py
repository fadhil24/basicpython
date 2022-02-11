class Kubus():
    def __init__(self,angka,sisi):
        self.angka = angka
        self.sisi = sisi
        print(F"Kubus {angka}")
    
    def volume(self):
        volum = self.sisi**3
        return volum

    def luas(self):
        luasp = 6 * (self.sisi**2)
        return luasp
    
    def keliling(self):
        kelilingg = 12 * self.sisi
        return kelilingg

    def show(self):
        print(f"Volume : {self.volume()} cm^3")
        print(f"Luas Permukaan : {self.luas()} cm^2")
        print(f"Keliling : {self.keliling()} cm")
        print("="*26)

print("="*26)
sisi1 = int(input("Masukkan sisi Kubus 1 : "))
sisi2 = int(input("Masukkan sisi Kubus 2 : "))
print("="*26)

kubus1 = Kubus(1, sisi1)
kubus1.show()
kubus2 = Kubus(2, sisi2)
kubus2.show()