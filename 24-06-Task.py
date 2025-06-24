# 1.Flatten the nested list [[1, 2], [3, 4], [5, 6]] into a single list.
l1=[[1, 2], [3, 4], [5, 6]] 
print([j for i in l1 for j in i ])

# Output:
# [1, 2, 3, 4, 5, 6]

# 2.From a nested list [[2, 5], [7, 9], [12, 15]], extract all even numbers.
l1=[[2, 5], [7, 9], [12, 15]]
print([j for i in l1 for j in i if j%2==0])

# Output:
# [2, 12]

# 3.Create a list of squares for numbers from 1 to 20.
print([i**2 for i in range(1,20)])

# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

# 4.Print prime numbers between 10 to 20 using list comprehension?
print([i for i in range(10,21) if all(i%j!=0 for j in range(2,i))])

# Output:
# [11, 13, 17, 19]

# 5.Convert a=2 int data type to 10 string data type  with out using str()?
m=2
a=''
l="0123456789"
for i in range(len(l)):
    if i==m:
        a=l[i]+a
print(a,type(a))

# a=2
# s="0123456789"
# st=s[a]
# print(a,type(a))

# Output:
# 2 <class 'str'>

# 5.Convert a=10 int data type to 10 string data type  with out using str()?
n=10
a=''
l="0123456789"
while n>0:
    m=n%10
    n//=10
    for i in range(len(l)):
        if i==m:
            a=l[i]+a
print(a,type(a))

# m=10
# a=''
# l="0123456789"
# while m>0:
#     n=m%10
#     a=l[n]+a
#     m//=10
# print(a,type(a))

# Output:
# 10 <class 'str'>

# 6.Write a Python program to swap the case of each character in a given string without using the built-in swapcase() method.
s="SRIhari"
def swap_case(s):
    for i in s:
        if ord(i)>=65 and ord(i)<91:
            print(chr(ord(i)+32),end='')
        else:
            print(chr(ord(i)-32),end='')
swap_case(s)

# Output:
# sriHARI

# 7.Write a list comprehension to print only the word 'python' from the list.
#S=[ ‘python’ ,’java’ , ‘c++’ , ‘developer’ ]
s=['python', 'java', 'c++', 'developer']
print([i for i in s if i =='python'])

# Output:
# ['python']
