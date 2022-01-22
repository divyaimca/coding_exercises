def rev_word(s):
    a = s.split()
    a.reverse()
    return a


print(rev_word('Hi John,   are you ready to go?'))
print(rev_word('    space before'))
print(rev_word('space after     '))
print(rev_word('1'))