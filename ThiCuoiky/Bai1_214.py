# Bai 1: Tinh dien tich day va the tich hinh khoi chu nhat

dai = float(input("Nhap chieu dai day hinh khoi chu nhat (cm):>? "))
rong = float(input("Nhap chieu rong day hinh khoi chu nhat (cm):>? "))
cao = float(input("Nhap chieu cao hinh khoi chu nhat (cm):>? "))
so_le = int(input("So luong so le can hien thi:>? "))

dien_tich = dai * rong
the_tich = dai * rong * cao

print(f"Dien tich day hinh chu nhat = {dien_tich:.{so_le}f} cm\u00b2")
print(f"The tich hinh khoi= {the_tich:.{so_le}f} cm\u00b3")