from functions import *
from LoadData import banks_list

input("Press Enter To Start The Bank Management System")
start = True
while start:
    open_login = display_options1()
    start2 = True
    while start2:
        open_customer = display_options2()
        display_options3(open_login, open_customer)




