import pickle
# Importing Bank Details
try:
    with open("bank_data.pkl", 'rb') as bank_data:
        sbi_bank = pickle.load(bank_data)
        hdfc_bank = pickle.load(bank_data)
        icici_bank = pickle.load(bank_data)
        union_bank = pickle.load(bank_data)
        axis_bank = pickle.load(bank_data)
except:
    print("No data Found")

banks_list = [sbi_bank, hdfc_bank, icici_bank, union_bank, axis_bank]

