def hello():
    print("hello, world!")

hello()  # Call the function to execute its code.

def add(a, b):
    return a + b

result = add(5, 3)  # Call the function with arguments and store the result.
print("The sum is:", result)  # Print the result of the addition.

def greet(name):
    return f"Hello, {name}!"

greeting = greet("Alice")  # Call the function with a name argument.
print(greeting)  # Print the greeting message.\

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

table(7)  # Call the function to print the multiplication table for 7.