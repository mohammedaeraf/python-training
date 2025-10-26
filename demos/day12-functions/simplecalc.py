def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y

print("Select operation: +, -, *, /")
op = input("Enter operator: ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if op == '+':
    print("Result =", add(a, b))
elif op == '-':
    print("Result =", sub(a, b))
elif op == '*':
    print("Result =", mul(a, b))
elif op == '/':
    print("Result =", div(a, b))
else:
    print("Invalid operator")