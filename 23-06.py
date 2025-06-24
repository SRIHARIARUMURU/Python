# 1.Write a Python program that takes an amount n = 5200 and breaks it down into the minimum number of currency notes available in                         denominations of 500, 200, 100, 50, 20, 10, and 1 rupees.
# Output: 10 500 rupees notes and 1 200rupees notes
n = 5200
m=n//500
x=(n%500)//200
print(f"{m} 500 rupees notes and {x} 200 rupees notes")

# Output:
# 10 500 rupees notes and 1 200 rupees notes

# 2.Write a Python program to keep asking the user to enter a password until they enter the correct
password="Abc123"
while True:
    inp_password=input("Enter your password")
    if inp_password==password:
        print("Welcome Chief")
        break
else:
    print("Enter Correct Passwoed")

# Output:
# Enter your password : abc123
# Enter your password : Abc 123
# Enter your password : Abc123
# Welcome Chief

# 3.Convert a 2D list into a flat 1D list using list comprehension.
l1=[[1,2,3,4,5,6],[8,9,10,11,12]]
print([j for i in l1 for j in i])

# Output:
[1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]

# 4.Given a string, use list comprehension to create a list of all characters, excluding vowels.
s="srihari"
print([ i  for i in s  if i not in "AEIOUaeiou"])

# Output:
# ['s', 'r', 'h', 'r']

# 5.From a given list of words, extract only those that start with a vowel (a, e, i, o, u).
# Example: words = ["functions", "loops", "oops", "exception", "as"]
w = ["functions", "loops", "oops", "exception", "as"]
print([i for i in w  for j in "AEIOUaeiou"  if i.startswith(j)])

# Output:
# ['oops', 'exception', 'as']
