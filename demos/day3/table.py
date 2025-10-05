n = int(input("Enter number for which you want table: "))

for i in range(1,100001):
    product = n * i;
    print(f"{n} x {i} = {product}")