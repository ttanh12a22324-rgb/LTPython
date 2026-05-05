numbers = []
while True:
    n = int(input("Nhập số nguyên dương: "))
    numbers.append(n)
    
    tiep = input("Bạn có muốn nhập nữa không? (Y/N): ")
    if tiep.upper() == "N":
        break
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\na) Các số nguyên tố:", [x for x in numbers if is_prime(x)])
am = [x for x in numbers if x < 0]
duong = [x for x in numbers if x > 0]

if am:
    print(f"b) Trung bình các số âm: {sum(am)/len(am):.2f}")
else:
    print("b) Không có số âm")

if duong:
    print(f"   Trung bình các số dương: {sum(duong)/len(duong):.2f}")
print(f"c) Số lớn nhất: {max(numbers)}, Số nhỏ nhất: {min(numbers)}")
tang_dan = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
print(f"d) Danh sách {'đã' if tang_dan else 'chưa'} được sắp xếp tăng dần")