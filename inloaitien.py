X = int(input("Nhap so tien X: "))

menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

print(f"So tien {X} duoc doi thanh:")

tong = 0
so_du = X

for tien in menh_gia:
    so_to = so_du // tien
    so_du = so_du % tien
    tong += so_to
    print(f"Loai {tien} gom {so_to} to")

print(f"TONG CONG CO {tong} TO")