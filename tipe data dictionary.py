# Membuat dictionary
mahasiswa = {
    "nama": "Andi",
    "umur": 21,
    "jurusan": "Teknik Informatika"
}

print("Dictionary mahasiswa:", mahasiswa)

# Mengakses nilai menggunakan key
print("Nama mahasiswa:", mahasiswa["nama"])
print("Umur mahasiswa:", mahasiswa["umur"])
print("Jurusan mahasiswa:", mahasiswa["jurusan"])

# Menambah pasangan key-value baru
mahasiswa["alamat"] = "Jakarta"
print("Dictionary setelah menambah alamat:", mahasiswa)

# Mengubah nilai menggunakan key
mahasiswa["umur"] = 22
print("Dictionary setelah mengubah umur:", mahasiswa)

# Menghapus pasangan key-value
del mahasiswa["jurusan"]
print("Dictionary setelah menghapus jurusan:", mahasiswa)

# Menggunakan perulangan pada dictionary
print("Data mahasiswa:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")