# SCENARIO: Fahrenheit to Celsius:
# 
# 0. Write the necessary code to convert a degree in Fahrenheit
#    to Celsius and print it to the console. Use variable names!
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5.0/9.0

print(fahrenheit, "degrees Fahrenheit is equal to", celsius, "degrees Celsius.")
