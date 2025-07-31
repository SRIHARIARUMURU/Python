# Develop a Hospital Patient Management System in Python with the following functionalities:

# i) Add patient data with automatic ID generation.

# ii) Store multiple patients using a list.

# iii) Use methods for admitting, discharging, checking details, and printing reports.

# iv) Use a loop-based menu to allow user interaction.

import random
class hospital_management:
    all_patients=[]
 # -------------------------------------Admitting new person------------------------------------------   
    def admitting(self):
        patient_data={}
        patient_data["patient_id"]=random.randint(900000,999999)
        patient_data["name"]=input("Enter Patient Name : ").upper()
        while True:
            try:
                age=int(input("Enter Age : "))
                # if age.isdigit():
                if age>=1 and age <=100:
                        patient_data["age"]=age
                        break
            except Exception as e:
                print(e)
            print("Enter valid Age")
        while True:
            gender=input("Enter gender : ").lower()
            if gender in ("male","m","female","f","trans"):
                patient_data["gender"]=gender
                break
            print("Enter correct gender")
        while True:
            num=input("Enter Mobile Number(Only 10 digits) : ")
            if len(num)==10 and num.isdigit():
                patient_data["Mobile Number"]=int(num)
                break
            print("Enter valid Mobile Number")
        while True:
            date=input("Enter Admission date(DD/MM/YY) ")
            if len(date)==10 and all(i in "0123456789-/" for i in date):
                patient_data["admission_date"]=date
                break
            print("Enter Valid date")

        patient_data["Status"]="IN"
        print("Patient Registered Successfully")
        print(patient_data)
        hospital_management.all_patients.append(patient_data)
# -------------------------------------discharging------------------------------------------
    def discharging(self):
        while True:
            p_id=int(input("Enter patient ID "))
            for i in hospital_management.all_patients:
                if i["patient_id"]==p_id:
                    while True:
                        date=input("Enter Discharging date(DD/MM/YY) ")
                        if len(date)==10 and all(i in "0123456789-/" for i in date):
                            i["discharging_date"]=date
                            break
                        print("Enter Valid date")
                    i["Status"]="OUT"
                    print(i)
                    print("Patient Succesfully Discharged")
                    return
            print("patient not found") 
# ----------------------------------------checking_details--------------------------------------      
    def checking_details(self):
        while True:
            p_id=int(input("Enter patient ID to get details "))
            for i in hospital_management.all_patients:
                if i["patient_id"]==p_id:
                    i["Date of discharged"]=input()
                    print(i)
                    return
            print("patient not found\nEnter 5 to go to main menu\n")
            x=int(input())
            if x==5:
                return

# ---------------------------------------------------------------------------------------------
obj=hospital_management()
while True:
    opt=int(input("Enter 1 for admitting\nEnter 2 for discharging\nEnter 3 for checking details\nEnter 4 for all Patients data\nEnter 5 to go to main menu\nChoose Option : "))
    match opt:
        case 1:
            obj.admitting()
        case 2:
            obj.discharging()
        case 3:
            obj.checking_details()
        case 4:
            print(hospital_management.all_patients)
        case 5:
            print("Thank you for visiting! Have a nice day")
            break
        case _:
            print("Enter options between 1 to 5")