# 0. Ask your user for a number between 0 and 1,000,000,000.
# 1. Use a `while` loop to find the number.
# 
# SCENARIO: When the number is found, exit the loop and 
# print the number to the console.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

number = int(input("Enter a number between 0 and 1,000,000,000: "))
search_range = range(1000000001)
found = False

while not found:
    if number not in search_range:
        print("Out of range!")
        number = int(input())
        continue
    else:
        print(f"Found the number: {number}")
        found = True
