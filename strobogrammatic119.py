def la_nguyen_to(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

def xoay180(c):
    bang = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    return bang.get(c, None)

def xoay180_mo_rong(c):
    bang = {'0':'0', '1':'1', '2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}
    return bang.get(c, None)

def la_strobogrammatic(n):
    s = str(n)
    trai, phai = 0, len(s) - 1
    while trai <= phai:
        if xoay180(s[trai]) != s[phai]:
            return False
        trai += 1
        phai -= 1
    return True

def la_strobogrammatic_mo_rong(n):
    s = str(n)
    trai, phai = 0, len(s) - 1
    while trai <= phai:
        if xoay180_mo_rong(s[trai]) != s[phai]:
            return False
        trai += 1
        phai -= 1
    return True

def tinh_so_xoay(n):
    s = str(n)
    ket_qua = ""
    for c in reversed(s):
        x = xoay180(c)
        if x is None:
            return -1
        ket_qua += x
    return int(ket_qua)

def cau_a():
    print("Cau a: So Strobogrammatic chuan < 1,000,000")
    ket_qua = [i for i in range(1000000) if la_strobogrammatic(i)]
    print(*ket_qua)
    print(f"Tong cong: {len(ket_qua)} so\n")

def cau_b():
    print("Cau b: So NGUYEN TO Strobogrammatic chuan < 1,000,000")
    ket_qua = [i for i in range(2, 1000000) if la_strobogrammatic(i) and la_nguyen_to(i)]
    print(*ket_qua)
    print(f"Tong cong: {len(ket_qua)} so\n")

def cau_c():
    print("Cau c: So Strobogrammatic MO RONG < 1,000,000")
    ket_qua = [i for i in range(1000000) if la_strobogrammatic_mo_rong(i)]
    print(*ket_qua)
    print(f"Tong cong: {len(ket_qua)} so\n")

def cau_d():
    print("Cau d: So NGUYEN TO Strobogrammatic MO RONG < 1,000,000")
    ket_qua = [i for i in range(2, 1000000) if la_strobogrammatic_mo_rong(i) and la_nguyen_to(i)]
    print(*ket_qua)
    print(f"Tong cong: {len(ket_qua)} so\n")

def cau_e():
    print("Cau e: So khong phai Strobo, khong nguyen to, nhung so Strobo cua no la nguyen to")
    ket_qua = []
    for i in range(2, 1000000):
        if la_strobogrammatic(i): continue
        if la_nguyen_to(i): continue
        so_xoay = tinh_so_xoay(i)
        if so_xoay > 0 and la_nguyen_to(so_xoay):
            ket_qua.append((i, so_xoay))
    for so, xoay in ket_qua:
        print(f"{so} (xoay->{xoay})", end=" ")
    print(f"\nTong cong: {len(ket_qua)} so\n")

cau_a()
cau_b()
cau_c()
cau_d()
cau_e()