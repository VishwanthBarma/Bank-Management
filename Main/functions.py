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


def display_options1():
    print("----Enter Option Respectively----")
    print("1> Login To Account")
    print("2> SignUp New Account")
    print("3> Exit")
    try:
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
    except ValueError:
        print("--INVALID OPTION ENTRY--")
        return 0


def login_acc():
    while True:
        user_name = input("Enter the username (0 - exit): ")
        if user_name == "":
            print("You Need to Enter the UserName")
            continue
        elif user_name == '0':
            return 0
        while True:
            pass_word = input("Enter the password (0 - exit) : ")
            if pass_word == '0':
                return 0
            acc = find_acc(user_name)
            if acc is None:
                print("Account Does Not Exists")
                return 0
            elif pass_word != acc.password:
                print("Incorrect Password")

                check = input("Forgotten Password, need help?(yes/no) : ").lower()
                if check == "yes":
                    while True:
                        name = input("Enter your Username : ")
                        if name == "":
                            continue

                        the_acc = find_acc(name)
                        if the_acc is not None:
                            the_pass = the_acc.password
                            the_num = the_acc.number
                            the_body = "The Password of " + name + "is " + the_pass
                            send_message(the_body)
                            print(f"The User - {name}, Phone Number - {the_num},"
                                  f" - your recovery password hase been sent to your bank ")
                            break
                        else:
                            print(f"Actually, No account exists with username {name}")
                            choice = input("Do you want to enter Username again(yes/no) : ").lower()
                            if choice == 'yes':
                                continue
                            else:
                                return 0
                    continue
                else:
                    print("Try Again")
                    continue

            else:
                return acc   # Correctly Returning the acc of the user


def sign_up_acc():
    while True:
        user_name = input("Create Your New Account -> Username (0 - exit) : ")
        if user_name == "0":
            return 0
        elif user_name == "":
            print("Sorry You need to enter the Username")
            continue
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
            else:
                print("Check the Password Requirements")


def find_acc(un):
    for acc in total_account:
        if acc.username == un:
            return acc
        else:
            return None


def display_options2():
    print("--Bank account verification--")
    key = input("Do you have a Bank Account(yes/no) / 0 to exit : ").lower()
    if key == '0':
        return -1

    if key == "no":
        print("To create a bank account, enter the details")

        while True:
            person_name = input("Enter Your Name (0 - exit): ")
            if person_name == '0':
                return -1
            elif person_name == "":
                continue
            else:
                break

        while True:
            bank_name = input("Enter Name of the Bank : ").lower()
            if bank_name == "":
                continue
            else:
                break

        while True:
            branch_name = input("Enter Name of the Branch : ").lower()
            if branch_name == "":
                continue
            else:
                break

        new_bank = Bank(bank_name)
        new_bank.add_branch(branch_name)
        new_bank.add_customer(branch_name, person_name, 1000)
        branch_n = new_bank.find_branch(branch_name)
        return branch_n.find_customer(person_name)

    else:

        while True:
            person_name = input("Enter Your Name (0 - exit): ")
            if person_name == '0':
                return -1
            elif person_name == "":
                continue
            else:
                break

        while True:
            bank_name = input("Enter Name of the Bank : ").lower()
            if bank_name == "":
                continue
            else:
                break

        while True:
            branch_name = input("Enter Name of the Branch : ").lower()
            if branch_name == "":
                continue
            else:
                break

        open_acc = None
        for item in banks_list:
            if item.name == bank_name:
                open_acc = item

        customer = open_acc.find_branch(branch_name).find_customer(person_name)
        return customer


# Handling the
def display_options3(open_login, customer):
    while True:

        print("----What do you want to Know----")
        print("""1> Account
2> Bank Details
3> Visiting Bank 
4> Exit""")

        option = int(input("Select your option : "))

        if option == 1:
            while True:
                print("-->[1] Account :- ")
                print("""    1> Bank Account Balance
    2> Withdraw Amount
    3> Deposit Amount
    4> Change User Account Details
    5> Exit
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
                    while True:
                        print("     -->[4] Change User Account Details :-")
                        print("     ----What do you want to change----")
                        print("""        1> Change Username of Account
        2> Change Password
        3> Change Phone Number
        4> Exit""")

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
                        elif option3 == 4:
                            break
                    continue

                elif option2 == 5:
                    break

        elif option == 2:
            while True:
                print("-->[2] Bank Details :- ")
                print("     ----What details do you want----")
                print("""    1> List the Customers in Bank
    2> List The Customers in Branch with Transactions
    3> List Entire Full Details of the Banks
    4> Exit""")
                try:

                    option4 = int(input("Enter Valid Option : "))

                    if option4 == 1:
                        bank_open = None

                        while True:
                            bank_n = input("Enter Bank Name : ").lower()

                            if bank_n == "":
                                print("You Should Enter Bank Name")
                                continue
                            else:
                                break

                        while True:
                            branch_n = input("Enter Branch Name : ").lower()

                            if branch_n == "":
                                print("You Should Enter Branch Name")
                                continue
                            else:
                                break

                        for item in banks_list:
                            if item.name == bank_n:
                                bank_open = item
                        bank_open.list_branch_customers(branch_n, False)
                    elif option4 == 2:
                        bank_open2 = None
                        while True:
                            bank_n = input("Enter Bank Name : ").lower()

                            if bank_n == "":
                                print("You Should Enter Bank Name")
                                continue
                            else:
                                break

                        while True:
                            branch_n = input("Enter Branch Name : ").lower()

                            if branch_n == "":
                                print("You Should Enter Branch Name")
                                continue
                            else:
                                break

                        for item in banks_list:
                            if item.name == bank_n:
                                bank_open2 = item
                        branch_open2 = bank_open2.find_branch(branch_n)
                        branch_open2.list_customers()
                    elif option4 == 3:
                        for item in banks_list:
                            item.bank_details()
                    elif option4 == 4:
                        break
                except ValueError:
                    print("--INVALID OPTION ENTRY--")
                    continue
                continue

            continue

        elif option == 3:
            pass
            # slot_booking() TODO
        elif option == 4:
            return -1

        continue


def banks_avail():
    print("""1. SBI BANK
2. HDFC BANK
3. ICICI BANK
4. UNION BANK
5. AXIS BANK""")









# password_checker("Hello")
# password_checker("1Arq@frds")


# sbi_bank = Bank("State Bank Of India")
# hdfc_bank = Bank("HDFC Bank Of India")
# icici_bank = Bank("ICICI Bank")
# union_bank = Bank("Union Bank Of India")
# axis_bank = Bank("AXIS Bank")
