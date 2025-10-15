# 🐍 Python Week 3 Notes & Cheat Sheet (Days 11–15)

---

## **Day 11 – Functions (Basics)**

### Syntax

```python
def function_name(parameters):
    # code block
    return value
```

### Example – Factorial

```python
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))  # 120
```

### Calling a Function

```python
print(factorial(7))
```

✅ Exercise: Write a function that adds two numbers and returns the result.

---

## **Day 12 – Functions (Advanced)**

### Default Arguments

```python
def greet(name="Guest"):
    print(f"Hello {name}!")

greet("Ali")
greet()  # uses default
```

### Lambda Functions

```python
square = lambda x: x*x
print(square(5))  # 25
```

✅ Exercise: Write a lambda function to multiply two numbers.

---

## **Day 13 – Tuples**

### Create Tuple

```python
t = (1, 2, 3)
print(t[0])    # 1
print(len(t))  # 3
```

### Immutable

```python
# t[0] = 10   # ❌ Error
```

### Unpacking

```python
a, b, c = t
print(a, b, c)
```

✅ Exercise: Create a tuple with 4 items and unpack them into variables.

---

## **Day 14 – Sets**

### Create Set

```python
s = {1, 2, 3, 2, 1}
print(s)  # {1, 2, 3}  # unique elements only
```

### Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1,2,3,4,5}
print(a.intersection(b)) # {3}
print(a - b)             # {1,2}
```

✅ Exercise: Create two sets and print their union and intersection.

---

## **Day 15 – Dictionaries**

### Create Dictionary

```python
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

print(student["name"])  # Ali
```

### Add / Update / Delete

```python
student["grade"] = "A"   # add
student["marks"] = 90    # update
del student["age"]       # delete
```

### Iteration

```python
for key, value in student.items():
    print(key, ":", value)
```

✅ Exercise: Create a dictionary for a book (title, author, pages) and print details.

---

# 🎯 Week 3 Quick Reference Cheat Sheet

| Concept           | Syntax / Example                 |
| ----------------- | -------------------------------- |
| Function          | `def func(params): return value` |
| Call Function     | `func(arguments)`                |
| Default Argument  | `def greet(name="Guest"):`       |
| Lambda Function   | `lambda x: x*x`                  |
| Tuple             | `(1,2,3)`                        |
| Tuple Unpacking   | `a,b,c = t`                      |
| Set               | `{1,2,3}`                        |
| Set Operations    | `union()`, `intersection()`, `-` |
| Dictionary        | `{"key":"value"}`                |
| Dictionary Access | `dict[key]`                      |
| Dictionary Iter   | `for k,v in dict.items():`       |

