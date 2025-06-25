#1.  Wait a python programme to find the nearest prime number to a given number.?
def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
n=10
upper=n
lower=n

while True:
    if is_prime(upper):
        print(upper)
        break
    elif is_prime(lower):
        print(lower)
        break
    upper+=1    
    lower-=1

# Output:
# 11

#2. programme to print the first 5 prime numbers.?
def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
count=0
n=2
while count<5:
    if is_prime(n):
        print(n)
        count+=1
    n+=1
    
# Output:
# 2 3 5 7 11 
