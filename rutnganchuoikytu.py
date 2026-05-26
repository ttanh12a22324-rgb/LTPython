def decode(cipher_text):
    result = []
    i = 0
    while i < len(cipher_text):
        if cipher_text[i] == '#':
            
            i += 1
            num_str = ''
            while i < len(cipher_text) and cipher_text[i].isdigit():
                num_str += cipher_text[i]
                i += 1
            
            if i < len(cipher_text):
                
                char = cipher_text[i]
                result.append(char * int(num_str))
                i += 1
        else:
            result.append(cipher_text[i])
            i += 1
    return ''.join(result)



print(decode("XY#6Z1#4023"))     
print(decode("#39+1=1#30"))      