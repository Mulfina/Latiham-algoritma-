def tambah(*args):
    total = 0
    for angka in args:
        total += angka
    return total

# Memanggil fungsi dengan berbagai jumlah argumen
print(tambah(1, 2, 3))       # Output: 6
print(tambah(10, 20, 30, 40)) # Output: 100
print(tambah(5))              # Output: 5