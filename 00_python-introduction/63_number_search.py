# 0. Ask your user for a number between 0 and 1,000,000,000.
# 1. Use a `while` loop to find the number.
# 
# SCENARIO: When the number is found, exit the loop and 
# print the number to the console.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

number = int(input("Enter a number between 0 and 1,000,000,000: "))
found = False
search_list = range(1000000001)

if 0 > number or number > 1000000000:
    print("Out of range!")
else:
    for item in search_list:
        if item == number:
            found = True
            print(f"Number found: {item}")
            break