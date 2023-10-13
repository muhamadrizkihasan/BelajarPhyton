# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih besar dari >
print('=== Lebih Besar Dari (>) ===')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# Kurang dari <
print('=== Kurang Dari (<) ===')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# Lebih besar dari sama dengan >=
print('=== Lebih Besar Dari Sama Dengan (>=) ===')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# Kurang dari sama dengan <=
print('=== Kurang dari sama dengan (<=) ===')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# Sama dengan (!==)
print('=== Sama Dengan (==) ===')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# Tidak sama dengan (!=)
print('=== Sama Dengan (!=) ===')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

# 'is' sebagai komparasi object identify
print('=== Object Identify (is)')
x = 5 # Ini adalah assignment membuat object
y = 5
print('Nilai x =', x, ',id = ', hex(id(x)))
print('Nilai y =', y, ',id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5 # Ini adalah assignment membuat object
y = 6
print('Nilai x =', x, ',id = ', hex(id(x)))
print('Nilai y =', y, ',id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)
print('=== Object Identify (is not)')
x = 5 # Ini adalah assignment membuat object
y = 5
print('Nilai x =', x, ',id = ', hex(id(x)))
print('Nilai y =', y, ',id = ', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

x = 5 # Ini adalah assignment membuat object
y = 6
print('Nilai x =', x, ',id = ', hex(id(x)))
print('Nilai y =', y, ',id = ', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)