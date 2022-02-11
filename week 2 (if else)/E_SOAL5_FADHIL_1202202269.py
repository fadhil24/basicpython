berat = float(input("Masukkan berat badan dalam kg: "))
tinggi = float(input("Masukkan tinggi badan dalam m: "))

BMI = berat / (tinggi * tinggi)

if (BMI < 18.5) :
 print(f"{BMI} termasuk kategori Underweight")
elif (BMI >= 18.5 and BMI <= 24.9) :
 print(f"{BMI} termasuk kategori Normal")
elif (BMI >= 25 and BMI <= 29.9) :
 print(f"{BMI} termasuk kategori Overweight")
elif (BMI >= 30 and BMI <= 34.9) :
 print(f"{BMI} termasuk kategori Obese")
elif (BMI >= 35 and BMI <= 39.9) :
 print(f"{BMI} termasuk kategori Very Obese")
else :
 print(f"{BMI} termasuk kategori Extremely Obese")