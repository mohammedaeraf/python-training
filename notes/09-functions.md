# 🧮 **Python Tutorial – Functions**

---

## 🟢 **1. What is a Function?**

A **function** is a reusable block of code that performs a specific task.
Functions help organize and avoid repetition in programs.

---

## 🟢 **2. Defining and Calling a Function**

```python
def greet():
    print("Hello from Python!")

# calling the function
greet()
```

✅ **Output:**

```
Hello from Python!
```

---

## 🟢 **3. Function with Parameters**

```python
def greet(name):
    print("Hello", name)

greet("Ali")
greet("Sara")
```

✅ **Output:**

```
Hello Ali
Hello Sara
```

---

## 🟢 **4. Function with Return Value**

```python
def add(x, y):
    return x + y

result = add(10, 20)
print("Sum =", result)
```

✅ **Output:**

```
Sum = 30
```

---

## 🟢 **5. Default Parameter Value**

```python
def greet(name="Friend"):
    print("Hi", name)

greet("Sara")
greet()
```

✅ **Output:**

```
Hi Sara
Hi Friend
```

---

## 🟢 **6. Keyword Arguments**

You can specify parameters by name while calling.

```python
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=20, name="Ali")
```

✅ Output:

```
Name: Ali
Age: 20
```

---

## 🟢 **7. Return Multiple Values**

```python
def calculate(a, b):
    sum = a + b
    diff = a - b
    return sum, diff

s, d = calculate(10, 5)
print("Sum =", s)
print("Difference =", d)
```

✅ Output:

```
Sum = 15
Difference = 5
```

---

## 🟢 **8. Function with Loop Example**

```python
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

print_table(5)
```

---

## 🟢 **9. Lambda (Anonymous) Functions**

Lambda functions are short, one-line functions.

```python
square = lambda x: x * x
print(square(4))
```

✅ Output:

```
16
```

---

## 🧩 **Mini Project – Simple Calculator**

```python
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
```

---

## 🧠 **Assignment Ideas**

1. Write a function to find the factorial of a number.
2. Write a function to check whether a number is prime.
3. Write a function to count vowels in a string.
4. Write a function that accepts a list and returns the largest number.
5. Write a function to calculate area of a circle (use default value of π = 3.142).
