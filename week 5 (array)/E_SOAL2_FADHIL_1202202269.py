print("\tPorsi Terbanyak?")
list_porsi = []

while True:
    porsi = input('Masukkan jumlah porsi ("stop" untuk berhenti) : ')
    if (porsi == "stop"):
        break
    else:
        list_porsi.append(int(porsi))

print(f"Penjualan terbanyak dari satu pelanggan hari ini adalah : {max(list_porsi)}")

