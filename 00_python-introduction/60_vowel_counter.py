# 0. Write a script that takes a string input from a user and prints
#    a total count of how often each individual vowel appeared.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


vowels = ['a', 'e', 'i', 'o', 'u']
user_input = input("Enter a text: ")

for vowel in vowels:
    vowel_count = 0
    vowel_count += user_input.lower().count(vowel)

    if vowel_count == 0:
        print(f"There is no '{vowel}' in the text.")
    elif vowel_count == 1:
        print(f"The vowel '{vowel}' appeared only once in the text.")
    else:
        print(f"The vowel '{vowel}' appeared {vowel_count} times in the text.")
