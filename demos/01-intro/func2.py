# greet function
def greet(name):
    return f"Hello {name}!"

print(greet("Mohammed"))


# max function
def max_value(x, y):
    return x if x > y else y

print("Max is", max_value(11, 21))


# isEven function
def is_even(n):
    return True if n % 2 == 0 else False
    # (or simply: return n % 2 == 0)

print(is_even(10))


# constant PI and area function
PI = 3.142

def get_area(r):
    return PI * r * r

print("Area =", get_area(10))


# welcome function
def welcome():
    return "Welcome to Python"

print(welcome())
