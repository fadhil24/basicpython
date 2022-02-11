try:
    gen = input("Masukkan Nama Gen (minimal 5 huruf) : ")
    assert len(gen)>5
    anggota = int(input(f"Masukkan jumlah anggota Gen {gen} (tidak boleh 0) : "))
    assert anggota != 0
except AssertionError:
    print("Isi sesuai dengan ketentuan yang diberikan")
finally:
    print("Percobaan Program Selesai")