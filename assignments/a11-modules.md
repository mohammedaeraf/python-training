# 🧩 Assignment 09: Working with Modules in Python

## 📘 Instructions

1. Write each program in a separate Python file.
2. Use Python's built-in modules wherever required.
3. Display clear output messages.
4. Import only the required modules.
5. Test your programs before submission.

---

## 🔢 1️⃣ Using the `math` Module

**Problem:**

Write a Python program that imports the `math` module and displays:

* Square root of 81
* Value of π (pi)
* Value of 5²

### Example Output

```text
Square Root of 81 = 9.0
Value of Pi = 3.141592653589793
5² = 25.0
```

---

## 🎲 2️⃣ Generate a Random Number

**Problem:**

Write a Python program using the `random` module to generate a random number between 1 and 100.

### Example Output

```text
Random Number = 57
```

*(Output will be different each time.)*

---

## 🎯 3️⃣ Random Choice from a List

**Problem:**

Create a list of colors and display one random color using the `random.choice()` function.

### Example Output

```text
Selected Color = Blue
```

---

## 📅 4️⃣ Display Current Date and Time

**Problem:**

Write a Python program using the `datetime` module to display the current date and time.

### Example Output

```text
Current Date and Time:
2025-08-21 10:45:32
```

---

## ⏰ 5️⃣ Display Current Year

**Problem:**

Write a Python program that displays only the current year using the `datetime` module.

### Example Output

```text
Current Year = 2025
```

---

## 📂 6️⃣ Find the Current Working Directory

**Problem:**

Write a Python program using the `os` module to display the current working directory.

### Example Output

```text
Current Directory:
C:\PythonPrograms
```

---

## 📋 7️⃣ Create Your Own Module

**Problem:**

Create a file named `calculator.py` containing the following functions:

* `add(a, b)`
* `subtract(a, b)`

Then create another Python file that imports `calculator` and uses both functions.

### Example Output

```text
Addition = 30
Subtraction = 10
```

---

## 📦 8️⃣ Import Specific Functions from a Module

**Problem:**

Import only the `sqrt()` function from the `math` module and calculate the square root of 144.

### Example Output

```text
Square Root = 12.0
```

---

# ⭐ Bonus Question

## Student Utility Module

### Step 1: Create a Module

Create a file named `student.py` containing:

```python
def display_name(name):
    print("Student Name:", name)

def display_marks(marks):
    print("Marks:", marks)
```

### Step 2: Use the Module

Import the module and call both functions.

### Example Output

```text
Student Name: Ahmed
Marks: 85
```

---

# 🎯 Learning Outcomes

After completing this assignment, students will be able to:

✅ Import built-in Python modules
✅ Use functions from the `math`, `random`, `datetime`, and `os` modules
✅ Import specific functions from modules
✅ Create custom modules
✅ Use modules in multiple Python files
✅ Organize programs into reusable components
