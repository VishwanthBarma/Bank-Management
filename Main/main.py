from functions import *
from LoadData import banks_list

input("Press Enter To Start The Bank Management System")
start = True
while start:
    open_login = display_options1()
    if open_login == -1:
        break
    elif open_login == 0:
        continue
    print()
    open_customer = display_options2()
    # Should be Checked  -> display_options2()
    if open_customer == -1:
        continue

    start2 = True
    while start2:
        flag = display_options3(open_login, open_customer)
        if flag == -1:
            break
        print()
print("Exited The Program Successfully")


