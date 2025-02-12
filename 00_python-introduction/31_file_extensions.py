# 0. Use a Python string method to prove which of the following files
#    are .pdf files, and which aren't.
#       - operators.pdf
#       - snowfall.jpg  
#       - uncle-joes-wedding.doc
#       - invitation.pdf
#
# 1. Call the method on each file string and print() Python's response.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# define file names
file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

# check first file
if file_1.endswith(".pdf"):
    print('"' + file_1 + '"', "is a PDF file.")
else:
    print('"' + file_1 + '"', "is not a PDF file.")

# check second file
if file_2.endswith(".pdf"):
    print('"' + file_2 + '"', "is a PDF file.")
else:
    print('"' + file_2 + '"', "is not a PDF file.")

# check third file
if file_3.endswith(".pdf"):
    print('"' + file_3 + '"', "is a PDF file.")
else:
    print('"' + file_3 + '"', "is not a PDF file.")

# check fourth file
if file_4.endswith(".pdf"):
    print('"' + file_4 + '"', "is a PDF file.")
else:
    print('"' + file_4 + '"', "is not a PDF file.")
