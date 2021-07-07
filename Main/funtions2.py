# Importing Files
import sqlite3
from Send_sms import send_message
from functions import strong_pass_cond, password_checker
from SlotBooking import main_booking

# Data-Base connection and cursor
connection = sqlite3.connect('data_base.db')
cursor = connection.cursor()

# New Functions
# -> display_function1
# -> display_function2
# -> display_function3


def display_function1():
    print()
    print("----Enter Option Respectively----")
    print("1> Login To Account")
    print("2> SignUp New Account")
    print("3> Exit")
    try:
        print()
        option = int(input("Select the Function Option : "))
        if option == 1:
            opt1 = login_account()    # login account
            if opt1 == 0:
                return 0
            elif opt1 == 1:
                return 1
            else:
                return opt1

        elif option == 2:
            opt2 = sign_up_account()   # sign up account
            if opt2 == 0:
                return 0
            elif opt2 == 1:
                return 1
            else:
                return opt2

        elif option == 3:
            return -1
        else:
            print("Invalid Option Selected")
            return 0
    except ValueError:
        print("--INVALID OPTION ENTRY--")
        return 0


def sign_up_account():
    while True:
        print()
        user_name = input("Create Your New Account -> Username (0 - exit) : ")
        if user_name == "0":
            return 0
        elif user_name == "":
            print("Sorry You need to enter the Username")
            continue

        # num = int(input("Enter your phone number : "))

        print("Create Your Password")
        strong_pass_cond()
        print()
        valid = False
        while not valid:
            print()
            pass_word = input("Create Your Account Password : ")
            isvalid = password_checker(pass_word)
            if isvalid:
                # new_account = Accounts(user_name, pass_word, num)
                with connection:
                    cursor.execute("SELECT * FROM accounts WHERE username=:username", {'username': user_name})
                    user = cursor.fetchone()
                    if user is None:
                        cursor.execute("INSERT INTO accounts VALUES(:username, :password)", {'username': user_name, 'password': pass_word})
                        connection.commit()
                        print("**Created Account Successfully**")

                        cursor.execute("SELECT * FROM accounts WHERE username=:username AND password=:password", {'username': user_name, 'password': pass_word})
                        data = cursor.fetchone()

                        return data
                    else:
                        print("**Account Already Exists. Logging In**")

                        cursor.execute("SELECT * FROM accounts WHERE username=:username AND password=:password", {'username': user_name, 'password': pass_word})
                        data = cursor.fetchone()

                        return data

            else:
                print("Check the Password Requirements")


def login_account():
    while True:
        print()
        user_name = input("Enter the username (0 - exit): ")
        if user_name == "":
            print("You Need to Enter the Valid UserName")
            continue

        elif user_name == '0':
            return 0

        while True:
            print()
            pass_word = input("Enter the password (0 - exit) : ")
            if pass_word == '0':
                return 0

            # acc = find_acc(user_name)

            with connection:
                cursor.execute("SELECT * FROM accounts WHERE username=:username", {'username': user_name})
                acc = cursor.fetchone()

            if acc is None:
                print("Account Does Not Exists")
                return 0

            elif acc[1] != pass_word:
                print("Incorrect Password")

                print()
                check = input("Forgotten Password, need help?(yes/no) : ").lower()
                if check == "yes":
                    while True:
                        # name = input("Enter your Username : ")
                        # if name == "":
                        #     continue

                        # cursor.execute("SELECT * FROM accounts WHERE username=:username", {'username': user_name})
                        # the_acc = cursor.fetchone()

                        # the_acc = find_acc(name)
                        the_name = acc[0]

                        if acc is not None:
                            the_pass = acc[1]
                            # the_num = the_acc.number
                            the_body = "The Password of Username : " + the_name + "is " + the_pass
                            send_message(the_body)
                            print(f"The User - {the_name},"
                                  f" - your recovery password hase been sent to your bank volunteer")
                            break

                        # else:
                        #     print(f"Actually, No account exists with username {the_name}")
                        #     choice = input("Do you want to enter Username again(yes/no) : ").lower()
                        #     if choice == 'yes':
                        #         continue
                        #     else:
                        #         return 0
                    continue
                else:
                    print("Try Again")
                    continue

            else:
                print("**Logged In Successfully**")

                cursor.execute("SELECT * FROM accounts WHERE username=:username AND password=:password", {'username': user_name, 'password': pass_word})
                data = cursor.fetchone()

                return data   # Correctly Returning the acc of the user


