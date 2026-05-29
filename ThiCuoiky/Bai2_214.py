# Bai 2: Cac ham so nguyen to

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def dem_so_nguyen_to(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count

def uoc_so_nguyen_to(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0 and is_prime(i):
            result.append(i)
    return result

# Chuc nang 1: Kiem tra so nguyen to
n1 = int(input("Cho nhap so nguyen duong n (kiem tra so nguyen to): "))
if is_prime(n1):
    print(f"{n1} la so nguyen to")
else:
    print(f"{n1} khong phai so nguyen to")

# Chuc nang 2: Dem so nguyen to < n
n2 = int(input("Cho nhap so nguyen duong n (dem so nguyen to < n): "))
print(f"So luong so nguyen to nho hon {n2} la: {dem_so_nguyen_to(n2)}")

# Chuc nang 3: Uoc so nguyen to cua n
n3 = int(input("Cho nhap so nguyen duong n (liet ke uoc so nguyen to): "))
ds_uoc = [i for i in range(1, n3 + 1) if n3 % i == 0]
print(f"Cac uoc so cua {n3} gom {','.join(map(str, ds_uoc))}. "
      f"Nhung chi in ra: Cac so vua la uoc so cua {n3}, vua la so nguyen to: "
      f"{','.join(map(str, uoc_so_nguyen_to(n3)))}")