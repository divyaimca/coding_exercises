
passwd = "Abcd123@"

c_cap, c_sma, c_spe, c_num = 0,0,0,0

if len(passwd) >= 8:
    for l in passwd:
        if l.isnumeric():
            c_num += 1
        elif l.isupper():
            c_cap += 1
        elif l.isalpha():
            c_sma += 1
        elif l in ["@","_"]:
            c_spe += 1
        else:
            print("Pleasesupply a pass woth atleast a cap, a small, a num, a special")
    
else:
    print("Password should be atleast 8 char length")

if (c_cap > 0) and (c_sma > 0) and (c_spe > 0) and (c_num > 0):
    print("Valid")
else:
    print("Invalid")