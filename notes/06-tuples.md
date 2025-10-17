## 🐍 **Python Tutorial: Working with Tuples**

### 🎯 **Learning Objectives**

By the end of this lesson, you will be able to:

* Understand what tuples are and how they differ from lists
* Create and access tuples
* Use tuple operations and methods
* Understand tuple immutability
* Use tuples in practical examples

---

### 🧩 **1. What is a Tuple?**

A **tuple** is an ordered and immutable (unchangeable) collection of elements.
Tuples are written using **parentheses `()`** instead of square brackets `[]`.

```python
numbers = (10, 20, 30, 40)
fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.5, True)
```

---

### 🧠 **2. Characteristics of Tuples**

* **Ordered:** The elements have a defined order.
* **Immutable:** Once created, tuple elements cannot be changed.
* **Allows duplicates:** Like lists, tuples can have duplicate values.
* **Can contain mixed data types.**

---

### 🧮 **3. Creating Tuples**

#### Example 1: Empty and Single-element Tuples

```python
empty_tuple = ()
single_tuple = (5,)  # Note the comma!
```

> ⚠️ Without a comma, Python treats `(5)` as an integer, not a tuple.

---

### 🔍 **4. Accessing Tuple Elements**

You can access tuple elements using **indexing** or **slicing**.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[0])     # 10
print(numbers[-1])    # 50
print(numbers[1:4])   # (20, 30, 40)
```

---

### 🚫 **5. Tuples are Immutable**

You cannot modify tuple elements once created.

```python
colors = ("red", "green", "blue")
# colors[1] = "yellow"  # ❌ This will cause an error
```

If you need to “modify” a tuple, you can convert it into a list and then back into a tuple.

```python
colors = ("red", "green", "blue")
temp = list(colors)
temp[1] = "yellow"
colors = tuple(temp)
print(colors)  # ('red', 'yellow', 'blue')
```

---

### 🧰 **6. Tuple Methods**

Tuples have very few methods:

```python
t = (1, 2, 2, 3, 4, 2)
print(t.count(2))  # 3
print(t.index(3))  # 3 appears at index 3
```

---

### ➕ **7. Tuple Operations**

You can combine and repeat tuples using operators.

```python
t1 = (1, 2, 3)
t2 = (4, 5)

# Concatenation
print(t1 + t2)  # (1, 2, 3, 4, 5)

# Repetition
print(t1 * 2)   # (1, 2, 3, 1, 2, 3)
```

---

### 🧮 **8. Tuple Unpacking**

You can assign tuple elements directly to variables.

```python
person = ("Ali", 25, "India")
name, age, country = person
print(name)
print(age)
print(country)
```

---

### 🧑‍💻 **Mini Project: Student Marks Analyzer**

#### Problem:

Write a Python program that:

1. Takes marks of 3 subjects as a tuple.
2. Displays the total and average marks.
3. Checks if the student passed (average ≥ 40).

#### Example Output:

```
Enter marks for 3 subjects (comma separated): 75, 82, 68
Total Marks = 225
Average = 75.0
Result: Pass
```

---

### 🧠 **Assignment Ideas**

1. Create a tuple with 5 numbers and print only the even numbers.
2. Create a tuple with 10 names and print names starting with the letter “A”.
3. Write a program to find the maximum and minimum values in a tuple.
4. Write a program to count how many times a particular element appears in a tuple.
5. Write a program to combine two tuples and display the length of the new tuple.