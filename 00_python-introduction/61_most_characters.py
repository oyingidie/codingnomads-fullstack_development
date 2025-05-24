# 0. Write a script that takes three strings from the user
#    and prints the longest string together with its length.
#
#       Example [Input]:
#                   -   hello
#                   -   world
#                   -   greetings
#
#       Example [Output]:
#                   -   9, greetings
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("This a test of character \U0001F609... You'll be required to enter three strings.")
print("Your string can be a word, a number, or a sentence; but it cannot be empty.\n")

first_string = input("The first string: ")
second_string = input("The second string: ")
third_string = input("The third string: ")
length_0 = len(first_string)
length_1 = len(second_string)
length_2 = len(third_string)

while (length_0 == 0) and (length_1 == 0) and (length_2 == 0):
    print("Your strings cannot be empty! Try again.")
    first_string = input("Your first string: ")
    second_string = input("Your second string: ")
    third_string = input("Your third string: ")
    length_0 = len(first_string)
    length_1 = len(second_string)
    length_2 = len(third_string)


while (length_0 == 0) or (length_1 == 0) or (length_2 == 0):
    if (length_0 == 0) and (length_1 == 0):
        print("Both your first and second strings are empty. Please enter a string for each.")
        first_string = input("Your first string: ")
        second_string = input("Your second string: ")
        length_0 = len(first_string)
        length_1 = len(second_string)
    elif (length_0 == 0) and (length_2 == 0):
        print("Both your first and third strings are empty. Please enter a string for each.")
        first_string = input("Your first string: ")
        third_string = input("Your third string: ")
        length_0 = len(first_string)
        length_2 = len(third_string)
    elif (length_1 == 0) and (length_2 == 0):
        print("Both your second and third strings are empty. Please enter a string for each.")
        second_string = input("Your second string: ")
        third_string = input("Your third string: ")
        length_1 = len(second_string)
        length_2 = len(third_string)
    elif length_0 == 0:
        first_string = input("Your first string is empty.\nPlease enter a string: ")
        length_0 = len(first_string)
    elif length_1 == 0:
        second_string = input("Your second string is empty.\nPlease enter a string: ")
        length_1 = len(second_string)
    elif length_2 == 0:
        third_string = input("Your third string is empty.\nPlease enter a string: ")
        length_2 = len(third_string)


if (length_0 > length_1) and (length_0 > length_2):
    print(f"\"{first_string}\" is the longest string with {length_0} characters!")
elif (length_1 > length_0) and (length_1 > length_2):
    print(f"\"{second_string}\" is the longest string with {length_1} characters!")
elif (length_2 > length_0) and (length_2 > length_1):
    print(f"\"{third_string}\" is the longest string with {length_2} characters!")
elif (length_0 == length_1) and (length_0 > length_2):
    print(f"Both \"{first_string}\" and \"{second_string}\" are the longest strings with {length_0} characters each.")
elif (length_0 == length_2) and (length_0 > length_1):
    print(f"Both \"{first_string}\" and \"{third_string}\" are the longest strings with {length_0} characters each.")
elif (length_1 == length_2) and (length_1 > length_0):
    print(f"Both \"{second_string}\" and \"{third_string}\" are the longest strings with {length_1} characters each.")
else:
    print(f"All strings are of equal length with {length_0} character(s) each.")
