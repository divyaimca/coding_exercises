import random
import calendar
import math
import time
import re
import string
from forex_python.converter import CurrencyRates
import qrcode
import numpy


def hello_world():
    print("Hello World")

def sum_div():
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))

    print(f"Sum of {a} and {b} is : {a + b} \nDivision of {a} and {b} is {a/b}")

def area_of_triangle():
    a = float(input("Enter height of triangle:"))
    b = float(input("Enter base of triangle:"))

    print(f"Area of traingle is {0.5*a*b}")

def swap_var():
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    
    print(f"Before swap a is {a} and b is {b}")
    temp  = a
    a = b
    b = temp
    print(f"Before swap a is {a} and b is {b}")

def random_num():
    print(f"Random Number between 1 and 100 : {random.randint(1,100)}")

def km_2_mile():
    a = float(input("Enter distance in kilometer:"))

    print(f"1 Kilometer is 0.621371 mile\n{a} KM distance is {a*.621371} in miles")

def celcisus_2_faren():
    a = float(input("Enter temp. in celcisus:"))

    print(f"{a} degree celcius is {(a*1.8)+32} Farenhit")

def calend():
    year = int(input("Enter year :"))
    month = int(input("Enter month :"))

    print(f"Calender is \n {calendar.month(year, month)}")

def quadratic_eq():
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:")) 
    c = float(input("Enter third number:"))    
   

def swap_var2():
    a = float(input("Enter first number:"))   
    b = float(input("Enter second number:"))
    print(f"Before swap a is {a} and b is {b}")
    a,b = b, a    
    print(f"Before swap a is {a} and b is {b}")
 

def int_type():
    a = int(input("Enter first number:")) 
    if (a < 0): 
        print(f" {a} is negative") 
    elif a == 0: 
        print(f"{a} is zero") 
    else:
        print(f" {a} is positive")   

def odd_even():
    a = int(input("Enter first number:")) 
    if a % 2 == 0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")

def leap_year():
    year = int(input("Enter the year :"))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
            print(f"{year} is a leap year") 
    else:
        print(f"{year} is not a leap year")                  


def isPrime():
    num = int(input("Enter the number :"))
    #li = []
    flag = False
    if num == 1:
        print(f"{num} is not prime")  
    elif num > 1:
        for i in range(2,num):
            if num % i == 0:
                #li.append("not prime")
                #print(f"{num} is not prime")
                flag = True
                break

    #if li.count("prime") == len(li):
    if flag:
        print(f"{num} is not prime")              
    else:
        print(f"{num} is prime")

     
def all_prime_in_range():
    a = int(input("Enter first number:"))   
    b = int(input("Enter last number:"))

    li = []
    def isPrime(n):
        flag = True
        if n == 1:
            return(False)
        if n > 1:
            for i in range(2,n):
                if n % i == 0:
                    flag = False
                    break
        return(flag)
    
    print(f"Prime number between {a} and {b} are : ")

    for i in range(a,b):
        if isPrime(i):
            print(i)

def factorial():
    num = int(input("Enter the number :"))
    factorial = 1
    if num <= 1:
        print(f"No factorial for negative number")
    elif num == 0:
        print(f"Factorial is 0")
    else:
        for i in range(1,num+1):
            factorial = factorial * i
        print(f"Factorial of {num} is : {factorial}")

def multi_table():
    num = int(input("Display multiplication table of :"))
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

def fibonacci():
    num = int(input("How many fibonacci sequence to show :"))
    sum, n1, n2 = 0, 0, 1
    if num <= 0:
        print(f"Positive numbers only")
    elif num == 1:
        print(f"Fibonacci sequenc is : \n{n2}")
    else:
        print(f"Fibonacci sequenc is : ")
        print(n1,"\n",n2)
        for i in range(num-2):
            sum = n1 + n2
            print(sum)
            n1 = n2
            n2 = sum

def isArmstrong1(num):
    #num = int(input("Enter number to check armstrong :"))
    po = len(str(num))
    sum = 0
    for i in str(num):
        sum = sum + int(i)**po

    ##     
    if (num == sum):
        #print(f"{num} is Armstrong number")
        return(True)
    else:
        #print(f"{num} is not an Armstrong number")
        return(False)

def all_armstrong_in_range():
    a = int(input("Enter first number:"))   
    b = int(input("Enter last number:"))

    for num in range(a,b):
        if isArmstrong1(num):
            print(num)

def sum_of_nums():
    a = int(input("Enter the number:"))  
    sum = 0
    for i in range(1, a+1):
        sum = sum + i
    print(f"Sum of all natural numbers upto {a} is {sum}")

