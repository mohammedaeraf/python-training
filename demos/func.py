# Functions / Methods

# defining a function
def greet():
    print("Hello Dear!")

greet() # calling the function

def greetUser(name):
    print("Hello", name)

greetUser("Arif")
greetUser("Usman")

def add(a,b):
    result = a + b
    print("Result =", result)

add(3,4)


def printTable(n):
    print("Printing table of", n)
    print("-" * 25)
    for i in range(1,11):
        product = n * i
        print(f"{n} x {i} = {product}")
    print()
    
printTable(5)
printTable(16)
