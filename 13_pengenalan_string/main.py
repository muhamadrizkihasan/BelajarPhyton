data = "Ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = 'Menggunakan double quote'
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("Ini adalah hari jum'at")

# 2. Menggunakan tanda \ (Backslash)

# Membuat tanda ' menjadi string
print('Mari shalat jum\'at')
print('g\'day, isn\'t it?')

# Backslash
print("C:\\user\\hasan")

# Tab
print("Rizki\t\t\tikyy, semakin jauhan")

# Backspace
print("Rizki \ikyy, jadi deketan")

# Newline
print("Baris pertama.\nBaris kedua.") # LF -> Line Feed -> unix, macos, linux
print("Baris pertama.\rBaris kedua.") # CR -> Carriage Return -> commodore, acorn, lisp
print("Baris pertama.\r\nBaris kedua.") # CRLF -> Line Feed Carriage Return -> Dipakai oleh windows

# 3. Strinh literal / raw

# Hati-hati
print('C:\new Folder') # Akan salah pathnya

# Menggunakan raw string
print(r'C:\new Folder')

# Multiline literal string
print("""
    Nama  : Hasan
    Kelas : 2 SMK  
""")

# Multiline literal sring dan raw
print("""
    Nama    : Hasan
    Kelas   : 2 SMK \new normal
    website : www.ikyy.com/newID 
""")