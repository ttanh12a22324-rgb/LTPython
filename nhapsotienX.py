def doi_tien(so_tien):
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    print(f"So tien {so_tien} duoc doi thanh:")
    
    tong = 0
    so_loai = 0
    so_du = so_tien
    
    for tien in menh_gia:
        so_to = so_du // tien
        so_du = so_du % tien
        tong += so_to
        
        if so_to > 0:
            print(f"Loai {tien} gom {so_to} to")
            so_loai += 1
    
    print(f"TONG CONG CO {tong} TO")
    print(f"Tong so loai = {so_loai}")
a = int(input("Nhap so tien hang can thu (a): "))
b = int(input("Nhap so tien khach dua (b): "))
 

if a > b:
    print(f"Khach hang con thieu: {a - b}")

elif a == b:
    print("Cam on khach hang. Hen gap lai")

else:  
    tien_thoi = b - a
    doi_tien(tien_thoi)
    input("\nNhan Enter de tiep tuc...")
    print("Cam on khach hang. Hen gap lai")