# 🧠 **Python Tuples and Sets**

---

## 🎯 **Learning Objectives**

By the end of this tutorial, students will be able to:

* Understand what **Tuples** and **Sets** are.
* Know how they differ from **Lists**.
* Perform basic operations such as indexing, slicing, and iteration.
* Use common **methods and functions** with tuples and sets.

---

## 🧩 **1️⃣ Tuples in Python**

### 📘 What is a Tuple?

A **tuple** is similar to a list but **immutable** — once created, its values cannot be changed.

Tuples are written inside **parentheses ( )** instead of square brackets `[ ]`.

```python
fruits = ("apple", "mango", "orange")
print(fruits)
print(type(fruits))
```

### ✅ **Accessing Elements**

Tuples support indexing and slicing like lists.

```python
colors = ("red", "green", "blue", "yellow")

print(colors[0])     # red
print(colors[-1])    # yellow
print(colors[1:3])   # ('green', 'blue')
```

---

### ⚙️ **Tuple Operations**

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

print(t1 + t2)   # Concatenation → (1, 2, 3, 4, 5, 6)
print(t1 * 2)    # Repetition → (1, 2, 3, 1, 2, 3)
print(2 in t1)   # Membership → True
```

---

### 🚫 **Tuples are Immutable**

```python
numbers = (1, 2, 3)
# numbers[0] = 10   ❌ This will cause an error
print(numbers)
```

---

### 🧰 **Tuple Methods**

| Method         | Description                       | Example                    |
| -------------- | --------------------------------- | -------------------------- |
| `count(value)` | Returns number of occurrences     | `(1,2,2,3).count(2)` → 2   |
| `index(value)` | Returns index of first occurrence | `(10,20,30).index(20)` → 1 |

---

### 🧮 **Tuple Example Program**

```python
marks = (87, 92, 76, 81, 92)

print("Marks:", marks)
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Count of 92:", marks.count(92))
print("Index of 76:", marks.index(76))
```

---

## 🔹 **2️⃣ Sets in Python**

### 📘 What is a Set?

A **set** is an unordered collection of **unique elements**.
Sets are written inside **curly braces `{ }`**.

```python
fruits = {"apple", "banana", "mango", "apple"}
print(fruits)  # Duplicates are removed automatically
print(type(fruits))
```

---

### ⚙️ **Basic Set Operations**

```python
numbers = {10, 20, 30, 40}

numbers.add(50)
print(numbers)

numbers.remove(20)
print(numbers)

print(30 in numbers)  # Membership check
```

---

### 🧮 **Set Operations (Union, Intersection, Difference)**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)           # {1, 2, 3, 4, 5, 6}
print("Intersection:", a & b)    # {3, 4}
print("Difference:", a - b)      # {1, 2}
print("Symmetric Difference:", a ^ b)  # {1, 2, 5, 6}
```

---

### 🧰 **Common Set Methods**

| Method      | Description                     | Example          |
| ----------- | ------------------------------- | ---------------- |
| `add()`     | Adds an element                 | `s.add(10)`      |
| `remove()`  | Removes an element              | `s.remove(20)`   |
| `discard()` | Removes without error if absent | `s.discard(100)` |
| `clear()`   | Empties the set                 | `s.clear()`      |
| `copy()`    | Returns a shallow copy          | `s.copy()`       |

---

### 🧠 **Example: Working with Student Subjects**

```python
science = {"Alice", "Bob", "Charlie"}
maths = {"Bob", "David", "Charlie", "Eve"}

print("All students:", science | maths)
print("Students in both:", science & maths)
print("Only in Science:", science - maths)
```

---

## 💡 **3️⃣ Key Differences: Tuple vs Set vs List**

| Feature            | List            | Tuple      | Set               |
| ------------------ | --------------- | ---------- | ----------------- |
| Brackets Used      | `[ ]`           | `( )`      | `{ }`             |
| Mutable            | ✅ Yes           | ❌ No       | ✅ Yes             |
| Allows Duplicates  | ✅ Yes           | ✅ Yes      | ❌ No              |
| Ordered            | ✅ Yes           | ✅ Yes      | ❌ No              |
| Indexing Supported | ✅ Yes           | ✅ Yes      | ❌ No              |
| Use Case           | General purpose | Fixed data | Unique collection |

---

## 🧮 **4️⃣ Practice Programs**

1. Create a tuple of 5 colors and print them in reverse order.
2. Find common elements between two sets `{10, 20, 30}` and `{20, 30, 40}`.
3. Given a list with duplicates, convert it into a **set** to remove duplicates.
4. Create two sets of friends and find:

   * Those common to both
   * Those unique to each group.
