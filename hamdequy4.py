import math
def tim_gcd_nhanh(a, b):
    return math.gcd(a, b)
print(f"GCD là: {tim_gcd_nhanh(48, 18)}")
def tim_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
num1 = 48
num2 = 18
print(f"GCD của {num1} và {num2} là: {tim_gcd(num1, num2)}")