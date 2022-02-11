bebas = [1,2,3,4,5]

def getIndex():
    try:
        index = int(input("Masukkan index ke :"))
        print(f"Data index ke-{index} adalah {bebas[index]}")
    except IndexError:
        print("Index tidak ada")
getIndex()
