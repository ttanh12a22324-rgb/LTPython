import datetime
now = datetime.datetime.now()
print(f"Năm hiện tại: {now.strftime('%Y')}")
print(f"Tháng hiện tại bằng chữ: {now.strftime('%B')}")
print(f"Tuần thứ mấy trong năm: {now.strftime('%U')}")
print(f"Tuần thứ mấy trong tháng: {(now.day - 1) // 7 + 1}")
print(f"Ngày thứ mấy trong năm: {now.strftime('%j')}")
print(f"Ngày dương lịch hiện tại: {now.strftime('%d')}")
print(f"Thứ của ngày hiện tại: {now.strftime('%A')}")
print(f"Giờ phút giây hiện tại: {now.strftime('%H:%M:%S')}")
from datetime import date
print("Nhập ngày thứ 1:")
d1 = int(input("Ngày: "))
m1 = int(input("Tháng: "))
y1 = int(input("Năm: "))
print("Nhập ngày thứ 2:")
d2 = int(input("Ngày: "))
m2 = int(input("Tháng: "))
y2 = int(input("Năm: "))
ngay1 = date(y1, m1, d1)
ngay2 = date(y2, m2, d2)
khoang_cach = abs((ngay2 - ngay1).days)
print(f"Số ngày cách nhau giữa 2 ngày là: {khoang_cach} ngày")
import datetime

S = 'Sep 18 2019 2:43PM'

kieu_ngay = datetime.datetime.strptime(S, '%b %d %Y %I:%M%p')

print(f"Dữ liệu sau khi chuyển đổi: {kieu_ngay}")
print(f"Kiểu dữ liệu: {type(kieu_ngay)}")
import datetime

bay_gio = datetime.datetime.now()
print(f"Thời gian hiện tại: {bay_gio.strftime('%H:%M:%S')}")

thoi_gian_moi = bay_gio + datetime.timedelta(seconds=5)

print(f"Thời gian sau khi thêm 5 giây: {thoi_gian_moi.strftime('%H:%M:%S')}")