def display_functions2():
    print()
    print("--Bank account verification--")
    print()
    key = input("Do you have a Bank Account (yes / no) / (0 to exit) : ").lower()
    if key == '0':
        return -1

    if key == "no":
        print("To create a bank account, enter the details")

        while True:
            print()
            person_name = input("Enter Your Name (0 - exit): ").lower()
            if person_name == '0':
                return -1

            elif person_name == "":
                print("Enter Valid Name")
                continue

            else:
                break

        while True:
            bank_name = ""
            banks_avail()
            try:
                print()
                choice = int(input("Select The Bank to create the account in that bank : "))
                if choice == 1:
                    bank_name = "sbi"
                elif choice == 2:
                    bank_name = "hdfc"
                elif choice == 3:
                    bank_name = "icici"
                elif choice == 4:
                    bank_name = "union"
                elif choice == 5:
                    bank_name = "axis"
                else:
                    print("Invalid Syntax")
                    print("-TRY AGAIN-")
                    continue
                break
            except ValueError:
                print("Invalid Syntax")
                print("-TRY AGAIN-")
                continue

            # bank_name = input("Enter Name of the Bank : ").lower()
            # if bank_name == "":
            #     continue
            # else:
            #     break

        while True:
            print()
            branch_name = input("Enter Name of the Branch : ").lower()
            if branch_name == "":
                print("Invalid Syntax")
                continue
            else:
                break

        # new_bank = Bank(bank_name)
        # new_bank.add_branch(branch_name)
        # new_bank.add_customer(branch_name, person_name, 1000)
        # branch_n = new_bank.find_branch(branch_name)

        with connection:
            cursor.execute("SELECT * FROM bankaccounts WHERE personname=:personname"
                           " AND bankname=:bankname AND branchname=:branchname",
                           {'personname': person_name, 'bankname': bank_name, 'branchname': branch_name})
            data = cursor.fetchone()
            if data is None:
                cursor.execute("INSERT INTO bankaccounts VALUES(:bankname, :branchname, :personname, :amount)",
                               {'bankname': bank_name, 'branchname': branch_name,
                                'personname': person_name, 'amount': 1000})
                connection.commit()
                print("Created Bank Account Successfully - with initial bonus amount of Rs.1000 for opening the bank")
            else:
                print("Already Bank Account Exists with specified details")

            cursor.execute("SELECT * FROM bankaccounts WHERE personname=:personname"
                           " AND bankname=:bankname AND branchname=:branchname",
                           {'personname': person_name, 'bankname': bank_name, 'branchname': branch_name})

            data = cursor.fetchone()

            return data

    elif key == "yes":

        while True:
            print()
            person_name = input("Enter Your Exact Name, as mentioned in the bank account (0 - exit): ")

            if person_name == '0':
                return -1
            elif person_name == "":
                print("Enter Valid Name")
                continue
            else:
                break

        while True:
            bank_name = ""
            banks_avail()
            try:
                print()
                choice = int(input("Select The Bank in which your account exists : "))
                if choice == 1:
                    bank_name = "sbi"
                elif choice == 2:
                    bank_name = "hdfc"
                elif choice == 3:
                    bank_name = "icici"
                elif choice == 4:
                    bank_name = "union"
                elif choice == 5:
                    bank_name = "axis"
                else:
                    print("Invalid Syntax")
                    print("-TRY AGAIN-")
                    continue
                break
            except ValueError:
                print("Invalid Syntax")
                print("-TRY AGAIN-")
                continue


        # while True:
        #     bank_name = input("Enter Name of the Bank : ").lower()
        #     if bank_name == "":
        #         continue
        #     else:
        #         break

        # while True:
        #     branch_name = input("Enter Name of the Branch : ").lower()
        #     if branch_name == "":
        #         print("Enter Valid Branch Name")
        #         continue
        #     else:
        #         break

        # open_acc = None
        # for item in banks_list:
        #     if item.name == bank_name:
        #         open_acc = item

        # customer = open_acc.find_branch(branch_name).find_customer(person_name)

        cursor.execute("SELECT * FROM bankaccounts WHERE personname=:personname"
                       " AND bankname=:bankname",
                       {'personname': person_name, 'bankname': bank_name})

        data = cursor.fetchone()

        if data is None:
            print("Mentioned Details Does Not Match")
            print("TRY AGAIN - (your name is case sensitive)")
            return 0
        else:
            return data

    else:
        print("Entered Invalid Option - Try Again")
        return 0


