# SCENARIO: Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries
# before they lose.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import random

number = random.randint(1, 100)
attempts = 5
print("It's the Guess-My-Number game. Let's play!\n")

while attempts > 0:
    print(f"Attempts left: {attempts}")
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
        print("Congrats! \U0001F389 Your guess is correct! \U0001F973")