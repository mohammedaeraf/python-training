# Program to calculate Square Root and Power
import math as m

val1 = input("Enter a number: ")
val = int(val1)
print(f"You entered: {val}")

# Calculate square root
sqrt = m.sqrt(val)
print(f"The square root of {val} is {sqrt}")

# Calculate power 
power = input("Enter the power: ")
exp = input("Enter the exponent: ")
print(f"{exp} raised to power {power} is {m.pow(int(exp), int(power))}")