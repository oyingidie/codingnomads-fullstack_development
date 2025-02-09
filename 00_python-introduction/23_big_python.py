# 0. Write the necessary code to print the BIG PYTHON string shown below.
# 1. Research multi-line strings to make this easier for you :)
#
#       PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N
#       P   P   Y   Y       T      H    H     O O    N N     N
#       P   P    Y Y        T      H    H    O   O   N  N    N
#       PPPP      Y         T      HHHHHH    O   O   N   N   N
#       P         Y         T      H    H    O   O   N    N  N
#       P         Y         T      H    H     O O    N     N N
#       P         Y         T      H    H      O     N       N
#
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# using triple quotes
big_python_quoted = """
PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N
P   P   Y   Y       T      H    H     O O    N N     N
P   P    Y Y        T      H    H    O   O   N  N    N
PPPP      Y         T      HHHHHH    O   O   N   N   N
P         Y         T      H    H    O   O   N    N  N
P         Y         T      H    H     O O    N     N N
P         Y         T      H    H      O     N       N
"""

# using parentheses and escape characters
big_python_escaped = (
    "PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N\n"
    "P   P   Y   Y       T      H    H     O O    N N     N\n"
    "P   P    Y Y        T      H    H    O   O   N  N    N\n"
    "PPPP      Y         T      HHHHHH    O   O   N   N   N\n"
    "P         Y         T      H    H    O   O   N    N  N\n"
    "P         Y         T      H    H     O O    N     N N\n"
    "P         Y         T      H    H      O     N       N\n"
)

# using the join method
big_python_joined = "\n".join([
    "PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N",
    "P   P   Y   Y       T      H    H     O O    N N     N",
    "P   P    Y Y        T      H    H    O   O   N  N    N",
    "PPPP      Y         T      HHHHHH    O   O   N   N   N",
    "P         Y         T      H    H    O   O   N    N  N",
    "P         Y         T      H    H     O O    N     N N",
    "P         Y         T      H    H      O     N       N",
])

# same output for all ˜\_(ツ)_/˜
print(big_python_quoted)
print(big_python_escaped)
print(big_python_joined)
