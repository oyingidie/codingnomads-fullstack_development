# 0. Write a script that takes a string of words and a letter from the user.
# 1. Find the index of first occurrence of the letter in the string.
#    Example:
#
#           String input: hello world
#           Letter input: o
#           Result: 4
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

words = input("Enter a string of words: ")
letter = input("Enter a letter: ")

if letter in words:
    index = words.index(letter)
    print(f"The first occurrence of {letter} in the string is at index: {index}")
    