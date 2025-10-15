# 🐍 **Python Tutorial – Lists (Arrays in Python)**

---

## 🔹 1. Introduction

A **list** is a collection of items stored in a single variable.
Lists are one of Python’s most powerful data structures — they can store:

- Numbers
- Strings
- Booleans
- Even a mix of all types

Think of a list as a **container that can hold multiple values**.

---

### ✅ Example:

```python
fruits = ["apple", "mango", "banana"]
print(fruits)
```

**Output:**

```
['apple', 'mango', 'banana']
```

---

## 🔹 2. Creating Lists

### 🧩 Examples:

```python
numbers = [10, 20, 30, 40]
names = ["Ali", "Sara", "John"]
mixed = [10, "apple", 3.5, True]
```

### Empty list:

```python
items = []
```

---

## 🔹 3. Accessing List Elements (Indexing)

Each element has an **index** (position).
Indexes start from **0**.

### ✅ Example:

```python
fruits = ["apple", "mango", "banana"]
print(fruits[0])  # apple
print(fruits[1])  # mango
print(fruits[2])  # banana
```

---

### 🔄 Negative Indexing:

You can also use **negative indexes** to start from the end.

```python
print(fruits[-1])  # banana
print(fruits[-2])  # mango
```

---

## 🔹 4. Changing Elements

Lists are **mutable** — meaning you can change their values.

### ✅ Example:

```python
fruits = ["apple", "mango", "banana"]
fruits[1] = "orange"
print(fruits)
```

**Output:**

```
['apple', 'orange', 'banana']
```

---

## 🔹 5. Adding Elements

| Method     | Description                          | Example                            |
| ---------- | ------------------------------------ | ---------------------------------- |
| `append()` | Adds element at the **end**          | `fruits.append("grape")`           |
| `insert()` | Adds element at a specific **index** | `fruits.insert(1, "kiwi")`         |
| `extend()` | Adds elements from another list      | `fruits.extend(["melon", "pear"])` |

### ✅ Example:

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.insert(1, "mango")
fruits.extend(["pear", "melon"])
print(fruits)
```

**Output:**

```
['apple', 'mango', 'banana', 'cherry', 'pear', 'melon']
```

---

## 🔹 6. Removing Elements

| Method     | Description                                  | Example                   |
| ---------- | -------------------------------------------- | ------------------------- |
| `remove()` | Removes first occurrence of a value          | `fruits.remove("banana")` |
| `pop()`    | Removes element at given index (or last one) | `fruits.pop()`            |
| `del`      | Deletes element or entire list               | `del fruits[1]`           |
| `clear()`  | Removes all items                            | `fruits.clear()`          |

### ✅ Example:

```python
fruits = ["apple", "mango", "banana", "cherry"]
fruits.remove("banana")
fruits.pop(1)
print(fruits)
```

**Output:**

```
['apple', 'cherry']
```

---

## 🔹 7. Looping Through a List

### ✅ Example:

```python
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
```

**Output:**

```
red
green
blue
```

---

## 🔹 8. List Length

Use `len()` to get the total number of elements.

```python
numbers = [10, 20, 30, 40]
print("Total items =", len(numbers))
```

**Output:**

```
Total items = 4
```

---

## 🔹 9. Slicing Lists

You can get a **sublist** by using slicing.

### ✅ Example:

```python
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[3:])    # [40, 50, 60]
print(numbers[-3:])   # [40, 50, 60]
```

---

## 🔹 10. Common List Methods

| Method      | Description            | Example                     |
| ----------- | ---------------------- | --------------------------- |
| `sort()`    | Sorts the list         | `numbers.sort()`            |
| `reverse()` | Reverses the list      | `numbers.reverse()`         |
| `count(x)`  | Counts occurrences     | `numbers.count(20)`         |
| `index(x)`  | Returns index of value | `numbers.index(30)`         |
| `copy()`    | Copies list            | `new_list = numbers.copy()` |

---

## 🔹 11. Example Programs

### 🧮 Program 1: Find Maximum Element

```python
numbers = [12, 45, 7, 34, 89, 23]
print("Maximum =", max(numbers))
```

---

### 🧮 Program 2: Find Sum of All Elements

```python
numbers = [5, 10, 15, 20]
print("Sum =", sum(numbers))
```

---

### 🧮 Program 3: Count Even and Odd Numbers

```python
numbers = [10, 21, 32, 43, 54]
even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)
```

---

## 🔹 12. Summary

✅ Lists are **ordered, mutable** collections.
✅ Can store **mixed data types**.
✅ Support **indexing, slicing, loops, and built-in functions**.
✅ Used extensively in **data processing** and **iterative programs**.

---

## 🧩 **Practice Assignment**

Write Python programs for the following:

1. Create a list of 5 numbers and find their **sum and average**.
2. Input 5 names, store them in a list, and display them in **reverse order**.
3. Create a list of numbers and display **only even numbers**.
4. Merge two lists and sort the final list in **ascending order**.
5. Remove duplicates from a list of items.
