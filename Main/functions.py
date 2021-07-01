from LoadData import banks_list
########################
#      Functions       #
########################


def full_details():
    for bank in banks_list:
        bank.bank_details()


# sbi_bank = Bank("State Bank Of India")
# hdfc_bank = Bank("HDFC Bank Of India")
# icici_bank = Bank("ICICI Bank")
# union_bank = Bank("Union Bank Of India")
# axis_bank = Bank("AXIS Bank")
