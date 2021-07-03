from LoadData import banks_list
from Account import *
from Classes import *
from Send_sms import send_message


########################
#      Functions       #
########################


def full_details():
    for bank in banks_list:
        bank.bank_details()


def strong_pass_cond():
    print("""Conditions for a valid password are : 
    - Should have at least one number.
    - Should have at least one uppercase and one lowercase character.
    - Should have at least one special symbol.
    - Should be between 6 to 20 characters long.""")


def password_checker(password):
    import re
    passwd = password
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)
    mat = re.search(pat, passwd)

    if mat:
        print("Password is Valid.")
        return True
    else:
        print("Password Invalid !!")
        return False


def display_options2():
    key = input("Do you have a Bank Account(yes/no) / 0 to exit : ").lower()
    if key == '0':
        return -1

    if key == "no":
        print("To create a bank account, enter the details")
        ### ------- TODO
        person_name = input("Enter Your Name : ")
        bank_name = input("Enter Name of the Bank : ")
        branch_name = input("Enter Name of the Branch : ")
        new_bank = Bank(bank_name)
        new_bank.add_branch(branch_name)
        new_bank.add_customer(branch_name, person_name, 1000)
        branch_n = new_bank.find_branch(branch_name)
        return branch_n.find_customer(person_name)
    else:
        person_name = input("Enter Your Name : ")
        bank_name = input("Enter Name of the Bank : ")
        branch_name = input("Enter Name of the Branch : ")
        open_acc = None
        for item in banks_list:
            if item.name == bank_name:
                open_acc = item

        customer = open_acc.find_branch(branch_name).find_customer(person_name)
        return customer


def display_options1():
    print("----Enter Option Respectively----")
    print("1. Login To Account")
    print("2. SignUp New Account")
    print("3. Exit")
    option = int(input("Select the Function Option : "))
    if option == 1:
        acc = login_acc()
        return acc
    elif option == 2:
        acc = sign_up_acc()
        return acc
    elif option == 3:
        return -1
    else:
        print("Invalid Option Selected")
        return 0


def login_acc():
    user_name = input("Enter the username : ")
    while True:
        pass_word = input("Enter the password : ")
        acc = find_acc(user_name)
        if acc is None:
            print("Account Does Not Exists")
            return 0
        elif pass_word != acc.password:
            print("Incorrect Password")

            check = input("Forgotten Password, need help?(yes/no) : ").lower()
            if check == "yes":
                name = input("Enter your Username : ")
                the_acc = find_acc(name)
                if the_acc is not None:
                    the_pass = the_acc.password
                    the_num = the_acc.number
                    the_body = "The Password of " + name + "is " + the_pass
                    send_message(the_body)
                    print(f"The Password of the User - {name} has sent to the your manager of the bank")
                    break
                else:
                    print(f"Actually, No account exists with username {name}")
                    continue
            else:
                print("Try Again")
                continue

        else:
            return acc


def sign_up_acc():
    user_name = input("Create Your New Account -> Username : ")
    num = int(input("Enter your phone number : "))
    print("Create Your Password")
    strong_pass_cond()
    print()
    valid = False
    while not valid:
        pass_word = input("Create Your Account Password : ")
        isvalid = password_checker(pass_word)
        if isvalid:
            new_account = Accounts(user_name, pass_word, num)
            valid = True
            return new_account


def find_acc(un):
    for acc in total_account:
        if acc.username == un:
            return acc
        else:
            return None


# Handling the
def display_options3(open_login, customer):
    print("----What do you want to Know----")
    print("""1. -> Account
2. -> Bank Details
3. -> Visiting Bank 
4. -> Exit
    """)

    option = int(input("Select your option : "))

    if option == 1:
        ###  _____________ TODO
        print("""1> Bank Account Balance
2> Withdraw Amount
3> Deposit Amount
4> Change User Account Details
        """)

        option2 = int(input("Select your option : "))

        if option2 == 1:
            print(f"Respected {customer.get_name}, Your account Balance is - {customer.get_amount()}")
        elif option2 == 2:
            print(f"Account Balance - {customer.get_amount()}")
            valid = False
            while not valid:
                amo = int(input("Enter Amount to Withdraw from Main Balance : "))
                if 0 <= amo <= customer.get_amount():
                    print("Withdrawal Successful")
                    valid = True
                    customer.add_transaction(-1 * amo)
                else:
                    print("Withdrawal Unsuccessful")
                    continue
        elif option2 == 3:
            amo = int(input("Enter Amount to Deposit : "))
            customer.add_transaction(amo)
            print("Deposit Completed Successfully")
        elif option2 == 4:
            ## ________ TODO
            print("----What do you want to change----")
            print("""1. Change Username of Account
2. Change Password
3. Change Phone Number""")

            option3 = int(input("Enter Valid Option : "))

            if option3 == 1:
                n_un = input("Enter New UserName : ")
                open_login.username = n_un
                print("Successfully Changed the Username")
            elif option3 == 2:
                strong_pass_cond()
                valid = False
                while not valid:
                    n_pa = input("Enter New Password : ")
                    if password_checker(n_pa):
                        open_login.password = n_pa
                        print("Successfully Changed The Password")
                        break
                    else:
                        print("Entered Invalid Password")
                        continue
            elif option3 == 3:
                n_num = int(input("Enter New Phone Number : "))
                open_login.number = n_num
                print("Successfully Changed Phone Number")

    elif option == 2:
        ##### _______ TODO
        print("----What details do you want----")
        print("""1. List the Customers in Bank
2. List The Customers in Branch with Transactions
3. List Entire Full Details of the Banks""")

        option4 = int(input("Enter Valid Option : "))

        if option4 == 1:
            bank_open = None
            bank_n = input("Enter Bank Name : ")
            branch_n = input("Enter Branch Name : ")
            for item in banks_list:
                if item.name == bank_n:
                    bank_open = item
            bank_open.list_branch_customers(branch_n, False)
        elif option4 == 2:
            bank_open2 = None
            bank_n = input("Enter Bank Name : ")
            branch_n = input("Enter Branch Name : ")
            for item in banks_list:
                if item.name == bank_n:
                    bank_open2 = item
            branch_open2 = bank_open2.find_branch(branch_n)
            branch_open2.list_customers()
        elif option4 == 3:
            for item in banks_list:
                item.bank_details()

    elif option == 3:
        pass
        # slot_booking() TODO
    elif option == 4:
        return -1











# password_checker("Hello")
# password_checker("1Arq@frds")


# sbi_bank = Bank("State Bank Of India")
# hdfc_bank = Bank("HDFC Bank Of India")
# icici_bank = Bank("ICICI Bank")
# union_bank = Bank("Union Bank Of India")
# axis_bank = Bank("AXIS Bank")
