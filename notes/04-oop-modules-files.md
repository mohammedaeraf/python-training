# 🐍 Python Week 4 Notes & Cheat Sheet (Days 16–20)

---

## **Day 16 – Introduction to OOP (Classes & Objects)**

### What is OOP?

* **Object-Oriented Programming** helps structure programs using **classes** (blueprints) and **objects** (instances).

### Syntax

```python
class Student:
    pass  # empty class

s1 = Student()  # create object
```

### Example – Student Class

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Ali", 85)
print(s1.name, s1.marks)
```

✅ Exercise: Create a `Car` class with `brand` and `color`.

---

## **Day 17 – Methods & Constructors**

### Constructor (`__init__`)

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name} scored {self.marks} marks")
```

### Using Methods

```python
s1 = Student("Sara", 90)
s1.display()
```

### Instance vs Class Variables

```python
class School:
    school_name = "ABC School"  # class variable

    def __init__(self, student):
        self.student = student  # instance variable
```

✅ Exercise: Add a method to `Car` class that prints its details.

---

## **Day 18 – Importing & Using Modules**

### Built-in Modules

```python
import math
print(math.sqrt(25))  # 5.0
print(math.pi)        # 3.141592653589793

import random
print(random.randint(1, 10))  # random number 1–10
```

### From Module Import

```python
from math import ceil, floor
print(ceil(4.2))   # 5
print(floor(4.8))  # 4
```

✅ Exercise: Use `random` to simulate dice roll (1–6).

---

## **Day 19 – File Handling**

### Writing to a File

```python
f = open("example.txt", "w")
f.write("Hello Python!\n")
f.write("Week 4 learning")
f.close()
```

### Reading from a File

```python
f = open("example.txt", "r")
content = f.read()
print(content)
f.close()
```

### Using `with` (Best Practice)

```python
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
```

✅ Exercise: Create a file, write your name and age, then read and print it.

---

## **Day 20 – Mini Project & Wrap-up**

### Mini Project Ideas

1. **Student Marks Manager**

   * Store student info (name, marks) in a class
   * Add methods to add, display, or update marks

2. **Simple Calculator** using functions and file logging

   * Save calculations to a file

### Recap & Next Steps

* OOP: Classes, Objects, Constructors, Methods
* Modules: math, random, others
* File Handling: read/write files
* Next: Libraries like **NumPy, Pandas** or Web Frameworks

---

# 🎯 Week 4 Cheat Sheet

| Concept           | Syntax / Example                                  |
| ----------------- | ------------------------------------------------- |
| Class             | `class ClassName:`                                |
| Constructor       | `def __init__(self, params):`                     |
| Object            | `obj = ClassName(args)`                           |
| Method            | `def method_name(self):`                          |
| Class vs Instance | `class_var = value` / `self.instance_var = value` |
| Import Module     | `import math` / `from math import sqrt`           |
| Random Number     | `random.randint(1,6)`                             |
| File Write        | `open("file.txt", "w")`                           |
| File Read         | `open("file.txt", "r")`                           |
| With Statement    | `with open(...) as f:`                            |