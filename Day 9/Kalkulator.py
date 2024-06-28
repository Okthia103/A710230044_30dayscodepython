# Kalkulator sederhana untuk penjumlahan, pengurangan, perkalian, dan pembagian

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

print("Pilih operasi matematika:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print("Hasil:", tambah(angka1, angka2))
elif pilihan == '2':
    print("Hasil:", kurang(angka1, angka2))
elif pilihan == '3':
    print("Hasil:", kali(angka1, angka2))
elif pilihan == '4':
    print("Hasil:", bagi(angka1, angka2))
else:
    print("Pilihan tidak valid")
