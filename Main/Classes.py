# ***************************
#  ****BANK APPLICATION****
# ***************************
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


# Branch Class (Bank)
class Branch:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def get_name(self):
        return self.name

    def get_customers(self):
        return list(self.customers)

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
                print("Customer ", index+1, ": ", end="")
                print(customer.name)

    def add_customer_transaction(self, name, transaction):
        customer = self.find_customer(name)
        if customer is not None:
            customer.add_transaction(transaction)
            return True
        return False


# Bank Class
class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def get_name(self):
        return self.name

    def get_branches(self):
        return self.branches

    def find_branch(self, name):
        if len(self.branches) != 0:
            for branch in self.branches:
                if branch.name == name:
                    return branch
        return None

    def add_branch(self, name):
        if self.find_branch(name) is None:
            new_branch = Branch(name)
            self.branches.append(new_branch)
            return True
        return False

    def add_customer(self, branch_name, customer_name, customer_transaction):
        branch = self.find_branch(branch_name)
        if branch is not None:
            return branch.new_customer(customer_name, customer_transaction)
        return False

    def add_customer_transaction(self, branch_name, customer_name, customer_transaction):
        branch = self.find_branch(branch_name)
        if branch is not None:
            return branch.add_customer_transaction(customer_name, customer_transaction)
        return False

    def list_branch_customers(self, branch_name, to_print_transactions : bool):
        branch = self.find_branch(branch_name)
        if branch is not None:
            if to_print_transactions:
                print("Bank Customers of Branch '{}' are : ".format(branch_name))
                branch_customers = list(branch.customers)
                for index, customer in enumerate(branch_customers):
                    print("Customer ", (index+1), " - ", customer.name)
                    print("-> Transactions : ", end=" ")
                    for transaction in customer.transactions:
                        print(transaction, end=", ")
                    print()
            else:
                branch.list_customers()
            return True
        return False

    # Creating a function in bank class to print all the customers of bank with not respect to branch of the bank
    # No branch is to specified in order to print the details of the customers
    # ****** Creating a function to print all details of customers without specifing the branch name

