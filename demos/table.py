def printTable(n):
    print("Printing table of", n)
    print("-" * 25)
    for i in range(1,11):
        product = n * i
        print(f"{n} x {i} = {product}")
    print()


def greetUser(name):
    print("As salam alaykum", name)