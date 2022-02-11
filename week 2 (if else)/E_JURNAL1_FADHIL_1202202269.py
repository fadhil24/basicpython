umur = int(input("Masukkan umur = "))

if (umur >= 0 and umur <= 5) :
    print("Balita")
elif (umur >= 6 and umur <= 13) :
    print("Anak Anak")
elif (umur >= 14 and umur <= 17) :
    print("Remaja")
elif (umur >= 18 and umur <= 59) :
    print("Dewasa")
elif (umur >= 60) :
    print("Lansia")
else :
    print("Inputan Salah")