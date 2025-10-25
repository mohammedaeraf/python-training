def greet():
    print("Hello!")
greet()

def greetUser(name):
    print(f"Hello, {name}!")
greetUser("Aeraf")

def greet2(name="User"):
    print(f"Hello, {name}!")    
greet2()
greet2("Abdullaah")

def add(a, b):
    return a + b

print(add(5, 3))

def student_info(name, age=18, grade="A"):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student_info(age=19, name="Alice")

def calculate(a,b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result

s, d = calculate(10, 5)
print(f"Sum: {s}, Difference: {d}")

def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
print_table(7)