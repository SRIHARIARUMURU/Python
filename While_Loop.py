#1. Print numbers from 1 to 10 using a while loop.
num=1
while num<=10:
    print(num,end=" ")
    num+=1
    
#OutPut:
#1 2 3 4 5 6 7 8 9 10 
#-------------------------------------------------------------------------
#2. Print even numbers between 1 and 50 using a while loop.
num=2
while num<=50:
    print(num,end=" ")
    num+=2
    
#OutPut:
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 
#-------------------------------------------------------------------------
#3. Print the multiplication table of a given number (e.g., 5) using a while loop.
    
num=int(input("Enter a Number"))
start=1
while start<=10:
    print(f"{num} x {start} = {num*start}")
    start+=1

# OutPut:

# Enter a Number5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
#-------------------------------------------------------------------------
#4. Calculate the sum of digits of a number using a while loop.e.g., 123 → 6
num=int(input())
add=0
while num>0:
    digit=num%10
    add=add+digit
    num//=10
print(add)
#-------------------------------------------------------------------------
#5. Reverse a number using a while loop.
num=int(input())
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print(rev)
#-------------------------------------------------------------------------
#6. Check if a number is a palindrome using a while loop.e.g., 121 → Palindrome
num=int(input("Enter a number"))
rev=0
temp=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
if temp==rev:
    print(f"{rev} is Palindrome")
else:
    print(f"{rev} is Not a Palindrome")
  #-------------------------------------------------------------------------
  #9. Keep asking the user for input until they enter "exit".Hint: Use while True: and break.
while True:
    print("To stop the loop enter 'exit'")
    a=input()
    if a=="exit":
        break

# OutPut:
# To stop the loop enter 'exit'
# 242
# To stop the loop enter 'exit'
# assd
# To stop the loop enter 'exit'
# dxxs
# To stop the loop enter 'exit'
# d
# To stop the loop enter 'exit'
# df
# To stop the loop enter 'exit'
# exit
#-------------------------------------------------------------------------
