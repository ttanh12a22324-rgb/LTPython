def xoay180(c):
    bang = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    return bang.get(c, None)

def xoay180_mo_rong(c):
    bang = {'0':'0', '1':'1', '2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}
    return bang.get(c, None)

def la_strobogramatic(n):
    s = str(n)
    trai, phai = 0, len(s) - 1
    while trai <= phai:
        if xoay180(s[trai]) != s[phai]:
            return False
        trai += 1
        phai -= 1
    return True

def la_strobogramatic_mo_rong(n):
    s = str(n)
    trai, phai = 0, len(s) - 1
    while trai <= phai:
        if xoay180_mo_rong(s[trai]) != s[phai]:
            return False
        trai += 1
        phai -= 1
    return True

def cau_a(n):
    print(f"Cau a: Tat ca so Strobogramatic gom {n} chu so:")
    bat_dau = 10 ** (n - 1)
    ket_thuc = 10 ** n
    ket_qua = [i for i in range(bat_dau, ket_thuc) if la_strobogramatic(i)]
    print(*ket_qua)
    print(f"Tong cong: {len(ket_qua)} so\n")

def cau_b(n):
    print(f"Cau b: Tat ca so Strobogramatic MO RONG gom {n} chu so:")
    bat_dau = 10 ** (n - 1)
    ket_thuc = 10 ** n
    ket_qua = [i for i in range(bat_dau, ket_thuc) if la_strobogramatic_mo_rong(i)]
    print(*ket_qua)
    print(f"Tong cong: {len(ket_qua)} so\n")

n = int(input("Nhap so chu so n (2 <= n <= 10): "))
if n < 2 or n > 10:
    print("n phai nam trong khoang [2, 10]")
else:
    cau_a(n)
    cau_b(n)