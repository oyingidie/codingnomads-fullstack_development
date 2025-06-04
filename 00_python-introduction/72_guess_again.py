# SCENARIO: Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries
# before they lose.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import random

number = random.randint(1, 50)
attempts = 5
print("It's the Guess-My-Number game. Let's play!")

while attempts > 0:
