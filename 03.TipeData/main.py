# a = 10, a adalah variable dengan nilai 10

# Tipe data: Angka satuan yang gak ada komanya (integer)
data_integer = 1
print("Data :", data_integer)
print("- bertipe :", type(data_integer))

# Tipe data: Angka dengan koma (float)
data_float = 1.5
print("Data :", data_float)
print("- bertipe :", type(data_float))

# Tipe data: Kumpulan karakter (string)
data_string = "Ucup"
print("Data :", data_string)
print("- bertipe :", type(data_string))

# Tipe data: Biner true/false (boolean)
data_bool = True
print("Data :", data_bool)
print("- bertipe :", type(data_bool))

## Tipe data khusus

# Bilangan kompleks
data_complex = complex(5,6)
print("Data :", data_complex)
print("- bertipe :", type(data_complex)) 

# Tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("Data :", data_c_double)
print("- bertipe :", type(data_c_double)) 