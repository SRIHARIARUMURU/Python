# 1. Rotate a list by k positions.
def rotate(a):
    b=[]
    c=[]
    k=2
    for i in range(len(a)-k,len(a)):
        # print(i,a[i])
        b.append(a[i])
    # print(b)
    for i in range(len(a)-k):
        c.append(a[i])
    print(b+c)
rotate(a)
a=[1,2,3,4,5,6,7]

# Output:
# [6, 7, 1, 2, 3, 4, 5]

#2. Find the second largest element in a list without sorting.
def sl(l):
    l.remove(max(l))
    print(max(l))
sl([1,2,3,5,6,4,7,9,2,1,99,100])

# Output:
# 99

#3. Move all zeroes to the end of the list while maintaining the order.
def zero(l):
    res=[]
    for i in l:
        if i==0:
            l.remove(i)
            res.append(i)
    return l+res
print(zero([1,0,2,3,50,0,6,4,7,9,2,0,1,99,100]))

# Output:
# [1, 2, 3, 50, 6, 4, 7, 9, 2, 1, 99, 100, 0, 0, 0]

#4. Remove duplicates from a list without using set().
l=[1,2,3,5,4,6,3,1,3,8,7,6,4,1,1,1,1,2]
def dup(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1
print(dup(l))

# Output:
# [1, 2, 3, 5, 4, 6, 8, 7]

#5. Count the frequency of each element in a list.
l=[1,2,3,5,4,6,3,1,3,8,7,6,4,1,1,1,1,2]
def frequency(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    for i in l1:
        print(i,":",l.count(i),end="     ")
frequency((l))

# Output
# 1 : 6     2 : 2     3 : 3     5 : 1     4 : 2     6 : 2     8 : 1     7 : 1     

#6. Find the maximum product of two elements in a list.
l=[9,100,2,3,5,4,6,3,1,3,8,7,6,4,1,1,1,1,2]
def max_product(l):
    max=0
    for i in range(len(l)-1):
        a=l[i]*l[i+1]
        if a >max:
            max=a
        else:
            max=max
    return max
print(max_product(l))

# Output:
900

#7. Reverse a list without using built-in reverse functions
l=[1,2,3,4,5,6,7,8,9]
def rev(l):
    res=[]
    for i in range(len(l)-1,-1,-1):
        res.append(l[i])
    return(res)
print(rev(l))

# Output:
# [9, 8, 7, 6, 5, 4, 3, 2, 1]

#8. Check if a list is a palindrome.
l=['m','a','d','a','m']
def palindrome(l):
    res=[]
    for i in range(len(l)-1,-1,-1):
        res.append(l[i])
    if res==l:
        print("palindrome")
    else:
        print("Not a Palindrome")
palindrome(l)

# Output:
# palindrome

#9. Find the common elements between two lists.
l1=[1,2,5,0,3,2]
l2=[4,5,0,3,7,8]
def  common(l1,l2):
    res=[]
    res1=[]
    for i in l1:
        for j in l2:
            if i==j:
                res.append(j)
    for i in res:
        if i not in res1:
            res1.append(i)
    return res1
print(common(l1,l2))

# Output:
# [5, 0, 3]
