# SCENARIO: Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries
# before they lose.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import random

number = random.randint(1, 100)
attempts = 5
print("It's the Guess-My-Number game. Let's play!")

while attempts > 0:
    print(f"\nAttempts left: {attempts}")
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
        print("\nCongrats! \U0001F389\nYour guess is correct! \U0001F973")
        break
    elif guess < number:
        print("\nYour guess is too low...")
        attempts -= 1
    elif guess > number:
        print("\nYour guess is too high...")
        attempts -= 1
