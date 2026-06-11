# Even or Odd Program
# Odd -> 1,3,5,7...
# Even -> 2,4,6,8....
n = int(input("Enter a number: "))
remainder = n % 2;

if remainder == 0:
    print(f"{n} is an Even Number.")
else:
    print(f"{n} is an Odd Number.")
