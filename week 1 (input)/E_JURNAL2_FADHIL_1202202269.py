print("=== Program Konversi Suhu ===")
suhu = float(input("Masukkan Suhu Reamur: "))

celicus = (4/5) * suhu
fahrenheit = (9/4) * (suhu + 32)
kelvin = ((5/4) * suhu) + 273

print(str(suhu) + " Reamur Ke Celcius: " + str(celicus))
print(str(suhu) + " Reamur Ke Fahrenheit: " + str(fahrenheit))
print(str(suhu) + " Reamur Ke Kelvin: " + str(kelvin))