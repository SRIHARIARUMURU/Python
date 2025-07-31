import random

class ASH_Bank:
    # ------------------------------------Account Creation------------------------------------
    # storing all customer details in a list
    customers=[]              
    def create_acc_no(self):
        # Storing details of a customers into a dictonary 
        customer_details={}
        # type of an account
        type=input("Enter type of an account(savings/zero) : ").strip().lower()
        while True:
            # type=input("Enter type of an account")
            if type=="savings":
                bal=int(input("Deposit Rs1000 to open savings account : "))
                if bal>=1000:
                    customer_details["Account_Type"]="Savings"
                    customer_details["Total balance"]=bal
                    break
                print(" Deposit Rs.1000")
            elif type=="zero":
                bal=int(input("Deposit Rs100 to open savings account : "))
                if bal>=100:
                    customer_details["Account_Type"]="Zero"
                    customer_details["Total balance"]=bal
                    break
                print("Deposit Rs.100")
            else:
                type=input("Invalid! Enter type of an account(savings/zero) : ").strip().lower()
        # customer main details start  
        self.IFSC="ASH0250726"
        customer_details["IFSC code"]=self.IFSC
        customer_details["Account Number"]=random.randint(1000000000,9999999999)
        customer_details["Custome Name"]=input("Enter Full Name : ").strip()
        # Store and Validate Aadhar Number
        while True:
            a_num=input("Enter Aadhar number without spaces : ").strip()
            if len(a_num)==12 and a_num.isdigit():
                customer_details["Aadhar number"]=int(a_num)
                break
            print("Enter valid Aadhar Number")
        # Store and Validate Mobile Number
        while True:
            num=input("Enter Mobile Number(Only 10 digits) : ")
            if len(num)==10 and num.isdigit():
                customer_details["Mobile Number"]=int(num)
                break
            print("Enter valid Mobile Number")
        print("\nAccount created successfully:")
        print(customer_details)
        # Stores all the customers data in a list
        ASH_Bank.customers.append(customer_details)
    # search for a person by using aadhar number
    def search_persons(self):
        while True:
            inp_acc_no=input("Enter correct 12 digit Aadhar Number\n")
            if not (inp_acc_no.isdigit() and len(inp_acc_no)==12):
                print("Enter Valid Aadhar number")
                continue
            for i in ASH_Bank.customers:
                if i["Aadhar number"]==int(inp_acc_no):
                    print(i)
                    return
            print("customer not Found")
    # ------------------------------------Withdraw------------------------------------
    def deposit(self):
        acc_num=int(input("Enter Account Number"))
        for cust in ASH_Bank.customers:
            if cust["Account Number"]==acc_num:
                amount=int(input("Enter Amount to to Deposite"))
                cust["Total balance"]+=amount
                print(f"Total amount in your account is {cust["Total balance"]}")
    # ------------------------------------Deposit------------------------------------
    def withdraw(self):
        acc_num=int(input("Enter Account Number"))
        for cust in ASH_Bank.customers:
            if cust["Account Number"]==acc_num:
                amount=int(input("Enter Amount to to Deposite"))
                cust["Total balance"]-=amount
                print(f"Total amount in your account is {cust["Total balance"]}")
    # ------------------------------------Check balancec------------------------------------
    def check_balance(self):
        acc_num=int(input("Enter Account Number"))
        for cust in ASH_Bank.customers:
            if cust["Account Number"]==acc_num:
                print(f"Total amount in your account is {cust["Total balance"]}")
    # ------------------------------------Account Close/Delete------------------------------------
    def delete_account(self):
        acc_num=int(input("Enter Account Number : "))
        for cust in ASH_Bank.customers:
            if cust["Account Number"]==acc_num:
                d=input("Are You sure to delete Account\nEnter(Y/N) : ").upper()
                if d=="Y":
                    ASH_Bank.customers.remove(cust)
                    print("This accounted is deleted")
                else:
                    print("Account Deletion Canceled")
                break
            print("Account Not Found")
        return ""
bank=ASH_Bank()
while True:
    print("\nWelcome to ASH_Bank")
    opt=int(input("Enter 1 to create New Account\nEnter 2 for Deposite\nEnter 3 to Withdraw\nEnter 4 to Check Balance\nEnter 5 to search customer details\nEnter 6 to see all customer details\nEnter 7 to Delete Account\nEnter 8 to exit\nChoose Your Option "))
    match opt:
        case 1:
            bank.create_acc_no()
        case 2:
            bank.deposit()
        case 3:
            bank.withdraw()
        case 4:
            bank.check_balance()
        case 5:
            bank.search_persons()
        case 6:
            print(ASH_Bank.customers)
        case 7:
            bank.delete_account()
        case 8:
            print("Thank you for visiting our bank! Have a good day.")
            break
        case _:
            print("--------------Enter Valid Option--------------")
