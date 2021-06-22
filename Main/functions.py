import pickle

banks_list = []

try:
    with open("bank_data.pkl", 'rb') as bank_data:
        sbi_bank = pickle.load(bank_data)
        hdfc_bank = pickle.load(bank_data)
        icici_bank = pickle.load(bank_data)
        union_bank = pickle.load(bank_data)
        axis_bank = pickle.load(bank_data)
except:
    print("No data Found")

sbi_bank.list_branch_customers("Balanagar", True)

# We need to store all banks in the list to print the full details of the customers including their transactions

# sbi_bank = Bank("State Bank Of India")
# hdfc_bank = Bank("HDFC Bank Of India")
# icici_bank = Bank("ICICI Bank")
# union_bank = Bank("Union Bank Of India")
# axis_bank = Bank("AXIS Bank")
