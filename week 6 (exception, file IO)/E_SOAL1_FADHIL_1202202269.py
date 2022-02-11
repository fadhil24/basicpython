try:
    bil1 = int(input("Masukkan Bilangan 1 : "))
    bil2 = int(input("Masukkan Bilangan 2 : "))
    hasil = bil1/bil2
    print(f"Total hasil pembagian adalah {hasil}")
except ValueError:
    print("Tipe data kamu tidak sesuai!")
except ZeroDivisionError:
    print("Program tidak dapat membagi operasi pembagian dengan nol")