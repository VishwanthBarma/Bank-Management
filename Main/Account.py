# Account Class
import pickle

total_account = []


class Acc:
    accounts = []

    def __init__(self, username, password, number):
        self.username = username
        self.password = password
        self.number = number

    def find_account(self, username):
        for acc in self.accounts:
            if acc.name == username:
                return acc
            else:
                print("NO ACCOUNT")
                return False

    def create_account(self, username, password, number):
        if not self.find_account(username):
            new_acc = Acc(username, password, number)
            self.accounts.append(new_acc)
        else:
            print("Account already exists")

        self.update()

    def remove_account(self, username):
        acc = self.find_account(username)
        if not acc:
            print(f"No account exists with username - {username}")
            return False
        else:
            self.accounts.remove(acc)
            print("Account Deleted Successfully")
            self.update()
            return True

    def update_name(self, username, new_ur):
        acc = self.find_account(username)
        if not acc:
            print("Account Not Found")
            return False
        else:
            acc.username = new_ur
            self.update()
            return True

    def update_pass(self, username, passwo):
        acc = self.find_account(username)
        if not acc:
            print("Account Not Found")
            return False
        else:
            acc.password = passwo
            self.update()
            return True

    def update_num(self, username, num):
        acc = self.find_account(username)
        if not acc:
            print("Account Not Found")
            return False
        else:
            acc.number = num
            self.update()
            return True

    def update(self):
        del total_account[:]
        for curr in self.accounts:
            total_account.append(curr)


class Accounts(Acc):
    accounts = []

    def __init__(self, username, password, number):
        super().__init__(username, password, number)
        new_acc = Acc(username, password, number)
        self.accounts.append(new_acc)
        total_account.append(new_acc)

    def find_account(self, username):
        for acc in self.accounts:
            if acc.username == username:
                return acc
            else:
                print("NO ACCOUNT")
                return False

    def create_account(self, username, password, number):
        if not self.find_account(username):
            new_acc = Acc(username, password, number)
            self.accounts.append(new_acc)
        else:
            print("Account already exists")

        self.update()

    def remove_account(self, username):
        acc = self.find_account(username)
        if not acc:
            print(f"No account exists with username - {username}")
            return False
        else:
            self.accounts.remove(acc)
            print("Account Deleted Successfully")
            self.update()
            return True

    def update_name(self, username, new_ur):
        acc = self.find_account(username)
        if not acc:
            print("Account Not Found")
            return False
        else:
            acc.username = new_ur
            self.update()
            return True

    def update_pass(self, username, passwo):
        acc = self.find_account(username)
        if not acc:
            print("Account Not Found")
            return False
        else:
            acc.password = passwo
            self.update()
            return True

    def update_num(self, username, num):
        acc = self.find_account(username)
        if not acc:
            print("Account Not Found")
            return False
        else:
            acc.number = num
            self.update()
            return True






# def load_dumped_data():
#     try:
#         with open("bank_data.pkl", 'rb') as bank_data:
#             sbi_bank = pickle.load(bank_data)
#             hdfc_bank = pickle.load(bank_data)
#             icici_bank = pickle.load(bank_data)
#             union_bank = pickle.load(bank_data)
#             axis_bank = pickle.load(bank_data)
#     except:
#         print("No data Found")
#
#     banks_info = [sbi_bank, hdfc_bank, icici_bank, union_bank, axis_bank]
#
#     for i in banks_info:
#         banks_list.append(i)


# a1 = Accounts("ajf", "aldbbia", 35619)
# print(a1.number)
