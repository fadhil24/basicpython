def tambah(bil1,bil2,bil3):
    hasil = bil1 + bil2 + bil3
    return hasil
    
def kurang(bil1,bil2,bil3):
    hasil = bil1 - bil2 - bil3
    return hasil

def kali(bil1,bil2,bil3):
    hasil = bil1 * bil2 * bil3
    return hasil

def bagi(bil1,bil2,bil3):
    hasil = bil1 / bil2 / bil3
    return hasil

def show():
    print(f"Hasil Pertambahan ketiga bilangan bulat adalah {tambah(bil1,bil2,bil3)}")
    print(f"Hasil Pengurangan ketiga bilangan bulat adalah {kurang(bil1,bil2,bil3)}")
    print(f"Hasil Perkalian ketiga bilangan bulat adalah {kali(bil1,bil2,bil3)}")
    print(f"Hasil Pembagian ketiga bilangan bulat adalah {bagi(bil1,bil2,bil3)}")

bil1 = int(input("Masukkan bil 1: "))
bil2 = int(input("Masukkan bil 2: "))
bil3 = int(input("Masukkan bil 3: "))
show()

