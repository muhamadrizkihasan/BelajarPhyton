# Operator dalam bentuk methods

## Merubah case dari string

# Merubah semua ke upper case
salam = "bro!"
print("Normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# Merubah semua ke lower case
alay = "aKu KeCe AbieezZzZZZZZ"
print("Normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## Pengecekan dengan isX method

# Contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha()   <-- Untuk mengecek semuanya huruf
# isalnum()   <-- Huruf dan angka
# isdecimal() <-- Angka saja
# isspace()   <-- Spasi, tab, newline \n
# istitle()   <-- Semua kata dimulai dengan huruf besar 

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # Hasil bool
print(judul + " is title = " + str(cek_judul))

# Ngecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## Penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# Alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(20, ":")
print("'" + tengah + "'")

# Kebalikannya -> strip()
tengah = "tengah".strip(":") # Menghilangkan tanda :
print("'" + tengah + "'")