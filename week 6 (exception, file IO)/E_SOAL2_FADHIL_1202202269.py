print("===OPERASI PEMBAGIAN===")
try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    hasil = angka1/angka2
    print(f"Hasil pembagian : {hasil}")
except ZeroDivisionError:
    print("Anda tidak dapat membagi bilangan dengan angka 0")

