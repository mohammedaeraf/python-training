# 🐍 Python Week 1 Cheat Sheet

---

## **1️⃣ Printing & Input**

```python
# Print text
print("Hello, World!")

# Print variables
name = "Ali"
age = 20
print("My name is", name, "and I am", age)
print(f"My name is {name} and I am {age}")  # f-string

# Input from user
name = input("Enter your name: ")    # string
age = int(input("Enter your age: ")) # convert to integer
```

---

## **2️⃣ Variables & Data Types**

```python
# Numbers
x = 10          # int
pi = 3.14       # float

# Strings
name = "Sara"

# Boolean
is_active = True

# Check type
print(type(x))
print(type(name))
```

---

## **3️⃣ Operators**

### Arithmetic

```python
a, b = 10, 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333
print(a // b) # 3 (floor division)
print(a % b)  # 1 (remainder)
print(a ** b) # 1000 (power)
```

### Comparison

```python
print(a > b)   # True
print(a == b)  # False
```

### Logical

```python
x, y = True, False
print(x and y) # False
print(x or y)  # True
print(not x)   # False
```

---

## **4️⃣ Conditional Statements**

```python
percent = 75

if percent >= 80:
    grade = "A"
elif percent >= 60:
    grade = "B"
elif percent >= 40:
    grade = "C"
else:
    grade = "D"

print(f"Grade: {grade}")

# Example: Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## **5️⃣ Loops (Introduction)**

### For Loop

```python
# Multiplication table for 5
n = 5
for i in range(1, 11):  # 1 to 10
    print(f"{n} x {i} = {n*i}")
```

### While Loop

```python
count = 5
while count > 0:
    print(count)
    count -= 1
```

---

## **6️⃣ Mini Exercises**

1. Print your name and favorite hobby.
2. Simple calculator (sum, difference, product, division).
3. Check if a number is even or odd.
4. Grade calculator for marks.
5. Find the largest of 3 numbers.

---

### ✅ Quick Tips

* Python uses **indentation** instead of `{}` for blocks.
* Use **f-strings** for clean output: `f"Hello {name}"`
* Input is **always string**, convert to int or float when needed.
* Practice with **small programs** daily.
