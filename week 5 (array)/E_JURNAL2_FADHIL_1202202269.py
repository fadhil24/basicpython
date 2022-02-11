sifat_kamu = []
sifat_dia = []
berjalan = True

while berjalan:
    kamu = input("Masukkan Sifat Kamu : ")
    sifat_kamu.append(kamu)
    for i in range(len(sifat_kamu)):
        if (kamu == "selesai"):
            dia = input("Masukkan Sifat Dia  : ")
            sifat_dia.append(dia)
            if (dia == "selesai"):
                set_kamu = set(sifat_kamu)
                set_dia = set(sifat_dia)
                set_kamu.remove("selesai")
                set_dia.remove("selesai")
                print("\tSIFAT KAMU")
                print(set_kamu)
                print("\tSIFAT DIA")
                print(set_dia)
                print("\tPersamaan dari sifat kamu dan dia")
                gabungan = set_kamu.intersection(set_dia)
                print(gabungan)
                berjalan = False         
        
