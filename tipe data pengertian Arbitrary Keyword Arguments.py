def cetak_info(**kwargs):
    for kunci, nilai in kwargs.items():
        print(f"{kunci}: {nilai}")

cetak_info(nama="Alice", umur=30, kota="Jakarta")