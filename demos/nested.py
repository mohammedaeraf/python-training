i = 1
while i<=10:
    print(f"Printing Table of {i}")
    print("-" * 25)

    j = 1
    while j<=10:
        product = i * j
        print(f"{i} x {j} = {product}")
        j = j + 1
    
    print()
    i = i + 1