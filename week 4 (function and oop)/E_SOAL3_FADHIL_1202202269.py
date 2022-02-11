class Anak():
    def __init__(self,gender):
        self.gender = gender
        print(f"Sifat Anak {self.gender}:")
        print("I Love You\nSaya tidak marah kok\nSaya maafkan kamu\nKembalilah padaku")
    
    def Laki(self,sifat1="Saya tidak takut",sifat2="Ini saya ada rezeki buat kamu"):
        print(f"{sifat1}\n{sifat2}")
        print()

    def Cewe(self,sifat1="Haduh saya jadi malu",sifat2="Akumah cukup kamu aja"):
        print(f"{sifat1}\n{sifat2}")

anaklaki = Anak("Laki-laki")
anaklaki.Laki()

anakcewe = Anak("Perempuan")
anakcewe.Cewe()
