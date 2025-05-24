# 0. Write a script that takes a string input from a user and prints
#    a total count of how often each individual vowel appeared.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
control = "\N{mathematical bold capital d}"\

print(f"Hello! My name is {control}... I'm on the lookout for vowels in your data.")
player_name = input("What is your name, please? ")

while " " in player_name:
    player_name = player_name.split(" ")[0]

if player_name:
    player = player_name
else:
    player = "Anonymous"

print(f"\nNice to meet you, {player}!")
user_input = input("Enter any data of your choice: ")

vowels = ['a', 'e', 'i', 'o', 'u']

for vowel in vowels:
    vowel_count = 0
    vowel_count += user_input.lower().count(vowel)

    if vowel_count == 0:
        print(f"\nYour data does not contain the vowel '{vowel}'.")
    elif vowel_count == 1:
        print(f"\nThe vowel '{vowel}' appeared only once in your data.")
    else:
        print(f"\nThe vowel '{vowel}' appeared {vowel_count} times in your data.")
