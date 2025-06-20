# 1. Write a Python program to print the word with the maximum length from the list m = ['python', 'java', 'c++', 'developer']
m = ['python', 'java', 'c++', 'developer']
def mx_len(m):
    a=''
    for i in m:
        if len(i)>len(a):
            a=i
    return a
print(mx_len(m))

# Output:
# developer

# 2. Given a list and a target number, return all pairs that sum to the target.
l=[1,2,3,6,2,2,4,3,4,7,8,3,0]
def target_sum(l):
    n=7
    for i in range (len(l)-1):
        if l[i]+l[i+1]==n:  
           print(l[i],l[i+1])
target_sum(l)

# Output:
# 4 3
# 3 4

# 3. Write a program to remove duplicate elements from a list.
l1=[1,2,3,5,4,6,3,1,3,8,7,6,4,1,1,1,1,2]
def dup(l1):
    res=[]
    for i in l1:
        if i not in res:
            res.append(i)
    return res
print(dup(l1))

# Output:
# [1, 2, 3, 5, 4, 6, 8, 7]

# 4. Write a Python program to print the common elements between two given lists.
l1=[1,2,3,4,5,6,7,0]
l2=[5,0,3,8,9,10,11,0]
def common(l1,l2):
    l3=[]
    res=[]
    for i in l1:
        for j in l2:
            if i==j:
                  l3.append(i)
    for k in l3:
        if k not in res:
            res.append(k)
    return res
print(common(l1,l2))

# Output:
# [3, 5, 0]

# 5. Write a Python program to move all 0's in the list k = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0] to the end of the list?
k = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0]
def rev(k):
    l1=[]
    l2=[]
    for i in k:
        if i==0:
            l1.append(i)
        else:
            l2.append(i)
    return l2+l1
print(rev(k))

# Output:
# [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
