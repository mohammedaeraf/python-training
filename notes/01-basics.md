# 🐍 **Python Basics – Variables, Statements, Print, and Input**

---

## 🔹 1. Introduction

Now that Python is installed and ready, let’s start writing some code!
In this tutorial, you’ll learn about:

* Variables
* Statements
* Printing output
* Taking user input

---

## 🔹 2. Variables in Python

A **variable** is a name used to store a value in memory.

### ✨ Example:

```python
name = "Alice"
age = 20
height = 5.6
```

Here:

* `name` → stores a **string**
* `age` → stores an **integer**
* `height` → stores a **float (decimal number)**

### ✅ Rules for Naming Variables:

* Must start with a **letter or underscore** (`_`)
* Can contain **letters, numbers, and underscores**
* **Case-sensitive** (`Age` ≠ `age`)
* Should not be a **Python keyword** (`for`, `if`, `class`, etc.)

### ⚠️ Invalid Examples:

```python
2name = "John"    # ❌ starts with a number
first-name = "Ali" # ❌ hyphen not allowed
```

---

## 🔹 3. Statements

A **statement** is a single line of code that performs an action.
Examples:

```python
x = 10          # assignment statement
y = 20
sum = x + y     # expression statement
print(sum)      # function call statement
```

Python executes statements **from top to bottom**.

---

## 🔹 4. The `print()` Function

Used to **display output** on the screen.

### Example:

```python
print("Hello, World!")
print("My name is Alice")
print("I am", 20, "years old")
```

**Output:**

```
Hello, World!
My name is Alice
I am 20 years old
```

You can also **format text**:

```python
name = "Ali"
age = 21
print(f"My name is {name} and I am {age} years old.")
```

**Output:**

```
My name is Ali and I am 21 years old.
```

---

## 🔹 5. The `input()` Function

Used to **take input** from the user.

### Example:

```python
name = input("Enter your name: ")
print("Hello", name)
```

**Output:**

```
Enter your name: Alice
Hello Alice
```

🧠 **Note:**
`input()` always returns a **string**.
If you want a number, convert it using `int()` or `float()`.

### Example:

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum =", sum)
```

---

## 🔹 6. Example Programs

### 🧮 Program 1: Add Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The sum is:", a + b)
```

### 🎂 Program 2: Display Name and Age

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello", name + "!", "You are", age, "years old.")
```

### 🌡️ Program 3: Convert Celsius to Fahrenheit

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
```

---

## 🔹 7. Summary

✅ You learned:

* What variables are
* Writing simple statements
* Printing output using `print()`
* Taking input from users using `input()`
* Converting input values to numbers

---

## 🔹 8. Practice Assignment

Try these on your own:

1. Write a program to ask your name and favorite color, then print:

   ```
   Hello John, your favorite color is Blue.
   ```

2. Take two numbers and print their product.

3. Write a program to find the area of a rectangle using `length * width`.

4. Ask user for city and temperature, then print:

   ```
   The temperature in Mangalore is 29°C.
   ```
