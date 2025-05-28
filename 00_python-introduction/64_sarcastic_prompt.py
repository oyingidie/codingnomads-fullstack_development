# 0. Create a sarcastic program that asks a user for their honest opinion,
#    then prints the same sentence back to them in aLtErNaTiNg CaPs.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("I'm all ears, today... And alright as well.")

user_opinion = input("Please share your honest opinion: ")
sarcastic_response = ""
ironic = True

prompt = input("Please share your honest opinion: ")
sarcastic_response = ""

for char in prompt:
    char_index = prompt.index(char)
    if char_index % 2 == 0:
        sarcastic_response += char.lower()
    else:
        sarcastic_response += char.upper()

print(f"\nWow! your opinion is so unique. It really stands out:\n\"{sarcastic_response}\"")
