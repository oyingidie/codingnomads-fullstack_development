# 0. Ask the user to input their name.
# 1. Print a nice welcome message that welcomes them personally to your script.
# 2. If a user enters more than one name, e.g. "firstname lastname",
#    then use only their first name to overstep some personal boundaries
#    in your welcome message.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

name = input("Please provide your name: ")

if " " in name:
    first_name = name.split(" ")[0]
else:
    first_name = name
    