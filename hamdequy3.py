def tinh_tong(n):
    if n == 1:
        return 1
    return n + tinh_tong(n - 1)

print(f"\nTổng từ 1 đến 10 là: {tinh_tong(10)}")