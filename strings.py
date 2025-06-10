#1. reverse a string
def reverse(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i],end=" ")
reverse("chaitanya")

# Output:
# a y n a t i a h c

#2. Replace "a" wth "i"
def replace(a):
    b=""
    for i in a:
        if i=="a":
            b+="i"
        else:
            b+=i
    return b
print(replace("chaitanya"))

# Output:
# chiitinyi

# 3.capital first
def capital(a):
    b=""
    c=""
    for i in a:
        if i.isupper():
            b+=i
        else:
            c+=i
    return b+c
print(capital("chaitanyaRAJ"))

# Output:
# RAJchaitanya

# 4. Count no.of occurrence 
def occur(a):
    count=0
    for i in a:
        if i=="a":
            print(i,end=" ")
            count+=1
    return count
print(occur("chaitanya"))

# Output:
# a a a 3

#5. Concatinate Ovals
def Ovals(a):
    b=""
    for i in a:
        if i in "aeiouAEIOU":
            b+=i
    return b
print(Ovals("chaitanya"))

# Output:
# aiaa
