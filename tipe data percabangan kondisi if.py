# Meminta input dari pengguna
nilai = int(input("Masukkan nilai Anda: "))

# Mengecek kondisi
if nilai >= 90:
    print("Nilai Anda A")
elif nilai >= 80:
    print("Nilai Anda B")
elif nilai >= 70:
    print("Nilai Anda C")
elif nilai >= 60:
    print("Nilai Anda D")
else:
    print("Nilai Anda E")