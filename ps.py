# Sum of elements is 5
for i in range(6):
    for j in range(6):
        if i+j==5:
            print(i,j)

# Output:
# 0 5
# 1 4
# 2 3
# 3 2
# 4 1
# 5 0

# sum of elements only divisible by 5 & 3  
for i in range(9):
    for j in range(9):
        x=i+j
        if x%3==0 and x%5==0:
            print(i,j)
# Output:
# 0 0
# 7 8
# 8 7

# sum is odd 
for i in range(6):
    for j in range(6):
        x=i+j
        if x%2!=0:
            print(i,j)

Output:
0 1
0 3
0 5
1 0
1 2
1 4
2 1
2 3
2 5
3 0
3 2
3 4
4 1
4 3
4 5
5 0
5 2
5 4

# Without using count ,print which character is repeating 
a="srihari_arumuru"
x=""
y=""
k=""
for i in a:
    if i not in x:
        x+=i
    else: 
        y+=i
for j in y:
    if j not in k:
        k+=j
print(k) 

# Output:
# riau
