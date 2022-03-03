from itertools import count
import re

a = "kumar.allcloud@gmail.com"
b = "kmar1234@gmail.com"
c = "192.168.0.108 22"

# with open("mails.txt","w+") as f:
#     for i in range(100):
#         f.write(f"Hello WOrld from : {a}\n")
#         f.write(f"Hello WOrld from : {b}\n")
#         f.write(f"IP and Port to scan :{c}\n")

#obj = re.compile(r'(.*)([a-z]{4}[0-9]{4}@[a-z]{4}.[a-z]{3})(.*)')
mail_regex = r'\b[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-z|AZ]{2,}\b'

counter = 0
file1 = "mails.txt"
with open(file1, "r") as f1:
    for line in f1:
        objSearch = re.search(mail_regex,line)
        #print(objSearch)
        if (objSearch):
            print(objSearch.group())
        # a = obj.search(line)
        # print(a)
        #if a in line:
            counter += 1

print(counter)

    

