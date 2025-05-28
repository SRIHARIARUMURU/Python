#1. Count how many numbers between 1 and 50 are divisible by 7.
count=0
for i in range(1,51):
    if i%7==0:
      count+=1 
print("No.of numbers that are divisible by 7 between 1 and 50 = ",count)

# OutPut:
# No.of numbers that are divisible by 7 between 1 and 50 =  7
#---------------------------------------------------------------------------------
#2. Print the factorial of a number (e.g., 5!) using a for loop.
number=5
factorial=1
for i in range(1,number+1):
    factorial*=i
print(f"Factorial of {number} is",factorial)

#OutPut:
#Factorial of 5 is 120
#---------------------------------------------------------------------------------
#3. print all numbers b/w 1 to 40 which are divisible by both 5 and 7.
for i in range(1,41):
    if i%5==0 and i%7==0:
        print(f"No.of numbers that divisible by both 5 and 7 b/w 1 to 40 = ",i)
        
# OutPut:
# Numbers that divisible by both 5 and 7 b/w 1 to 40 =  35
