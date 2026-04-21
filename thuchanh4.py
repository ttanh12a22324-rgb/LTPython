S = '''    Quê  hương
Quê hương là chùm  khế ngọt.
   Cho con trèo hái  mỗi  ngày.
Quê hương là đường đi học.
  Con về rợp bướm vàng bay.
    Đỗ Trung Quân    '''

lines = S.split('\n')
ket_qua_lines = []

for line in lines:
   
    words = line.split()
    
    if not words: 
        continue
        
    line_clean = " ".join(words)
    
    line_clean = line_clean.replace(" .", ".").replace(" ,", ",")
    
    ket_qua_lines.append(line_clean)

S_hoan_chinh = "\n".join(ket_qua_lines)

print("--- Chuỗi sau khi đã hoàn chỉnh ---")
print(S_hoan_chinh)