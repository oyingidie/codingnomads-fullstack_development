# 0. Fetch the text of the CodingNomads collaborative story from:
#    https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt
# 1. Save it to a variable in this script and remember to use triple-double quotes
#    for creating a multi-line string.
# 2. Use a `for` loop to iterate over the story text
#    and string slicing to translate it to ~pig latin.
# 
# SCENARIO: For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# 
# TIP: You'll need to use conditional statements to decide when a word is over.
#           e.g. You would never guess --> ouyay ouldway evernay uessgay
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# fetch story (import or copy-paste)
story = """Once upon a time, in a land far, far away, there lived a
group of adventurers. They were brave and bold, always seeking new
challenges and experiences. One day, they stumbled upon a mysterious
cave that was said to hold great treasures. As they entered the cave,
they could feel the excitement in the air. Little did they know, this 
adventure would change their lives forever."""

# initialise variable for translation
pig_latin_story = ""

# iterate over each word in the story
for word in story.split():
    # check if the word is valid
    if word.isalpha():    
        # translate

        # otherwise add word as is

# print the translated story
print(pig_latin_story)
