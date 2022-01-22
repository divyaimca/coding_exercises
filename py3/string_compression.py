def string_compression(s):
    uniq_chars = []
    i = 0
    j = 0
    while i < len(s):
        char = s[j]
        if char not in uniq_chars: uniq_chars.append(char)
        if char != s[i]:
            #print(f'new char found {s[i]}')
            j = i
        i += 1
    res = []
    #uniq_chars = list(set(s))
    #print(uniq_chars)
    for char in uniq_chars:
        #print(str(s.count(char))+char)
        res.append(str(s.count(char))+char)

    #print(list(map(lambda x: s.count(x)+s, s)))

    return ''.join(res)




    

print(string_compression('AAAAABBBBCCCC'))
print(string_compression('AABBCC'))
print(string_compression('AAABCCDDDDD'))
print(string_compression(''))


