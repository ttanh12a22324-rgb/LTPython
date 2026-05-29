# Bai 3: Ham lambda

import math

la_chinh_phuong = lambda n: int(math.isqrt(n)) ** 2 == n

def loai_tam_giac(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Khong phai tam giac"
    xep_loai = lambda a, b, c: (
        "deu"   if a == b == c else
        "can"   if a == b or b == c or a == c else
        "vuong" if sorted([a**2, b**2, c**2])[0] + sorted([a**2, b**2, c**2])[1] == sorted([a**2, b**2, c**2])[2] else
        "thuong"
    )
    return xep_loai(a, b, c)

# Phan 1: So chinh phuong
n = int(input("Nhap so nguyen n (kiem tra so chinh phuong): "))
if la_chinh_phuong(n):
    print(f"{n} la so chinh phuong")
else:
    print(f"{n} khong phai so chinh phuong")

# Phan 2: Loai tam giac
a, b, c = map(int, input("Nhap 3 canh tam giac (a b c): ").split())
ket_qua = loai_tam_giac(a, b, c)
print(f"Tam giac voi 3 canh {a}, {b}, {c}: {ket_qua}")