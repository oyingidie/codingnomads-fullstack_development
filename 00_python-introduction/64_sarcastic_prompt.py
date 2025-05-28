# 0. Create a sarcastic program that asks a user for their honest opinion,
#    then prints the same sentence back to them in aLtErNaTiNg CaPs.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

prompt = input("Please share your honest opinion: ")
sarcastic_response = ""

for char in prompt:
    char_index = prompt.index(char)
    if char_index % 2 == 0:
        sarcastic_response += char.lower()
    else:
        sarcastic_response += char.upper()

