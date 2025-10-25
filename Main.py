 # Project Introduction Banner
 
print()
print('_ '*103)
print("* . "*58)
print()
print(" "*100,'SHRI VAISHNAV KANYA VIDYALAYA'," "*100)
print()
print(" "*96,'CHEMISTRY LAB MANAGEMENT SYSTEM'," "*96)
print()
print(" "*88,'DESIGNED & MAINTAINED BY RISHIKA VISHWAKARMA'," "*88)
print('_ '*103)
print()

# Import modules
from Login_module import register_user, login_user
from Chemical_module import chemical_records
from Equipment_module import equipment_records
from Chemical_Claim_module import c_claim_records
from Equipment_Claim_module import e_claim_records
from Bill_module import bill_records

# Main Menu Function
def menu():
    print(' '*78 ,'MAIN MENU' ,' '*78)
    print(' '*78 ,'1. CHEMICAL RECORDS',' '*78)
    print(' '*78 ,'2. EQUIPMENT RECORDS' ,' '*78)
    print(' '*78 ,'3. EQUIPMENT CLAIM RECORDS' ,' '*78)
    print(' '*78 ,'4. CHEMICAL CLAIM RECORDS' ,' '*78)
    print(' '*78 ,'5. GENERATE BILL' ,' '*78)
    print(' '*78 ,'6. EXIT' ,' '*78)
    ch = int(input('Enter choice:'))    # Choice 

    if ch == 1:
        chemical_records()
    elif ch == 2:
        equipment_records()
    elif ch == 3:
        e_claim_records()               # Equipment Claim Records
    elif ch == 4:
        c_claim_records()               # Chemical Claim Records
    elif ch == 5:
        bill_records()
    elif ch == 6:
        print('THANKYOU !')
        print("VISIT AGAIN :) ")
        exit()
    else:
        print('INVALID CHOICE')
        menu()

# Entry point for login / registration
if __name__ == "__main__":
    print()
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print()

    ch = int(input("Enter choice: "))
    if ch == 1:
        register_user()
    elif ch == 2:
        if login_user():
            while True:
                menu()
    elif ch == 3:
        print("THANK YOU! VISIT AGAIN :)")
        exit()
    else:
        print("Invalid choice!")
        