def ascii_value():
    a = str(input("Enter the chracter:"))  
    print(f"The ASCII value of {a} is {ord(a)}")


def decimal_2_bin_oct_hex():
    a = int(input("Enter a decimal number:"))
    print(f"The binary of {a} is : {bin(a)}")
    print(f"The octal of {a} is : {oct(a)}")
    print(f"The hexadecimal of {a} is : {hex(a)}")

def compute_hcf(a,b):
    #a = int(input("Enter first number: "))   
    #b = int(input("Enter second number: "))
    li = []
    for i in range(1,min(a,b)):
        if a % i == 0 and b % i == 0:
            li.append(i)
    #print(f"H.C.F of {a} and {b} is {max(li)}")
    return(max(li))        

def compute_lcm():
    a = int(input("Enter first number: "))   
    b = int(input("Enter second number: "))

    print(f"L.C.M of {a} and {b} is {int((a*b)/compute_hcf(a,b))}")
def simple_calculator():
    while True:    
        try:
            a = int(input("Enter first number: "))   
            b = int(input("Enter second number: "))
        except Exception as err:
            print("Please enter a valid number")
            print(err)
            break
            
        print("""
            Please Enter choice for each operation :
            1. Add
            2. Subtract
            3. Multiply
            4. Divide        
            """)   
        choice = int(input("Operation Selected : "))
        if choice not in [1,2,3,4]:
            print("Enter a valid choice")
        elif choice == 1:
            print(f"{a} + {b} = {a+b}")
        elif choice == 2:
            print(f"{a} - {b} = {a-b}")
        elif choice == 3:
            print(f"{a} x {b} = {a*b}")
        elif choice == 4:
            print(f"{a} % {b} = {a/b}")
        
        try:
            repeat = str(input("Do you want to repeat : (yes/no)"))
        except Exception as err:
            print("Please enter a valid option (yes/no)")
            print(err)
        if repeat == "no":
            break

def fibo_recursion():
    def fibo_func(n):
        if n <= 1:
            return n
        else:
            return(fibo_func(n-1)+fibo_func(n-2))
        
    a = int(input("Enter the sequence number > 0: "))
    print(f"Fibonacci sequence : ")
    for i in range(a):
        print(fibo_func(i))   
 
def factorial_recusion():
    def fact(n):
        if n <= 1:
            return(n)
        else:
            return(n*fact(n-1))
    a = int(input("Enter the sequence number > 0: "))
    print(f"Factorial of {a} is : {fact(a)}")

def count_bmi():
    h = float(input("Enter your height in meters: "))
    w = float(input("Enter your weight in kg: "))

    bmi = round(w/(h**2),2)    

    print("Your BMI is: ", bmi)
    if bmi <= 18.5:
        print("You are underweight.")
    elif 18.5 < bmi <= 24.9:
        print("Your weight is normal.")
    elif 25 < bmi <= 29.29:
        print("You are overweight.")
    else:
        print("You are obese.")

def logarthim():
    num = float(input("Enter the number: "))
    if num <= 0:
        print(f"Please enter a positive number")
    else:
        print(f"Natural logarthim of {num} is : {math.log(num)}")    

def cube_sum():
    num = int(input("Enter the number: "))
    total = sum(i**3 for i in range(1,num+1))
    print(f"Cube sum of {num} is {total}")

def arr_sum():
    arr = [1,2,3,4,33,4,4,4,4,55,45,65,789,1,2,4555,9,34]
    print(f"Array sum using inbuilt function is : {sum(arr)}")

    total = 0
    for i in arr: 
        total += i
    print(f"Array sum using manual add  is : {total}")
    
def large_in_arr():
    arr = [98989,1,2,3,4,33,4,4,4,4,55,45,65,789,1,2,4555,9,34,9999999999,98]
    print(f"The largest element in the array  using max : {max(arr)}")

    large = arr[0]
    for i in arr:
        if large < i:
            large = i
    print(f"The largest element in the array using loop : {large}")

def valid_passwords():
    passwords = str(input("Enter passwords separated by comma : ")).split(',')
    for paswd in passwords:
        #print(f"Validating {paswd}")
        if 6 <= len(paswd) <= 12: 
            if re.match(r"^(?=.*[a-z])(?=.*[$#@])(?=.*[0-9])(?=.*[A-Z])",paswd):
                print(f"{paswd} is valid")

def count_types():
    word = str(input("Enter the sentence in which counting needed :"))

    letters = []
    digits = []
    for char in word:
        if char in string.digits:
            digits.append(char)
        elif char in string.ascii_letters:
            letters.append(char)

    print(f"Letters {len(letters)} \nDigits {len(digits)}") 

