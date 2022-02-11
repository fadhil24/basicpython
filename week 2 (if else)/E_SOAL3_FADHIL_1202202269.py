umur = int(input("Masukkan umur anda : "))

if (umur >= 17 and umur < 20) :
    print("Anda bisa membuat SIM A, SIM C")
elif (umur >= 20 and umur < 23) :
    print("Anda bisa membuat SIM A UMUM")
elif (umur >= 23 ) :
    print("Anda bisa membuat SIM B")
else :
    print("Anda belum bisa membuat SIM")

