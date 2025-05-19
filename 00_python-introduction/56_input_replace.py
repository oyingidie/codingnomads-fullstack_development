# 0. Write a script that takes a string of words and a symbol from the user.
# 1. Replace all occurrences of the first letter with the symbol.
#    Example:
#
#           String input: more python programming please
#           Symbol input: §
#           Result: §ore python progra§§ing please
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

words = input("Input your message: ")
symbol = input("Choose an encoding symbol: ")
first_letter = words[0]

while len(symbol) != 1 or symbol.isalpha():
    print(f"'{symbol}' is not a symbol.")
    symbol = input("Please enter only one symbol: ")

while first_letter == symbol:
    print("A new symbol is required to encode your message.")
    retry = input("Would you like to try a different symbol? (y/n): ")
    if retry.lower() == 'y':
        symbol = input("New symbol: ")
    else:
        
    
else:
    words = words.replace(first_letter, symbol)
    print(f"")