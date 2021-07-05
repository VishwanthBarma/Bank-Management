from functions import *
from LoadData import banks_list
from Data import dumping_data
from LoadData import load_dumped_data
from funtions2 import *

input("Press ENTER to start the BANK MANAGEMENT SYSTEM")

while True:  # Main Starting Options
    opt1 = display_function1()
    if opt1 == -1:     # -1 -> exit , 1-> success, 0 -> continue
        break
    elif opt1 == 0:
        continue

    a = 0

    while True:

        opt2 = display_functions2()
        if opt2 == -1:
            a = 1
        elif opt2 == 0:
            continue
        # Option 2 is data
        else:
            break

    if a == 1:
        continue

    while True:
        flag = display_functions3(opt2, opt1)
        if flag == -1:
            break
        print()

    continue


# # Dumping the data at the very first
# dumping_data()
#
# # Loading Dumped Data
# load_dumped_data()
#
# input("Press Enter To Start The Bank Management System")
# start = True
# while start:
#     open_login = display_options1()
#     if open_login == -1:
#         break
#     elif open_login == 0:
#         continue
#     print()
#     open_customer = display_options2()
#     # Should be Checked  -> display_options2()
#     if open_customer == -1:
#         continue
#
#     while True:
#         flag = display_options3(open_login, open_customer)
#         if flag == -1:
#             break
#         print()
#     continue


print()
print("********************************")
print("**SUCCESSFULLY PROGRAM EXITED**")
print("********************************")



