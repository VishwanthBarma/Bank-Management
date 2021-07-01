# Account Class
class Account:
    accounts = []

    def __init__(self, username, password, number):
        self.username = username
        self.password = password
        self.number = number
        self.accounts.append(Account(username, password, number))

    def find_account(self, username):
        for acc in self.accounts:
            if acc.name == username:
                return acc
            else:
                print("NO ACCOUNT")
                return False

    def create_account(self, username, password, number):
        if not self.find_account(username):
            new_acc = Account(username, password, number)
            self.accounts.append(new_acc)
        else:
            print("Account already exists")

    def remove_account(self, username):
        acc = self.find_account(username)
        if not acc:
            print(f"No account exists with username - {username}")
            return False
        else:
            self.accounts.remove(acc)
            print("Account Deleted Successfully")
            return True

    def update_pass(self, username, passwo):
        acc = self.find_account(username)
        if not acc:
            print("Account Not Found")
            return False
        else:
            acc.password = passwo
            return True

    def update_num(self, username, num):
        acc = self.find_account(username)
        if not acc:
            print("Account Not Found")
            return False
        else:
            acc.number = num
            return True


