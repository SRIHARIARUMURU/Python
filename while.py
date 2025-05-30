# 1)Display count down timer from 10 to 0 using while loop?
i=10
while i>=0:
    print(i)
    i-=1
print("timmer complete")

# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# timmer complete

# 2)Find max digit in number s=2569 using while loop?

s=2569
maxi=0
while s>0:
    num=s%10
    s//=10
    if maxi>num:
        maxi=maxi
    else:
        maxi=num
print(maxi)

# Output:
# 9

# 3)simulate a basic login system (max attempts 3)Input=['kumar','202','84558906' ]
inp = ['kumar', '202', '84558906']
for i in range(1, 4):
    value = input("Enter Your Password: ")
    if value in inp:
        print("Login successful:", inp)
        break
    elif i == 3:
        inp.clear()
        print("Login failed 3 times. Your data is deleted:", inp)
    else:
        print("Incorrect password. Try again.")


# Output:
# # 1)
# Enter Your Password: ajaz
# Incorrect password. Try again.
# Enter Your Password: 1651553
# Incorrect password. Try again.
# Enter Your Password: 203
# Login failed 3 times. Your data is deleted: []

# 2)Enter Your Password: 20
# Incorrect password. Try again.
# Enter Your Password: ajay
# Incorrect password. Try again.
# Enter Your Password: 202
# Login successful: ['kumar', '202', '84558906']
