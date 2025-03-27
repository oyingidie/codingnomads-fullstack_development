# 0. You start this journey with a number `n`.
# 1. You have to display a string representation of all numbers from 1 to n,
#    but there are some constraints:
#
#       - If the number is divisible by 3, write `Fizz` instead of the number
#       - If the number is divisible by 5, write `Buzz` instead of the number
#       - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

for num in range(1, n + 1):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
