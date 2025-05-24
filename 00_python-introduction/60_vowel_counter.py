# 0. Write a script that takes a string input from a user and prints
#    a total count of how often each individual vowel appeared.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

vowels = ['a', 'e', 'i', 'o', 'u']
user_input = input("Enter any data of your choice: ")

for vowel in vowels:
    vowel_count = 0
    vowel_count += user_input.lower().count(vowel)

    if vowel_count == 0:
        print(f"Your data does not contain the vowel '{vowel}'.")
    elif vowel_count == 1:
        print(f"The vowel '{vowel}' appeared only once in your data.")
    else:
        print(f"The vowel '{vowel}' appeared {vowel_count} times in your data.")
