# Operasi dan manipulasi string

# 1. Menyambung string (concatenate)
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + " =" + str(panjang))

# 3. Operator untuk string

# Mengecek apakah ada komponen char / string di string

d = "d"
status = d in nama_lengkap
print(d + " Ada di " + nama_lengkap + " = " + str(status))

# Mengulang string
print("wk"*10)
print(15*"wk")

# Indexing
print("Index ke-0 : " + nama_lengkap[0])
print("Index ke-6 : " + nama_lengkap[6])
print("Index ke-(-1) : " + nama_lengkap[-1])
print("Index ke-(-2) : " + nama_lengkap[-2])
print("Index ke-(-2) : " + nama_lengkap[-2])
print("Index ke-[0:3] : " + nama_lengkap[0:3])
print("Index ke-[3:7] : " + nama_lengkap[3:7])
print("Index ke-[0,2,4,6,8,19] : " + nama_lengkap[0,2,4,6,8,19])

# Item paling kecil
print("Paling kecil : " + min(nama_lengkap))

# Item paling besar
print("Paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. Operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada " + data + " = " + str(jumlah))