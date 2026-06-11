# Program to print sum of 1st n natural numbers
n = int(input("Enter first number: "))
total = 0

for i in range(1, n+1):
    total = total + i

print(f"Total = {total}")