def compress(text):
    """Nén chuỗi bằng RLE"""
    if not text:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result.append(f"{count}{text[i-1]}")
            count = 1
    result.append(f"{count}{text[-1]}")
    
    return "".join(result)


def decompress(compressed):
    """Giải nén chuỗi RLE về ban đầu"""
    result = []
    i = 0
    
    while i < len(compressed):
        num_str = ""
        while i < len(compressed) and compressed[i].isdigit():
            num_str += compressed[i]
            i += 1
        
        if num_str and i < len(compressed):
            result.append(compressed[i] * int(num_str))
            i += 1
