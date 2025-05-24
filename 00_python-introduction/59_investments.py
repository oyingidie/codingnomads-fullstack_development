# 0. Take in the following three values from the user:
#       -   investment amount
#       -   interest rate in percentage
#       -   number of years to invest
#
# 1. Calculate the future values and print them to the console.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print(" >>> Investment Calculator <<< \n")

amount = float(input("Enter your investment amount: "))
interest_rate = float(input("Enter your preferred interest rate in percentage: "))
period = int(input("Enter the number of years you wish to invest for: "))

future_value = amount * (1 + interest_rate / 100) ** period

print(f"""\nAt an interest rate of {interest_rate}%,
your investment of {amount:.2f} will be worth
{future_value:.2f} in {period} years time.""")
