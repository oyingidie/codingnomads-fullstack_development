# 0. Write a script that takes a string input from a user and prints
#    a total count of how often each individual vowel appeared.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

vowel_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
user_input = input("Enter a string: ")

for vowel in vowels:
    vowel_count += user_input.lower().count(vowel)
    print(f"The vowel '{vowel}' appeared {vowel_count} times ")
