# SCENARIO: Fix the wikipedia blurb below by replacing the value for `animal`
# with the name of the animal that the text is talking about.
# Then, change the that way you're displaying the multi-line string
# so that the output doesn't show any superfluous spacing.
#
# code >>>  animal = None
#           blurb = "The {animal} (Felis {animal}us) is a domestic species of small \
#                   carnivorous mammal. It is the only domesti{animal}ed species \
#                   in the family Felidae and is often referred to as the \
#                   domestic {animal} to distinguish it from the wild members of the family." >>>
#
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("This is the ultimate One-Word Exercise!")
start = input("Type *'start'* to begin: ")

while start.lower() != "start":
    print("You have not entered the correct keyword. Please try again.")
    start = input("Type *'start'* to begin: ")

riddle = input("\nRiddle me this...\n\"I have whiskers and paws,\nI catch with my claws,\
\nI roam the night,\nAnd I purr with delight.\nWhat am I?\"")
animal = riddle.lower()

if animal == "cat":
    print("\nCorrect! You are a genius!")
    blurb = f"The {animal} (Felis {animal}us) is a domestic species of small \
carnivorous mammal. It is the only domesti{animal}ed species \
in the family Felidae and is often referred to as the \
domestic {animal} to distinguish it from the wild members of the family. \
The {animal} is often valued by humans for companionship and its ability to hunt vermin."
else:
    print("\nHmmm... Not quite right.")
    blurb = "It seems you are not familiar with the animal world. \
I recommend you binge on Discovery Channel's Animal Planet ."

print(blurb)
