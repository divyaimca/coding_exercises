def uniq_characters(s):
    return(all(list(map(lambda x: s.count(x) == 1, s))))
       

if __name__ == '__main__':
    print(uniq_characters('abcdefg'))
    print(uniq_characters('goo'))
    print(uniq_characters(''))

