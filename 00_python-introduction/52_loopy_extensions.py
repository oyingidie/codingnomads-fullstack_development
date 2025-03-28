# 0: Proof that the following file is a .pdf file using a `for` loop.
#           - filename = "operators.pdf"
#
# 1: Don't use the string method you've used to solve this before!
# 2: Don't use the `in` keyword to look for a sub-string!
# 3: Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

filename = "operators.pdf"
is_pdf = False

# loop through the filename
for i in range(len(filename)):
    # check if extension is .pdf
    if filename[i] == '.':
        if filename[i + 1] == 'p':
            if filename[i + 2] == 'd':
                if filename[i + 3] == 'f':
                    is_pdf = True
                    break

if is_pdf:
    print('"' + filename + '" is a PDF file.')
else:
    print('"' + filename + '" is not a PDF file.')
