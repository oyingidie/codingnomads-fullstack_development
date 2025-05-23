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
    print("A \"new\" symbol is required to encode your message.")
    retry = input("Would you like to proceed? [Y/N]: ")

    while retry.upper() not in ['Y', 'N']:
        retry = input("Invalid option. Enter 'Y' [Yes] or 'N' [No]: ")
    if retry.upper() == 'Y':
        symbol = input("New symbol: ")
    else:
        print("Exiting the program...")
        exit()

words = words.replace(first_letter, symbol)
print("Your message is encoded successfully.")
preview = input("Would you like to see the encoded message? (Y/N): ")

while preview.upper() not in ['Y', 'N']:
        preview = input("Invalid option. Enter 'Y' [Yes] or 'N' [No]: ")
if preview.upper() == 'Y':
    print(f"See your encoded message below: \n{words}")
else:
    print("You can always preview your secret message later.\nGoodbye!")
