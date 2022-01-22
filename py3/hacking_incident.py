import string


def encryption(sstr,n):
    s = sstr.lower()
    print(f'{s} shift {n}')
    


    lis = s.split()
    lis2 = []
    dict1 = {}
    dict2 = {}

    alphabet = string.ascii_lowercase
   # print(alphabet)
    lia2z = list(alphabet)

    for i,j in enumerate(lia2z):
        dict1[i] = j
    
    shiftn = 26 - int(n)

    cipher_alpha = alphabet[shiftn:]+alphabet[:shiftn]
    #print(cipher_alpha)

    for i,j in enumerate(cipher_alpha):
        dict2[i] = j


    
    
    # print(dict1)
    # print(dict2)

    nl = list(s)
    nll = nl.copy()

    for c in range(len(nl)):
        for m,n in dict1.items():
            if n == nl[c]:
                nll[c] =  dict2[m]
    




    print(''.join(nll))



                    
    




#def decryption(s):


if __name__ == '__main__':
    for i  in range(0,27):
        encryption('Get this message to the main server',i)
