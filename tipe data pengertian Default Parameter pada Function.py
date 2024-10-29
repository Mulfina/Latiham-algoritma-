# Fungsi dengan parameter default
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# Memanggil fungsi dengan dua argumen
greet("Andi", "Hi")  # Output: Hi, Andi!

# Memanggil fungsi dengan satu argumen
greet("Budi")  # Output: Hello, Budi!