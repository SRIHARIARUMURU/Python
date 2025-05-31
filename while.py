# 1)Display count down timer from 10 to 0 using while loop?
import time
i=10
while i>=0:
    print(i)
    time.sleep(1)
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
i=1
inp=['kumar','202','84558906']
while i<=3:
    pas=input("Enter Your Password : ")
    if pas in inp:
        print(inp)
        break
    else:
       if i==3:
            inp.clear()
            print("You Your data is deleted",inp)
       else:
           print("wrong password ,Try Again")
    i+=1

# Output:
# 1)
# Enter Your Password : 2
# wrong password ,Try Again
# Enter Your Password : ajaz
# wrong password ,Try Again
# Enter Your Password : 316861
# You Your data is deleted []
# 2)
# Enter Your Password : 203
# wrong password ,Try Again
# Enter Your Password : ajaz
# wrong password ,Try Again
# Enter Your Password : 202
# ['kumar', '202', '84558906']
