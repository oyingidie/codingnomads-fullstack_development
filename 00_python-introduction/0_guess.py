# programming concepts in the guess-my-number game

import random

number = random.randint(1, 30)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 30: "))
    
    if guess == number:
        print("Congratulations! You guessed correctly and won!")
        break
    else:
        print("Sorry, that's not it. Please try again.")
