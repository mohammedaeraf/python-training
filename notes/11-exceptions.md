# ⚙️ **Python Tutorial – Exception Handling**

---

## 🟢 **1. What is an Exception?**

An **exception** is an **error** that occurs during program execution.

Example:

```python
num = int(input("Enter a number: "))
print(10 / num)
```

If the user enters `0` or a non-numeric value, the program will crash.
To handle such errors gracefully, we use **exception handling**.

---

## 🟢 **2. Basic try–except Block**

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except:
    print("An error occurred!")
```

✅ This prevents the program from crashing and prints a friendly message instead.

---

## 🟢 **3. Handling Specific Exceptions**

You can handle different types of errors separately.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
```

---

## 🟢 **4. Using `else` and `finally`**

* **`else`** runs if no exception occurs.
* **`finally`** always runs — useful for cleanup (e.g., closing files).

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")
finally:
    print("Program completed.")
```

---

## 🟢 **5. Raising Exceptions Manually**

You can raise your own exceptions using `raise`.

```python
age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative!")
else:
    print("Your age is", age)
```

---

## 🟢 **6. Example: Handling File Errors**

```python
try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found! Please check the filename.")
```

---

## 🧩 **Mini Project – Safe Calculator**

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print("Result =", result)
    finally:
        print("Calculation complete.")

x = int(input("Enter numerator: "))
y = int(input("Enter denominator: "))
safe_divide(x, y)
```

---

## 🧠 **Assignment Ideas**

1. Write a program to handle invalid integer input from the user.
2. Create a calculator that catches invalid operations and zero division.
3. Handle file read errors (like missing or unreadable files).
4. Write a program that accepts age input and raises an exception for invalid age (<0 or >120).
5. Simulate ATM withdrawal – raise error if balance is insufficient.
