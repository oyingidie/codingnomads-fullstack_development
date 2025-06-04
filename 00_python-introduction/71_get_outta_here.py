# 0. Use the built-in `sys` module to explicitly quit your script.
# 1. Include this functionality into a loop where you're asking the user
#    for input in an infinite `while` loop.
#
# SCENARIO: If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import sys
import time

while True:
    user_input = input("Can I see something interesting, please? ")

    if user_input.lower() == "quit":
        print("[User bored. System terminates in 3, 2, 1...]")
        time.sleep(3)
        sys.exit()
    else:
        print("Urrghh... ")
        time.sleep(1.5)
        print("Not close enough. \U0001F615")
        time.sleep(1.5)
