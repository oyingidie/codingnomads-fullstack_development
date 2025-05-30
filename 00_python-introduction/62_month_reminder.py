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
    elif month_number == 3:
        print(f"March is the {month_number}rd month of the year.")
    elif month_number == 4:
        print(f"April is the {month_number}th month of the year.")
    elif month_number == 5:
        print(f"May is the {month_number}th month of the year.")
    elif month_number == 6:
        print(f"June is the {month_number}th month of the year.")
    elif month_number == 7:
        print(f"July is the {month_number}th month of the year.")
    elif month_number == 8:
        print(f"August is the {month_number}th month of the year.")
    elif month_number == 9:
        print(f"September is the {month_number}th month of the year.")
    elif month_number == 10:
        print(f"October is the {month_number}th month of the year.")
    elif month_number == 11:
        print(f"November is the {month_number}th month of the year.")
    elif month_number == 12:
        print(f"December is the {month_number}th month of the year.")
else:
    print(f"Error: The Gregorian calendar does not have a {month_number}-month year.")

