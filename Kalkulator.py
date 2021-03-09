import os

def penjumlahan(x, y):
   return x + y

def pengurangan(x, y):
   return x - y

def perkalian(x, y):
   return x * y

def pembagian(x, y):
   return x / y

print("Pilih Pilihan Anda")
print("1.Penjumlah")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

pilihan = input("Masukkan pilihan(1/2/3/4): ")

os.system('cls')

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

if pilihan == '1':
   print(angka1,"+",angka2,"=", penjumlahan(angka1,angka2))
elif pilihan == '2':
   print(angka1,"-",angka2,"=", pengurangan(angka1,angka2))
elif pilihan == '3':
   print(angka1,"*",angka2,"=", perkalian(angka1,angka2))
elif pilihan == '4':
   print(angka1,"/",angka2,"=", pengurangan(angka1,angka2))
else:
   print("Input salah")
