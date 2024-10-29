# Operator Identitas
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# Operator identitas `is` memeriksa apakah kedua variabel merujuk ke objek yang sama
print("Apakah a is b?", a is b)       # True, karena `b` merujuk ke objek yang sama dengan `a`
print("Apakah a is c?", a is c)       # False, karena `c` adalah objek baru meskipun nilainya sama

# Operator identitas `is not` memeriksa apakah kedua variabel tidak merujuk ke objek yang sama
print("Apakah a is not c?", a is not c)   # True, karena `a` dan `c` adalah objek berbeda

# Operator Keanggotaan
my_list = [1, 2, 3, 4, 5]

# Operator keanggotaan `in` memeriksa apakah sebuah nilai ada dalam koleksi (list, string, dll.)
print("Apakah 3 ada dalam my_list?", 3 in my_list)      # True, karena 3 ada di dalam `my_list`

# Operator keanggotaan `not in` memeriksa apakah sebuah nilai tidak ada dalam koleksi
print("Apakah 6 tidak ada dalam my_list?", 6 not in my_list)  # True, karena 6 tidak ada di dalam `my_list`