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


class Branch:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def get_name(self):
        return self.name

    def get_customers(self):
        return self.customers

    def find_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer   # Return the customer if the customer exits
        return None

    def new_customer(self, name, transaction):
        if self.find_customer(name) is None:
            new_customer = Customer(name, transaction)
            self.customers.append(new_customer)
            return True   # In case if the customer added to the branch customers list successfully
        print("Customer '{}' already exists".format(name))
        return False

    def list_customers(self):
        if len(self.customers) != 0:
            print("Bank Customers of Branch '{}' are : ".format(self.name))
            for index, customer in enumerate(self.customers):
                print(index+1, ": ", end="")
                print(customer.name)

    def add_customer_transaction(self, name, transaction):
        customer = self.find_customer(name)
        if customer is not None:
            customer.add_transaction(transaction)
            return True
        return False


# branch1 = Branch("SBI")
# branch1.new_customer("Vishwanth", 200)
# branch1.new_customer("Vishwanth", 302)
# branch1.new_customer("Hima", 23)
# branch1.list_customers()


#
# c1 = Customer("Vishwanth", 20)
# print(c1.get_transactions())
# print(c1.get_name())
# c1.add_transaction(30)
# print(c1.get_transactions())
# c2 = Customer("Hima", 340)
# c2.add_transaction(47)
# print(c2.get_transactions())
# print(c2.get_name())
# print(c1.get_name())

