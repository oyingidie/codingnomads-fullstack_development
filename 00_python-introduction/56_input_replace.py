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
    retry = input("Would you like to try a different symbol? (Y/N): ")
    
    if retry.upper() == 'Y':
        symbol = input("New symbol: ")
    elif retry.upper() == 'N':
        print("Exiting the program...")
        exit()

words = words.replace(first_letter, symbol)
print("Your message is encoded successfully.")
preview = input("Would you like to see the encoded message? (y/n): ")

if preview.lower() == 'y':
    print(f"See your encoded message below: \n{words}")
else:
    print("You can always check your message later.\nGoodbye!")