def rotate_array():
    array = [1,2,3,4,5]
    rotate_by = 2
    
    print(array[rotate_by::]+array[:rotate_by:]) 

def monotonic_array():
    def isMonotonic(arr):
        increase = decrease = True
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                decrease = False
            elif arr[i] < arr[i-1]:
                increase = False

        return(increase or decrease)        

    arr1 = [1, 2, 2, 3] # Monotonic (non-decreasing)
    arr2 = [3, 2, 1] # Monotonic (non-increasing)
    arr3 = [1, 3, 2, 4] # Not monotonic
    print("arr1 is monotonic:", isMonotonic(arr1))
    print("arr2 is monotonic:", isMonotonic(arr2))
    print("arr3 is monotonic:", isMonotonic(arr3)) 

def add_mul_matrix():

    matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]
    new_add_matrix = []
    new_mul_matrix = []
    for i in range(3):
        row1 = []
        row2 = []
        for j in range(3):
            row1.append(matrix1[i][j]+matrix2[i][j])
            row2.append(matrix1[i][j]*matrix2[i][j])
        new_add_matrix.append(row1)
        new_mul_matrix.append(row2)

    print(matrix1)
    print(matrix2)
    print(f"sum of matrices {new_add_matrix}")
    print(f"multiplication of matrices {new_mul_matrix}")

def sorted_words():
    words = input("Enter a string: ").split()
    words.sort()    
    for word in words:
        print(word.capitalize())

def remove_punct():
    word = input("Enter a string: ")
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    new_word = ""
    for char in word:
        if char not in punctuations:
            new_word += char

    print(new_word)

def isDiasarium(num):
    #num = int(input("Enter the number to check :"))
    sum = 0
    for i in str(num):
        sum += int(i)**(int(str(num).index(i))+1)

    return(sum == num)

def isDiasariumRange():
    num1 = int(input("Enter the first num :"))
    num2 = int(input("Enter the last num :"))
    print([i for i in range(num1,num2) if isDiasarium(i)])

def isHappyNum(num):
    #num = int(input("Enter the num :"))
    def isHappy(n):
        nums = set()
        while n != 1 and n not in nums:
            nums.add(n)
            n = sum(int(i)**2 for i in str(n))
        return(n == 1)    

    return(isHappy(num))
    #if isHappy(num):
    #    print(f"{num} is a Happy Number")
    #else:
    #    print(f"{num} is not a Happy Number")

def isHappyNumRange():
    num1 = int(input("Enter the first num :"))
    num2 = int(input("Enter the last num :"))
    
    print([i for i in range(num1,num2) if isHappyNum(i)])  

def isHarshad():
    num = int(input("Enter the  number :"))

    summ = sum(int(i) for i in str(num))
    if num % summ == 0:
        print(f"{num} is a Harshad Number.")
    else:
        print(f"{num} is not a Harshad Number.")
    
def random_password():
    num = int(input("Enter the  number :"))

    print(f"Random Password  of length {num} : {''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k = num))}")

def currency_converter():
    currency = CurrencyRates()

    amount = float(input("Enter the  amount to convert :"))
    from_currency = str(input("Enter the  from_currency e.g. INR, USD, EUR : "))
    to_currency = str(input("Enter the  to_currency e.g. INR, USD, EUR : "))

    converted_amount = currency.convert(from_currency, to_currency, amount)
    print(f"======\n{amount} {from_currency} = {converted_amount} {to_currency}")

def generate_qrcode():

    string_2_qr = str(input("Enter the string to generate QRCODE : "))

    data = "https://thegnulinuxguy.wordpress.com/"
    image = qrcode.make(string_2_qr)
    image.save("qr.png")

def pronic_number_range():
    num1 = int(input("Enter the first num :"))
    num2 = int(input("Enter the last num :"))

    print(f"Pronic numbers between {num1} and {num2} are :")
    for i in range(num1,num2):
        pro = i * (i+1)
        if pro > num2:
            break
        print(pro)
def sum_mul_list():
    numbers = [10, 20, 30, 40, 50]

    print(f"Sum of all numbers in {numbers} is : {sum(numbers)}")
    print(f"Mul of all numbers in {numbers} is : {numpy.prod(numbers)}")

def smallest_in_list():
    numbers = [10, 20, 30, 40, 50,1,5,2,0,9]

    print(min(numbers))

    small = numbers[0]
    for i in range(len(numbers)):
        if small > numbers[i]:
            small = numbers[i]

    print(f"smallest number in {numbers} is : {small}") 
    
            
    



if __name__ == "__main__":
    currency_converter()






