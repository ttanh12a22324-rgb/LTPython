from math import gcd

def reverse_num(n):
    return int(str(n)[::-1])

def is_friendly(n):
    rev = reverse_num(n)
    return gcd(n, rev) == 1

a, b = map(int, input("Nhập a, b: ").split())

count = 0
friendly_nums = []

for n in range(a, b + 1):
    if is_friendly(n):
        friendly_nums.append(n)
        count += 1

print("Các số thân thiện:", *friendly_nums)
print("Số lượng:", count)