print("===PROGRAM MIX COLOR RGB===")

warna = input("Masukkan warna pertama: ")
warna1 = input("Masukkan warna kedua: ")

if (warna == "merah" and "warna1 == biru") or (warna == "biru" and "warna1 == merah") :
    print(f"Campuran {warna} dan {warna1} menghasilkan warna ungu") 
elif (warna == "merah" and warna1 == "hijau") or (warna == "hijau" and warna1 == "merah") :
    print(f"Campuran {warna} dan {warna1} menghasilkan warna kuning")
elif (warna == "hijau" and warna1 == "biru") or (warna == "biru" and warna1 == "hijau") :
    print(f"Campuran {warna} dan {warna1} menghasilkan warna cyan")  
else :
    print("PROGRAM MIX COLOR ERROR")