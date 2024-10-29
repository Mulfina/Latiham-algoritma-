# Mendefinisikan dua bilangan bulat
a = 60  # 60 dalam biner adalah 0011 1100
b = 13  # 13 dalam biner adalah 0000 1101

# Operator AND (&)
result_and = a & b
print(f'{a} AND {b} = {result_and} (biner: {bin(result_and)})')

# Operator OR (|)
result_or = a | b
print(f'{a} OR {b} = {result_or} (biner: {bin(result_or)})')

# Operator NOT (~)
result_not = ~a
print(f'NOT {a} = {result_not} (biner: {bin(result_not)})')

# Operator XOR (^)
result_xor = a ^ b
print(f'{a} XOR {b} = {result_xor} (biner: {bin(result_xor)})')

# Operator left shift (<<)
result_left_shift = a << 2
print(f'{a} left shift 2 = {result_left_shift} (biner: {bin(result_left_shift)})')

# Operator right shift (>>)
result_right_shift = a >> 2
print(f'{a} right shift 2 = {result_right_shift} (biner: {bin(result_right_shift)})')