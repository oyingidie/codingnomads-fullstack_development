# 0. Write a program that takes a number between 1 and 1,000,000,000 from the user
#    and determines whether it is divisible by 3 using an `if` statement.
# 1. Print the result.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

number = int(input("Please enter a number between 1 and 1,000,000,000: "))

while number < 1 or number > 1000000000:
    print("Ooops! That's not between 1 and 1,000,000,000.")
    reload = input("Wanna try again? Press Y or N: ")
    if reload.upper() == "Y":
        number = int(input("Please enter a number between 1 and 1,000,000,000: "))
    elif reload.upper() == "N":
        print("I hope you come back soon. Bye!")
        exit()
    else:
        print("That's not valid. The system will go to sleep now...")
        exit()

if number % 3 == 0:
    quotient = number // 3
    print(f"{number} is divisible by 3 to give '{quotient}'.")
