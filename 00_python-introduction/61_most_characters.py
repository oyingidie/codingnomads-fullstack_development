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
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("This a test of character. You'll be required to enter three strings.\n")

first_string = input("The first string: ")
second_string = input("The second string: ")
third_string = input("The third string: ")

length_0 = len(first_string)
length_1 = len(second_string)
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
    print(f"All strings are of equal length with {length_0} charcter(s) each.")
