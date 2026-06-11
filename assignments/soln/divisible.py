# Program to find out if a number is divisible by 5
n = int(input("Enter a number: "))
rem = n % 5
print(f"Remainder = {rem}")
if rem == 0:
    print(f"{n} is divisible by 5")
else:
    print(f"{n} is not divisible by 5")
    
