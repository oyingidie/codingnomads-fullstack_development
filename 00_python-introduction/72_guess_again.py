# SCENARIO: Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries
# before they lose.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import random

number = random.randint(1, 100)
attempt = 5
print("It's the Guess-My-Number game. Let's play! \U0001F3B2")

while attempt > 0:
    print(f"\nAttempt(s) left: {attempt}")
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
        print("Congrats! \U0001F389\nYour guess is correct! \U0001F973")
        break
    elif guess < number:
        if attempt > 1:
            print("Your guess is too low... Try again.")
        attempt -= 1
    elif guess > number:
        if attempt > 1:
            print("Your guess is too high... Try again.")
        attempt -= 1

if attempt == 0:
    print("\N{mathematical bold capital g}" + ' '\
    + "\N{mathematical bold capital a}" + ' '\
    + "\N{mathematical bold capital m}" + ' '\
    + "\N{mathematical bold capital e}" + " - "\
    + "\N{mathematical bold capital o}" + ' '\
    + "\N{mathematical bold capital v}" + ' '\
    + "\N{mathematical bold capital e}" + ' '\
    + "\N{mathematical bold capital r}" + ' '\
    + "\U0001F3B3")
