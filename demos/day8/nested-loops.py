# Program to display multiplication tables from 1 to 5 using while loops

i = 1
while i <= 5:  # Outer loop for tables 1 to 5
    print(f"\nMultiplication Table of {i}")
    print("-" * 25)
    
    j = 1
    while j <= 10:  # Inner loop for 1 to 10

        print(f"{i} x {j} = {i * j}")
        j += 1
    
    i += 1
