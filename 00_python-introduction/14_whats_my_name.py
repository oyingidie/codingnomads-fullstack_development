# 0. What data type is the variable `mystery` at the end of the script?
# 1. What data types does it hold at certain points earlier in the script?
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

mystery = None # type: NoneType
mystery = "Sommerfeld" # type: str
mystery = 137 # type: int
mystery = mystery + 0.0 # type: float

# display the data type of the updated variable
print(type(mystery))
