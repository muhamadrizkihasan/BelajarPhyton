# Operator bitwise, biner dan binary

a = 9
b = 5

# Bitwise OR (|)
c = a | b
print('\n=========OR==========')
print('Nilai : ', a, ' binary :', format(a, '08b'))
print('Nilai : ', b, ' binary :', format(b, '08b'))
print('----------------------(|)')
print('Nilai : ', c, ' binary :', format(c, '08b'))

# Bitwise AND (&)
c = a & b
print('\n========AND==========')
print('Nilai : ', a, ' binary :', format(a, '08b'))
print('Nilai : ', b, ' binary :', format(b, '08b'))
print('----------------------(&)')
print('Nilai : ', c, ' binary :', format(c, '08b'))

# Bitwise XOR (^)
c = a ^ b
print('\n========XOR==========')
print('Nilai : ', a, ' binary :', format(a, '08b'))
print('Nilai : ', b, ' binary :', format(b, '08b'))
print('----------------------(^)')
print('Nilai : ', c, ' binary :', format(c, '08b'))

# Bitwise NOT (~)
c = ~a
print('\n========NOT==========')
print('Nilai : ', a, ' binary :', format(a, '08b'))
print('----------------------(~)')
print('Nilai : ', c, ' binary :', format(c, '08b'))
print('----------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('Nilai :', e^d, ', binary :', format(e^d, '08b'))

# Shifting

# Shift right (>>)
c = a >> 1
print('\n====================')
print('Nilai :', a, ', binary : ', format(a, '08b'))
print('---------------------- (>>)')
print('Nilai : ', c, ' binary :', format(c, '08b'))

# Shift Left (<<)
c = a << 1
print('\n====================')
print('Nilai :', a, ', binary : ', format(a, '08b'))
print('---------------------- (<<)')
print('Nilai : ', c, ' binary :', format(c, '08b'))