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

## 🟢 **5. The `__name__ == "__main__"` Trick**

When a file is run directly, `__name__` becomes `"__main__"`.
When it’s imported, `__name__` becomes the module name.

```python
# myutils.py
def greet():
    print("Hello from myutils")

if __name__ == "__main__":
    print("Running directly")
else:
    print("Imported as module")
```

---

## 🟢 **6. What is a Package?**

A **package** is a **folder that contains multiple modules** and a special file `__init__.py`.

Example structure:

```
my_package/
    __init__.py
    math_utils.py
    string_utils.py
```

Now you can import like this:

```python
from my_package.math_utils import add
```

---

## 🧩 **Mini Project – Custom Utility Package**

1. Create a folder named `my_tools`.
2. Inside it, create two modules:

   * `math_ops.py` → contains functions: `add`, `subtract`, `multiply`
   * `string_ops.py` → contains `reverse` and `to_upper`
3. Write a `main.py` that imports and uses functions from both modules.

---

## 🧠 **Assignment Ideas**

1. Create a module with temperature conversion functions (Celsius ↔ Fahrenheit).
2. Create a random password generator using the `random` module.
3. Write a program using the `datetime` module to display current date and time.
4. Create your own `geometry` module with area/perimeter functions for square, rectangle, and circle.
5. Build a simple calculator package containing two modules: `basic_ops` and `advanced_ops`.
