import math
# a)
bai_a = lambda n: abs(n)
print("a) Trị tuyệt đối của -5:", bai_a(-5))
# b) 
bai_b = lambda n: n + 15
print("b) 10 + 15 =", bai_b(10))
# c) 
bai_c = lambda x, y: x * y
print("c) Tích 4 x 5 =", bai_c(4, 5))
# d) 
bai_d = lambda n: n % 13 == 0 or n % 19 == 0
print("d) 39 có là bội của 13 hay 19?", bai_d(39))
# e) 
bai_e = lambda r: math.pi * r**2
print("e) Diện tích hình tròn r=3:", round(bai_e(3), 2))
# f) 
bai_f = lambda d, r: (d + r) * 2
print("f) Chu vi hình chữ nhật 4x5:", bai_f(4, 5))
# g) 
bai_g = lambda n: n >= 0 and math.sqrt(n) == int(math.sqrt(n))
print("g) 16 có là số chính phương?", bai_g(16))
