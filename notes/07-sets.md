## 🐍 **Python Tutorial: Working with Sets**

### 🎯 **Learning Objectives**

By the end of this lesson, you will be able to:

* Understand what sets are and how they differ from lists and tuples
* Create and access sets
* Perform set operations (union, intersection, difference, etc.)
* Use set methods effectively
* Solve a real-world problem using sets

---

### 🧩 **1. What is a Set?**

A **set** is an **unordered**, **mutable**, and **unindexed** collection of unique elements.
Sets are useful when you need to store non-duplicate items.

```python
fruits = {"apple", "banana", "cherry"}
numbers = {10, 20, 30, 40}
```

> ⚠️ Duplicate values are automatically removed.

```python
data = {10, 20, 10, 30, 20}
print(data)  # Output: {10, 20, 30}
```

---

### 🧠 **2. Characteristics of Sets**

* **Unordered:** No defined order (cannot use index numbers).
* **No duplicates:** Each element must be unique.
* **Mutable:** You can add or remove elements.
* **Can hold mixed data types.**

---

### 🧮 **3. Creating Sets**

```python
empty_set = set()       # ✅ Correct way to create an empty set
numbers = {1, 2, 3, 4}  # Set with values
```

> ⚠️ `{}` creates an empty dictionary, not a set.

---

### 🔍 **4. Accessing Set Elements**

Since sets are **unordered**, you can’t access elements using an index.
Instead, you can use a **loop** to traverse the elements.

```python
colors = {"red", "green", "blue"}
for c in colors:
    print(c)
```

---

### 🧰 **5. Adding and Removing Elements**

```python
fruits = {"apple", "banana"}

# Add a single element
fruits.add("cherry")

# Add multiple elements
fruits.update(["mango", "orange"])

# Remove elements
fruits.remove("banana")    # Raises error if not found
fruits.discard("kiwi")     # No error even if not found

print(fruits)
```

---

### ➕ **6. Set Operations**

Sets support **mathematical operations** such as union, intersection, difference, and symmetric difference.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)            # {1, 2, 3, 4, 5, 6}
print("Intersection:", A & B)     # {3, 4}
print("Difference:", A - B)       # {1, 2}
print("Symmetric Difference:", A ^ B)  # {1, 2, 5, 6}
```

---

### 🧮 **7. Other Useful Methods**

```python
numbers = {10, 20, 30}

print(len(numbers))        # 3
print(20 in numbers)       # True
numbers.clear()            # Removes all elements
```

---

### 🔄 **8. Converting Between List, Tuple, and Set**

```python
list_data = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_data)
print(unique_set)  # {1, 2, 3, 4, 5}

# Convert back to list
unique_list = list(unique_set)
print(unique_list)
```

---

### 🧑‍💻 **Mini Project: Unique Words Counter**

#### Problem:

Write a program that:

1. Takes a sentence from the user
2. Splits it into words
3. Counts how many **unique words** it contains

#### Example:

```
Enter a sentence: Python is easy and Python is fun
Unique words: {'Python', 'is', 'easy', 'and', 'fun'}
Count: 5
```

---

### 🧠 **Assignment Ideas**

1. Create two sets of favorite fruits for two friends and find:

   * Common fruits
   * Fruits only one friend likes
   * All unique fruits combined

2. Write a program to remove duplicate numbers from a list using a set.

3. Given two sets of numbers A and B, display:

   * A union B
   * A intersection B
   * A difference B

4. Create a set of vowels and check if a given character is a vowel or not.

5. Write a program that takes 5 colors from the user and displays them as a set (no duplicates allowed).

---

## 🧠 **Solutions: Python Set Assignments**

---

### **1. Favorite Fruits of Two Friends**

```python
# Sets of favorite fruits
friend1 = {"apple", "banana", "cherry", "mango"}
friend2 = {"banana", "kiwi", "mango", "orange"}

# Common fruits
common = friend1 & friend2

# Fruits only one friend likes
unique = friend1 ^ friend2

# All fruits combined
all_fruits = friend1 | friend2

print("Common Fruits:", common)
print("Unique Fruits:", unique)
print("All Fruits:", all_fruits)
```

---

### **2. Remove Duplicate Numbers from a List**

```python
numbers = [10, 20, 10, 30, 20, 40, 40, 50]

# Using a set to remove duplicates
unique_numbers = list(set(numbers))

print("Original List:", numbers)
print("Unique List:", unique_numbers)
```

---

### **3. Set Operations (Union, Intersection, Difference)**

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A - B):", A - B)
```

---

### **4. Check if a Character is a Vowel**

```python
vowels = {"a", "e", "i", "o", "u"}

ch = input("Enter a character: ").lower()

if ch in vowels:
    print(ch, "is a vowel.")
else:
    print(ch, "is not a vowel.")
```

---

### **5. Accept 5 Colors and Display Unique Set**

```python
colors = set()

for i in range(5):
    color = input("Enter a color: ")
    colors.add(color)

print("Unique Colors:", colors)
```