
n = int(input('Please enter the number:'))

## 1 < n < 10

for i in range(1,n+1): 
    print(( ((10**i-1)//9)) * (( 10 ** i - 1 ) // 9 ))