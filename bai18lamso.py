import math
is_than_thien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1
is_chinh_phuong = lambda n: int(n ** 0.5) ** 2 == n
is_dong_nhat_all = lambda n: all(c == str(n)[0] for c in str(n))
is_dong_nhat_any = lambda n: not any(c != str(n)[0] for c in str(n))
is_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n
is_phong_phu = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) > n
is_tang_dan = lambda n: all(str(n)[i] < str(n)[i+1] for i in range(len(str(n)) - 1))
is_armstrong = lambda n: sum(int(d) ** len(str(n)) for d in str(n)) == n
is_nto_c1 = lambda n: sum(1 for i in range(1, n + 1) if n % i == 0) == 2
is_nto_c2 = lambda n: sum(i for i in range(1, n + 1) if n % i == 0) == n + 1
is_nto_c3 = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(n ** 0.5) + 1))
def is_nto_c4(k):
    uoc_so = list(filter(lambda i: k % i == 0, range(1, k + 1)))
    return len(uoc_so) == 2
is_nto = is_nto_c3
is_palindrome = lambda n: str(n) == str(n)[::-1]
is_nto_palindrome = lambda n: is_nto(n) and is_palindrome(n)
is_loc_phat_all = lambda n: all(c in '68' for c in str(n))
is_loc_phat_count = lambda n: str(n).count('6') + str(n).count('8') == len(str(n))
is_loc_phat_palindrome = lambda n: is_loc_phat_all(n) and is_palindrome(n)
def in_ket_qua(ten, ham, gioi_han=1_000_001):
    print("=" * 60)
    print(f"{ten}:")
    print("=" * 60)
    for i in range(1, gioi_han):
        if ham(i):
                    
            print(i, end=" ")
    print("\n")


in_ket_qua("a) Số thân thiện", is_than_thien)
in_ket_qua("b) Số chính phương", is_chinh_phuong)
in_ket_qua("c) Số đồng nhất (dùng all)", is_dong_nhat_all)
in_ket_qua("d) Số hoàn thiện", is_hoan_thien)
in_ket_qua("e) Số phong phú", is_phong_phu)
in_ket_qua("f) Số tăng dần", is_tang_dan)
in_ket_qua("g) Số Armstrong", is_armstrong)
in_ket_qua("h) Số nguyên tố (cách 3 - nhanh nhất)", is_nto_c3)
in_ket_qua("i) Số Palindrome", is_palindrome)
in_ket_qua("j) Số nguyên tố Palindrome", is_nto_palindrome)
in_ket_qua("k) Số lộc phát (dùng all)", is_loc_phat_all)
in_ket_qua("l) Số lộc phát Palindrome", is_loc_phat_palindrome)