def display_functions3(data, data_acc):
    while True:
        print()
        print("----What do you want to Know----")
        print("""1> Account
2> Bank Details
3> Visiting Bank 
4> Exit""")

        print()
        option = int(input("Select your option : "))

        if option == 1:
            while True:
                print()
                print("-->[1] Account :- ")
                print("""    1> Bank Account Balance
    2> Withdraw Amount
    3> Deposit Amount
    4> Change User Account Details
    5> Exit
                """)

                print()
                option2 = int(input("Select your option : "))

                if option2 == 1:
                    print(f"Respected {data[2]}, Your account Balance is - {data[3]}")
                elif option2 == 2:
                    print(f"Account Balance - {data[3]}")
                    valid = False
                    while not valid:
                        print()
                        amo = int(input("Enter Valid Amount to Withdraw from Main Balance : "))
                        if 0 <= amo <= data[3]:
                            data[3] -= amo
                            print(f"New Amount {data[3]}")
                            with connection:
                                cursor.execute("UPDATE bankaccounts SET amount=:amount WHERE"
                                               " bankname=:bankname AND branchname=:branchname AND"
                                               " personname=:personname", {'amount': data[3], 'bankname': data[0],
                                                                           'branchname': data[1], 'personname': data[2]})
                                connection.commit()

                            print("**Withdrawal Successful**")
                            valid = True
                            # customer.add_transaction(-1 * amo)
                        else:
                            print("**Withdrawal Unsuccessful**")
                            print(f"Your Account Balance is - {data[3]}")
                            continue
                elif option2 == 3:
                    print()
                    amo = int(input("Enter Amount to Deposit : "))
                    # customer.add_transaction(amo)
                    data[3] += amo

                    with connection:
                        cursor.execute("UPDATE bankaccounts SET amount=:amount WHERE"
                                       " bankname=:bankname AND branchname=:branchname AND"
                                       " personname=:personname", {'amount': data[3], 'bankname': data[0],
                                                                   'branchname': data[1], 'personname': data[2]})
                        connection.commit()

                    print("Deposit Completed Successfully")

                elif option2 == 4:
                    while True:
                        print()
                        print("     -->[4] Change User Account Details :-")
                        print("     ----What do you want to change----")
                        print("""        1> Change Username of Account
        2> Change Password
        3> Exit""")

                        print()
                        option3 = int(input("Enter Valid Option : "))

                        if option3 == 1:
                            print()
                            n_un = input("Enter New UserName : ")

                            with connection:
                                cursor.execute("UPDATE accounts SET username=:username WHERE password=:password",{'username': n_un, 'password': data_acc[1]})
                                connection.commit()

                            # open_login.username = n_un
                            print("Successfully Changed the Username")

                        elif option3 == 2:
                            strong_pass_cond()
                            valid = False
                            while not valid:
                                print()
                                n_pa = input("Enter New Password : ")
                                if password_checker(n_pa):
                                    # open_login.password = n_pa

                                    with connection:
                                        cursor.execute("UPDATE accounts SET password=:password WHERE username=:username",{'password': n_pa, 'username': data_acc[0]})
                                        connection.commit()

                                    print("Successfully Changed The Password")
                                    break
                                else:
                                    print("Entered Invalid Password")
                                    continue

                        # elif option3 == 3:
                        #     n_num = int(input("Enter New Phone Number : "))
                        #     open_login.number = n_num
                        #     print("Successfully Changed Phone Number")

                        elif option3 == 3:
                            break
                    continue

                elif option2 == 5:
                    break

        elif option == 2:
            while True:
                print()
                print("-->[2] Bank Details :- ")
                print("     ----What details do you want----")
                print("""    1> List the Customers in Bank
    2> List The Customers in Branch
    3> List Entire Full Details of the Banks
    4> Exit""")
                try:

                    print()
                    option4 = int(input("Enter Valid Option : "))

                    if option4 == 1:
                        # bank_open = None

                        while True:
                            bank_name = ""
                            banks_avail()
                            try:
                                print()
                                choice = int(input("Select The Bank to list the customers in that bank : "))
                                if choice == 1:
                                    bank_name = "sbi"
                                elif choice == 2:
                                    bank_name = "hdfc"
                                elif choice == 3:
                                    bank_name = "icici"
                                elif choice == 4:
                                    bank_name = "union"
                                elif choice == 5:
                                    bank_name = "axis"
                                else:
                                    print("Invalid Syntax")
                                    print("-TRY AGAIN-")
                                    continue
                                break
                            except ValueError:
                                print("Invalid Syntax")
                                print("-TRY AGAIN-")
                                continue

                        # while True:
                        #     bank_n = input("Enter Bank Name : ").lower()
                        #
                        #     if bank_n == "":
                        #         print("You Should Enter Bank Name")
                        #         continue
                        #     else:
                        #         break

                        with connection:
                            cursor.execute("SELECT * FROM bankaccounts WHERE bankname=:bankname", {'bankname': bank_name})

                            data = cursor.fetchall()

                            for i in data:
                                print(i)       ###################### printing data

                        # while True:
                        #     branch_n = input("Enter Branch Name : ").lower()
                        #
                        #     if branch_n == "":
                        #         print("You Should Enter Branch Name")
                        #         continue
                        #     else:
                        #         break

                        # for item in banks_list:
                        #     if item.name == bank_n:
                        #         bank_open = item
                        # bank_open.list_branch_customers(branch_n, False)

                    elif option4 == 2:
                        # bank_open2 = None
                        # while True:
                        #     bank_n = input("Enter Bank Name : ").lower()
                        #
                        #     if bank_n == "":
                        #         print("You Should Enter Bank Name")
                        #         continue
                        #     else:
                        #         break

                        while True:
                            print()
                            branch_n = input("Enter Branch Name : ").lower()

                            if branch_n == "":
                                print("You Should Enter Branch Name")
                                continue
                            else:
                                break

                        with connection:
                            cursor.execute("SELECT * FROM bankaccounts WHERE branchname=:branchname", {'branchname': branch_n})

                            data = cursor.fetchall()

                            if data is None:
                                print("The Entered Branch Does not exists")
                            else:

                                for i in data:
                                    print(i)       ###################### printing data

                        # for item in banks_list:
                        #     if item.name == bank_n:
                        #         bank_open2 = item
                        # branch_open2 = bank_open2.find_branch(branch_n)
                        # branch_open2.list_customers()

                    elif option4 == 3:

                        with connection:
                            cursor.execute("SELECT * FROM bankaccounts")
                            data = cursor.fetchall()

                            for i in data:
                                print(i)          ################# printing data

                        # for item in banks_list:
                        #     item.bank_details()

                    elif option4 == 4:
                        break

                except ValueError:
                    print("--INVALID OPTION ENTRY--")

                    continue

                continue

            continue

        elif option == 3:
            print()
            while True:
                print("-->[3] Visiting Bank :- ")
                print("    1> Slot Booking")
                print("    2> Exit")
                # while True:
                try:
                    print()
                    slot_opt = int(input("Enter Valid Option : "))
                    if slot_opt == 1:
                        main_booking()
                        continue
                    elif slot_opt == 2:
                        break
                    else:
                        print("Invalid Option Entered")
                        print("Try Again")
                        continue
                except ValueError:
                    print("Invalid Syntax - Try Again")
                # pass
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

