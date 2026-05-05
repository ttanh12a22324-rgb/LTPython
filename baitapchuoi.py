from collections import Counter

s1 = input("Nhập chuỗi S1: ")
s2 = input("Nhập chuỗi S2: ")

counter1 = Counter(s1)
counter2 = Counter(s2)
common = counter1 & counter2
print("\na) Ký tự xuất hiện trong cả 2 chuỗi:")
print(set(common.keys()))
only_in_s1 = set(counter1.keys()) - set(counter2.keys())
only_in_s2 = set(counter2.keys()) - set(counter1.keys())
print("\nb) Số ký tự có trong S1 nhưng không có trong S2:", len(only_in_s1))
print("   Số ký tự có trong S2 nhưng không có trong S1:", len(only_in_s2))
print("\nc) Ký tự có trong S1 nhưng không có trong S2:", only_in_s1)
print("   Ký tự có trong S2 nhưng không có trong S1:", only_in_s2)