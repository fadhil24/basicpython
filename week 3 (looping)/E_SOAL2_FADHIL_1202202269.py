print("\t== COUNTDOWN SIMPLE ==")
batas = int(input("Masukkan angka: "))

for i in range(batas):
    print(batas)
    batas = batas - 1
    if (batas == 1) :
        print("It's enough.")
        break