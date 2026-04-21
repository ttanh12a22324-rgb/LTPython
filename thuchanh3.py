S = '''Chiều chiều trước bến Văn Lâu
Ai ngồi, ai câu, ai sầu, ai thảm
Ai thương, ai cảm, ai nhớ, ai trông
Thuyền ai thấp thoáng ven sông
Đưa câu mái đẩy chạnh lòng nước non'''
word = 'ai'

danh_sach_tu = S.split()
dem = 0
for tu in danh_sach_tu:
    
    if tu.strip(",.") == word.lower():
        dem += 1

print(f"số từ {word} là {dem}")