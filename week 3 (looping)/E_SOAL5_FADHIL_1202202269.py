banyak = int(input("Banyak Ronde? "))
t = 0
b = 0
for i in range(banyak) :
    tami = input("Tami pilih apa? (B/G/K) ").upper()
    boi = input("Boi pilih apa? (B/G/K) ").upper()
    print("")
    if (tami == "B") and (boi == "K") :
        b = b + 1
    elif (tami == "K") and (boi == "B") :
        t = t + 1
    elif (tami == "B") and (boi == "G") :
        t = t + 1
    elif (tami == "G") and (boi == "B") :
        b = b + 1
    elif (tami == "G") and (boi == "K") :
        t = t + 1
    elif (tami == "K") and (boi == "G") :
        b = b + 1
    else :
        t = t + 0
        b = b + 0
else:
    print(f"Selamat Tami menang sebanyak {t}")
    print(f"Selamat Boi menang sebanyak {b}")

    
