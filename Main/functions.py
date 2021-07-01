from LoadData import banks_list


########################
#      Functions       #
########################


def full_details():
    for bank in banks_list:
        bank.bank_details()


def strong_pass_con():
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
    else:
        print("Password Invalid !!")


# password_checker("Hello")
# password_checker("1Arq@frds")


# sbi_bank = Bank("State Bank Of India")
# hdfc_bank = Bank("HDFC Bank Of India")
# icici_bank = Bank("ICICI Bank")
# union_bank = Bank("Union Bank Of India")
# axis_bank = Bank("AXIS Bank")
