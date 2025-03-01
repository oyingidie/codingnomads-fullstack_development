# 0. Decipher the message within the `secret` variable.
# 1. Pick out only the alphabetic characters, not the numbers.
#
# code >>>  secret = "2349h30023388281e3299371l1l3094842o0333322883"
#           solution = ""   >>>
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = ""

for char in secret:
    if char.isalpha:
        solution += char

print(solution)
