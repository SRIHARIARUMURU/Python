# 1. Write a program to print the sum of all even numbers between 1 and 100.
def even_num(st,sp):
    sum=0
    for i in range(st,sp+1):
        if i%2==0:
            sum+=i
    return sum
print(even_num(1,100))

#Output:
2550
# ...............................................................................................
# 2. Write a program that prints the first 10 powers of 2 using a loop.
def power_num(num):
    res=0
    for i in range(1,num+1):
        res=2**i
        print(res,end=" ")
    return ""
print(power_num(10))

Output:
2 4 8 16 32 64 128 256 512 1024 
# ...............................................................................................
# 3. Calculate the factorial of a number entered by the user.
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
print(factorial(7))

# Output:
5040
# ...............................................................................................
# 4. Print the reverse of a given number (e.g., input 1234 → output 4321).
def reverse(n):
    rev=0
    for i in range(n):
        digit=n%10
        n//=10
        rev=rev*10+digit
        if n==0:
            break
    return rev
print(reverse(1234))

# Output:
4321
# ...............................................................................................
# 5. Count the number of digits in a given integer using a loop.
def count(n):
    no=0
    for i in range(n):
        digit=n%10
        n//=10
        no+=1
        if n==0:
            break
    return no
print(count(1234))

# Output:
4
# ...............................................................................................
# 6. Write a program that prints all numbers from 1 to 100 that are divisible by both 3 and 5.
def div(num):
    for i in range(1,num+1):
        if i%3==0 and i%5==0:
            print(i,end=' ')
    return ""
print(div(100))

# Output:
15 30 45 60 75 90 
# ...............................................................................................
# 7. Without using multiplication, calculate a * b using addition and a loop.
def multiply(a,b):
    result = 0
    for i in range(b):
        result+=a
    print(f"{a} * {b}")
    return result
print(multiply(10,5))    

# Output:
10 * 5
50
# ...............................................................................................
# 8. Print the sum of digits of a number entered by the user (e.g., 123 → 1+2+3 = 6).
def sum_of_dig(n):
    sum=0
    for i in range(n):
        digit=n%10
        n//=10
        sum+=digit
        if n==0:
            break
    return sum
print(sum_of_dig(1234))

# Output:
10
# ...............................................................................................
# 9. Write a loop to check if a number is a palindrome (number reads the same forwards and backwards).
def palindrome(n):
    num=n
    pd=0
    for i in range(n):
        digit=n%10
        n//=10
        pd=pd*10+digit
        if n==0:
            break
    if pd==num:
        print("Palindrome")
    else:
        print("Not Palindrome")
    return ""
print(palindrome(123321))

# Output:
Palindrome
# ...............................................................................................
# 10. Write a program to find the highest digit in a given number.
def highest_num(n):
    high=0
    for i in range(n):
        digit=n%10
        n//=10
        if n==0:
            break
        if digit > high:
            high=digit
        else:
            high=high
    return high
print(highest_num(12836))

# Output:
8

# 11. Write a program to check if a number is positive, negative, or zero.
def pos_neg_zero(n):
    if n==0:
        print("Zero")
    elif n>0:
        print("positive")
    else:
        print("Negative")
    return ""
print(pos_neg_zero(20))

# Output:
positive
# ...............................................................................................
# 12. Write a program that takes a number and prints whether it is divisible by 2, 3, both, or neither.
def div(n):
    if n%2==0 and n%3==0:
        print(f"{n} is divisible by both 2 & 3")
    elif n%2==0:
        print(f"{n} is divisible by 2")
    elif n%3==0:
        print(f"{n} is divisible by 3")
    else:
        print(f"{n} is not divisible by neither 2 nor 3")
    return ""
print(div(24))

# Output:
24 is divisible by both 2 & 3
# ...............................................................................................
# 13. Check if a number is a three-digit number using conditionals.
def three_digit(n):
    s=str(n)
    if len(s)==3:
        print("Given number is 3 digit number")
    else:
        print("Given number is nt a 3 digit number")
    return ""
print(three_digit(242))

# Output:
Given number is 3 digit number

# ...............................................................................................
# 14. Write a program to check whether a given number is a prime number.
def prime(n):
    if n<=1:
        print(f"{n} is not a prime number")
    else:
        for i in range(2,n):
            if n%i==0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")
    return ""
print(prime(29))

# Output:
29 is a prime number
# ...............................................................................................
# 15. Write a program to find the largest of three numbers entered by the user using nested if-else.
# def largest_3_num(a,b,c):
#     if a>b and a>c:
#         print(f"{a} is Largest")
#     elif b>a  and b>c:
#         print(f"{b} is Largest")
#     else:
#         print(f"{c} is Largest")
#     return ""
# print(largest_3_num(7,8,9))

def largest_3_num(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is Largest")
        else:
            print(f"{b} is Largest")
    else:
        if b>c:
            print(f"{b} is Largest")
        else:
            print(f"{c} is Largest")
    return ""
print(largest_3_num(7,8,9))

# Output:
9 is Largest
# ...............................................................................................
# 16. Check if a year is a leap year or not.
def leap_year(y):
    if (y%4==0 and y%100!=0) or y%400==0 :
        print("Leap year")
    else:
        print("Not a Leap year")
    return ""
print(leap_year(2024))

# Output:
Leap year
# ...............................................................................................
# 17. Take an integer input and determine if it is even and greater than 50.
def even_greater(n):
    if n%2==0 and n>51:
        print("Even number and greater than 50")
    elif n%2==0:
        print("Even number")
    else:
        print("valid Number")
    return ""
print(even_greater(6))

# Output:
Even number
# ...............................................................................................
# 18. Write a program to classify a number as:
# * Less than 0: "Negative"
# * 0 to 9: "Single Digit"
# * 10 to 99: "Two Digits"
# * 100 and above: "Three or More Digits"
def classify(n):
    if n<0:
        print("Negative")
    elif n>=0 and n<=9:
        print("Single digit")
    elif n>=10 and n<=99:
        print("Two digit")
    else:
        print("Three or More Digits")
    return ''
print(classify(503))

# Output:
Three or More Digits
# ...............................................................................................
# 19. Write a program to check if the square of a number is greater than 1000, and if yes, print the square.
def square_num(n):
    s=n**2
    if  s>1000:
        print("Yes",s)
    else :
        print(s,"not greater than 1000")
    return ""
print(square_num(25))

# Output:
625 not greater than 1000
# ...............................................................................................
# 20. Take two integers as input and determine if one is a factor of the other.
def factor(a,b):
    if a%b==0 or b%a==0:
        print("one is a factor of the other")
    else:
        print("No factors")
    return ""
print(factor(20,2))

# Output:
one is a factor of the other

