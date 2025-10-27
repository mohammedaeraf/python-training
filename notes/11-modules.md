# 📦 **Python Tutorial – Modules and Packages**

---

## 🟢 **1. What is a Module?**

A **module** in Python is simply a **file that contains Python code** — variables, functions, or classes — which you can **import** into another Python file.

👉 Example:
You already use modules like `math`, `random`, or `datetime` — they are built-in Python modules.

---

## 🟢 **2. Using Built-in Modules**

```python
import math

print(math.sqrt(25))      # 5.0
print(math.pi)            # 3.141592653589793
print(math.pow(2, 3))     # 8.0
```

### Import Specific Items:

```python
from math import sqrt, pi

print(sqrt(16))
print(pi)
```

### Rename a Module:

```python
import math as m
print(m.factorial(5))
```

---

## 🟢 **3. Commonly Used Built-in Modules**

| Module     | Purpose                            |
| ---------- | ---------------------------------- |
| `math`     | Mathematical functions             |
| `random`   | Generate random numbers            |
| `datetime` | Work with date and time            |
| `os`       | Interact with operating system     |
| `sys`      | Access system-specific information |
| `json`     | Work with JSON data                |

Example:

```python
import random

print(random.randint(1, 10))  # random number between 1–10
```

---

## 🟢 **4. Creating Your Own Module**

Let’s create a file named **`myutils.py`**:

```python
# myutils.py
def greet(name):
    print("Hello", name)

def add(x, y):
    return x + y
```

Now, create another file **`main.py`**:

```python
# main.py
import myutils

myutils.greet("Ali")
print("Sum =", myutils.add(10, 20))
```

✅ Output:

```
Hello Ali
Sum = 30
```

---

## 🧠 **Assignment Ideas**

1. Create a module with temperature conversion functions (Celsius ↔ Fahrenheit).
2. Create your own `geometry` module with area/perimeter functions for square, rectangle, and circle.

