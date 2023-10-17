# Kita belajar casting
# Merubah dari satu tipe ke tipe lain
# Tipe data = int, float, str, bool

## INTEGER
print("=====INTEGER======")
data_int = 9
print("Data = ", data_int, ", Type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # Akan false jika nilai int = 0
print("Data = ", data_float, ", Type = ", type(data_float))
print("Data = ", data_str, ", Type = ", type(data_str))
print("Data = ", data_bool, ", Type = ", type(data_bool))

## FLOAT
print("=====FLOAT======")
data_float = 9.5
print("Data = ", data_float, ", Type = ", type(data_float))

data_int = int(data_float) # Akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) # Akan false jika nilai int = 0
print("Data = ", data_int, ", Type = ", type(data_int))
print("Data = ", data_str, ", Type = ", type(data_str))
print("Data = ", data_bool, ", Type = ", type(data_bool))

## BOOLEAN
print("=====BOOLEAN======")
data_bool = 9.5
print("Data = ", data_bool, ", Type = ", type(data_bool))

data_int = int(data_bool) # Akan dibulatkan kebawah
data_str = str(data_bool)
data_float = float(data_float) # Akan false jika nilai int = 0
print("Data = ", data_int, ", Type = ", type(data_int))
print("Data = ", data_str, ", Type = ", type(data_str))
print("Data = ", data_float, ", Type = ", type(data_float))

## STRING
print("=====STRING======")
data_str = "10"
print("Data = ", data_str, ", Type = ", type(data_str))

data_int = int(data_str) # String harus angka
data_float = float(data_str) # String harus angka
data_bool = bool(data_str) # False jika string kosong
print("Data = ", data_int, ", Type = ", type(data_int))
print("Data = ", data_float, ", Type = ", type(data_float))
print("Data = ", data_bool, ", Type = ", type(data_bool))