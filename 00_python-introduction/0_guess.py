# 0. Identify the programming concepts in the guess-my-number game.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# - getting a package (code written by someone else)
import random

# - variable and assignment
# - using a function from a package
number = random.randint(1, 30)
guess = None

# - while loop
# - comparison operator
while guess != number:
    # - indentation
    # - collecting user input
    # - type conversion
    guess = int(input("Guess a number between 1 and 30: "))
    
    # - conditional statement
    # - control statement
    # - terminal output
    if guess == number:
        print("Congratulations! You guessed correctly and won!")
        break
    else:
        print("Sorry, that's not it. Please try again.")
