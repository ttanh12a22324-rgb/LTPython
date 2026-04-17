# bai1 5.3
# Cau 1
# 1. Nhập dữ liệu dùng float.
dai = float(input("Nhập chiều dài đáy hình chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
so_le = int(input("Số lượng số lẻ cần hiển thị: "))

# 2. Tính toán
dien_tich_day = dai * rong
the_tich = dien_tich_day * cao

# 3. Xuất kết quả
print(f"Diện tích đáy hình chữ nhật = {dien_tich_day:.{so_le}f}cm2")
print(f"Thể tích hình khối = {the_tich:.{so_le}f}cm3")
# Cau 2
# 1. Nhập 3 số nguyên
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

# 2. Tìm số nhỏ nhất và lớn nhất
so_nho_nhat = min(a, b, c)
so_lon_nhat = max(a, b, c)

# 3. Tìm số ở giữa (Tổng 3 số trừ đi số lớn nhất và nhỏ nhất)
so_giua = (a + b + c) - so_nho_nhat - so_lon_nhat

# 4. Xuất kết quả bằng phương thức format
print("Ba số theo thứ tự tăng dần là: {0}, {1}, {2}".format(so_nho_nhat, so_giua, so_lon_nhat))

# Cau 3
# 1. Nhập số nguyên dương từ 1-9
a = int(input (u'Nhập số nguyên a : ' ))
print('{x} + {y} + {z} = {s}'.format(x=a,y=a*11,z=a*111,s=a + a*11 +a*111) )