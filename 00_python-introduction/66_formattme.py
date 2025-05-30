# SCENARIO: Fix the wikipedia blurb below by replacing the value for `animal`
# with the name of the animal that the text is talking about.
# Then, change the that way you're displaying the multi-line string
# so that the output doesn't show any superfluous spacing.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("This is the ultimate One-Word Exercise!")

start = input("Type 'start' to begin: ")

while start.lower() != "start":
    print("You have not entered the correct keyword. Please try again.")
    start = input("Type 'start' to begin: ")

riddle = input("Riddle me this...\n\"I have whiskers and paws,\nI catch with my claws,\
\nI roam the night,\nAnd I purr with delight.\nWhat am I?\"\n")

animal = riddle.lower()
blurb = f"The {animal} (Felis {animal}us) is a domestic species of small \
        carnivorous mammal. It is the only domesti{animal}ed species \
        in the family Felidae and is often referred to as the \
        domestic {animal} to distinguish it from the wild members of the family."

print(blurb)