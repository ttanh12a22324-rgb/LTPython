def tinh_giai_thua(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * tinh_giai_thua(n - 1) 

n = 5
print(f"{n}! = {tinh_giai_thua(n)}")