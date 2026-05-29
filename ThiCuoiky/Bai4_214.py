# Bai 4: Ham an danh (lambda) - So chinh phuong va So hoan thien

import math

is_perfect_square = lambda n: int(math.isqrt(n)) ** 2 == n

is_perfect_number = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

# In cac so chinh phuong tu 1 den 10000
print("=== Cac so chinh phuong tu 1 den 10000 ===")
ds_chinh_phuong = [n for n in range(1, 10001) if is_perfect_square(n)]
print(*ds_chinh_phuong)

# In cac so hoan thien tu 1 den 10000
print("\n=== Cac so hoan thien tu 1 den 10000 ===")
ds_hoan_thien = [n for n in range(1, 10001) if is_perfect_number(n)]
print(*ds_hoan_thien)