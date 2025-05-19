# 0. Write a script that takes a string of words and a symbol from the user.
# 1. Replace all occurrences of the first letter with the symbol.
#    Example:
#
#           String input: more python programming please
#           Symbol input: §
#           Result: §ore python progra§§ing please
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

words = input("Enter a string of words: ")
symbol = input("Enter a symbol: ")
first_letter = words[0]

while len(symbol) != 1 or symbol.isalpha():
    print(f"'{symbol}' is not a symbol.")
    symbol = input("Please enter only one symbol: ")