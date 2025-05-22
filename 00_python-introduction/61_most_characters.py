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

print("This a test of character; you'll be required to enter three strings.")

first_string = input("The first string: ")
second_string = input("The second string: ")
third_string = input("The third string: ")

length_0 = len(first_string)
length_1 = len(second_string)
length_2 = len(third_string)

if length_0 == length_1 and length_1 == length_2:
    print(f"All strings are equal with {length_0} charcter(s)")
elif length_0 > length_1 and length_0 > length_2:
    print(f"\"{first_string}\" is the longest string with {length_0} characters")