# Input User

# Data yang dimasukan pasti string
data = input("Masukan Data : ")
print("Data =", data, ",Type =", type(data))

# Jika kita ingin mengambil int, maka
angka = float(input("Masukan angka: "))
angka = int(input("Masukan angka: "))

print("Data =", angka, ",Type =", type(angka))

# Bagaimana dengan boolean?
biner = bool(int(input("Masukan nilai boolean :")))
print("Data =", biner, ",Type =", type(biner))