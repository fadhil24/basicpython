jagoan = input("Alfian, Masukkan jagoan anda : ").upper()
jagoan1 = input("Nopal, Masukkan jagoan anda : ").upper()

if (jagoan == "jempol" and jagoan1 == "telunjuk") :
    print("ALFIAN MENANG")
elif (jagoan == "telunjuk" and jagoan1 == "jempol") :
    print("NOPAL MENANG")
elif (jagoan == "kelingking" and jagoan1 == "telunjuk") :
    print("NOPAL MENANG")
elif (jagoan == "telunjuk" and jagoan1 == "kelingking") :
    print("ALFIAN MENANG")
elif (jagoan == "kelingking" and jagoan1 == "jempol") :
    print("ALFIAN MENANG")
elif (jagoan == "jempol" and jagoan1 == "kelingking") :
    print("NOPAL MENANG")
elif (jagoan == "jempol" and jagoan1 == "jempol") or (jagoan == "telunjuk" and jagoan1 == "telunjuk") or (jagoan == "kelingking" and jagoan1 == "kelingking") :
    print("Pertandingan Seri")
else :
    print("pilih jagoan yang sesuai")