# Bai 4 số lượng chẵn và lẻ
n_str = input("Nhập số nguyên dương n: ")
chan = 0
le = 0

for chu_so in n_str:
    if int(chu_so) % 2 == 0:
        chan += 1
    else:
        le += 1

print(f"Số lượng số lẻ: {le}, Số lượng số chẵn: {chan}")
# Bai 5 Tính tổng và tích các chữ số
n_str = input("Nhập số nguyên dương n: ")
tong = 0
tich = 1

for chu_so in n_str:
    so = int(chu_so)
    tong += so
    tich *= so

print(f"Tổng = {tong}, Tích = {tich}")
# Bai 6 tìm chữ số lớn nhất
n_str = input("Nhập số nguyên dương n: ")

chu_so_lon_nhat = max(n_str)

print(f"Số lớn nhất = {chu_so_lon_nhat}")
# Bai 7 Tìm số may mắn
n_str = input("Nhập số nguyên n: ")
la_may_man = True

for chu_so in n_str:
    if chu_so != '6' and chu_so != '8':
        la_may_man = False
        break 

if la_may_man:
    print(f"{n_str} là số may mắn.")
else:
    print(f"{n_str} KHÔNG phải số may mắn.")