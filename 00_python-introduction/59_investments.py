# 0. Take in the following three values from the user:
#       -   investment amount
#       -   interest rate in percentage
#       -   number of years to invest
#
# 1. Calculate the future values and print them to the console.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

amount = float(input("Enter your investment amount: "))
interest_rate = float(input("Enter your preferred interest rate in percentage: "))
period = int(input("Enter the number of years you wish to invest for: "))

future_value = amount * (1 + interest_rate / 100) ** period

print(f"Your investment of {amount} will be worth {future_value:.2f} in {period} years time.")
