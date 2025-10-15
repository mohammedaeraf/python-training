Perfect 👍 — here’s a **complete, classroom-ready tutorial** on **Conditional Statements in Python** — designed to follow your earlier “Variables & Input/Output” session.

---

# 🐍 **Python Tutorial – Conditional Statements (`if`, `elif`, `else`)**

---

## 🔹 1. Introduction

In programming, we often need to **make decisions** — perform different actions depending on conditions.

Example:
If a student’s percentage is above 80 → show grade A,
otherwise → show grade B or C.

That’s where **conditional statements** come in.

---

## 🔹 2. The `if` Statement

Used to execute a block of code **only if** a condition is `True`.

### 🧩 Syntax:

```python
if condition:
    statement1
    statement2
```

> Indentation (spaces) is **very important** in Python!
> Typically, we use **4 spaces** or **1 tab** for each block.

### ✅ Example:

```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```

**Output:**

```
You are eligible to vote.
```

If the condition is false, nothing runs.

---

## 🔹 3. The `if–else` Statement

Use `else` to run an alternative block if the condition is **False**.

### ✅ Example:

```python
age = 16
if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")
```

**Output:**

```
Not eligible to vote.
```

---

## 🔹 4. The `if–elif–else` Statement

When there are **multiple conditions**, use `elif` (short for *else if*).

### ✅ Example:

```python
marks = 72

if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: D")
```

**Output:**

```
Grade: B
```

---

## 🔹 5. Nested `if` Statements

You can write one `if` inside another. This is called **nesting**.

### ✅ Example:

```python
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("You can vote in national elections.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are underage.")
```

**Output:**

```
You can vote in national elections.
```

---

## 🔹 6. Using Logical Operators

You can combine multiple conditions using:

* `and`
* `or`
* `not`

### ✅ Example:

```python
age = 22
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")
```

**Output:**

```
You can drive.
```

---

## 🔹 7. Comparison Operators (Quick Recap)

| Operator | Meaning               | Example  | Result |
| -------- | --------------------- | -------- | ------ |
| `==`     | Equal to              | `5 == 5` | True   |
| `!=`     | Not equal to          | `5 != 3` | True   |
| `>`      | Greater than          | `10 > 3` | True   |
| `<`      | Less than             | `4 < 2`  | False  |
| `>=`     | Greater than or equal | `6 >= 6` | True   |
| `<=`     | Less than or equal    | `8 <= 9` | True   |

---

## 🔹 8. Example Programs

### 🧮 Program 1: Check Even or Odd

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

---

### 💯 Program 2: Find the Largest of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")
```

---

### 📊 Program 3: Student Grade (Using if–elif–else)

```python
percent = float(input("Enter percentage: "))

if percent >= 80:
    grade = "A"
elif percent >= 60:
    grade = "B"
elif percent >= 40:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)
```

---

### 🧠 Program 4: Check Leap Year

```python
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
```

---

## 🔹 9. Summary

✅ You learned:

* `if`, `elif`, and `else` syntax
* Nested conditions
* Logical and comparison operators
* Real-life examples using decisions

---

## 🧩 **Practice Assignment**

Write Python programs for the following:

1. **Positive or Negative** – Take a number and print whether it’s positive, negative, or zero.
2. **Age Category** – Input age; print “Child”, “Teenager”, “Adult”, or “Senior Citizen”.
3. **Pass/Fail** – Input marks; print “Pass” if ≥ 40, otherwise “Fail”.
4. **Smallest of Three Numbers** – Input 3 numbers; find the smallest one.
5. **Character Check** – Input a character; check if it’s a vowel or consonant.
