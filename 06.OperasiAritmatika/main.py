# Operasi Aritmatika
a = 10
b = 3

# Operasi Penjumlahan +
hasil = a + b
print(a, "+", b, "=", hasil)

# Operasi Pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)

# Operasi Perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# Operasi Pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

# Operasi Modulus %
hasil = a % b
print(a, "%", b, "=", hasil)

# Operasi Eksponen (Pangkat) **
hasil = a ** b
print(a, "**", b, "=", hasil)

# Operasi Floor Division //
hasil = a // b
print(a, "//", b, "=", hasil)

# Prioritas Operasi, Operational Predence
"""
    1. ()
    2. Exponen **
    3. Perkalian dan Teman-Teman * / ** % //
    4. Pertambahan dan Pengurangan + -
"""

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil = x + y * z
print(x, "y", y, "*", z, "=", hasil)

# Kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print("(", x, "+", y, ") *", z, "=", hasil)