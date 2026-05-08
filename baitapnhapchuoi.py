S = input("Nhập chuỗi: ")

words = S.split()
seen = set()
result = None

for word in words:
    if word in seen:
        result = word
        break
    seen.add(word)

print(result)