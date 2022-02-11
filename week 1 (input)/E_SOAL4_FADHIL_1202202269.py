Hargaperkilo = 8000
jumlahBuah = int(input("Masukkan berat buah : "))
HargaBelumDiskon = Hargaperkilo * jumlahBuah
HargaUdahDiskon = HargaBelumDiskon - (HargaBelumDiskon * 0.15)

print("Harga sebelum diskon : Rp. " + str(HargaBelumDiskon))
print("Harga setelah diskon : Rp. " + str(HargaUdahDiskon))