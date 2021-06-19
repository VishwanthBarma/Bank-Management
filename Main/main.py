# Bank Application
# Customer Class (User)
class Customer:
    def __init__(self, name, transaction):
        self.name = name
        self.transactions = []
        self.transactions.append(transaction)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        print("Adding transactions '{}' to account of '{}'".format(transaction, self.name))

    def get_name(self):
        return self.name

    def get_transactions(self):
        return self.transactions


c1 = Customer("Vishwanth", 20)
print(c1.get_transactions())
print(c1.get_name())
c1.add_transaction(30)
print(c1.get_transactions())
c2 = Customer("Hima", 340)
c2.add_transaction(47)
print(c2.get_transactions())
print(c2.get_name())
print(c1.get_name())
