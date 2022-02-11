bahan = input("Masukkan bahan: ")

def Bahancelana():
    if (bahan == "Abaka"):
        print("Keluarlah celana tahan air")
    elif (bahan == "Pandan"):
        print("Keluarlah celana yang harum")
    elif (bahan == "Batu"):
        print("Keluarlah celana dengan efek perlindungan maksimal")
    else:
        print(f"Bahan {bahan} tidak diketahui")

Bahancelana()