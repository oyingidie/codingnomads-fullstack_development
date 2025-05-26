# 0. Take in a number between 1 and 12 from the user
#    and print the name of the associated month:
#               "January", "February", ... "December"
# 1. Print "Error" if the number from the user is not between 1 and 12.
# SCENARIO: Use a nested `if` statement.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

month_number = int(input("Enter a number for any month: "))

if 1 <= month_number <= 12:
    if month_number == 1:
        print(f"January is the {month_number}st month of the year.")
    elif month_number == 2:
        print(f"February is the {month_number}nd month of the year.")
    
