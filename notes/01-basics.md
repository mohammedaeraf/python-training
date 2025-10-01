Perfect 👍 — let’s create **beginner-friendly tutorial notes for Week 1** of your **20-day Python course**.
Each session is just **20 minutes**, so the notes are **short, clear, and demo-oriented** with examples + mini exercises.

---

# 🐍 Python Course – Week 1 Notes (Days 1–5)

---

## **Day 1 – Introduction & Setup**

### 🔹 What is Python?

* High-level, easy-to-learn programming language
* Used in:

  * Web Development (Django, Flask)
  * Data Science (NumPy, Pandas, Matplotlib)
  * AI & ML (TensorFlow, PyTorch)
  * Automation & Scripting

### 🔹 Installation & Setup

1. Download from [python.org](https://www.python.org/downloads/)
2. Install **VS Code** (editor)
3. Run first program:

```python
print("Hello, World!")
```

✅ **Exercise:**
Write a program that prints your name and favorite hobby.

---

## **Day 2 – Variables & Data Types**

### 🔹 Variables

* Containers for storing data
* No need to declare type explicitly

```python
x = 10        # integer
name = "Ali"  # string
pi = 3.14     # float
is_active = True  # boolean
```

### 🔹 Checking Type

```python
print(type(x))        # <class 'int'>
print(type(pi))       # <class 'float'>
```

✅ **Exercise:**
Create variables for:

* Your age
* Your height
* Your name
* Whether you are a student (True/False)

---

## **Day 3 – Input & Output**

### 🔹 Printing (Output)

```python
name = "Sara"
age = 20
print("My name is", name, "and I am", age, "years old")
print(f"My name is {name} and I am {age} years old")  # f-string
```

### 🔹 Input (User Input)

```python
name = input("Enter your name: ")
print("Hello", name)
```

⚠️ Note: input() returns **string**

```python
age = int(input("Enter your age: "))  # convert to int
```

✅ **Exercise:**
Write a program that asks for two numbers and prints their sum.

---

## **Day 4 – Operators**

### 🔹 Arithmetic Operators

```python
x, y = 10, 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.333
print(x // y) # 3 (floor division)
print(x % y)  # 1 (remainder)
print(x ** y) # 1000 (power)
```

### 🔹 Comparison Operators

```python
print(x > y)   # True
print(x == y)  # False
```

### 🔹 Logical Operators

```python
a, b = True, False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

✅ **Mini-Project:**
Simple calculator that takes 2 numbers and prints: sum, difference, product, division.

---

## **Day 5 – Conditional Statements**

### 🔹 If / Elif / Else

```python
percent = 75

if percent >= 80:
    print("Grade A")
elif percent >= 60:
    print("Grade B")
elif percent >= 40:
    print("Grade C")
else:
    print("Grade D")
```

### 🔹 Example – Even/Odd

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

✅ **Mini-Project:**
Write a program to input marks and print:

* A if >= 80
* B if >= 60
* C if >= 40
* D otherwise

---

# 🎯 Week 1 Recap

* Printing and input
* Variables & data types
* Operators
* If/elif/else

👉 By end of Week 1, students can write **basic interactive programs** like calculators and grade checkers.

---

Would you like me to also prepare **Week 1 Assignments (5–6 practice questions)** so your students can try after class?
