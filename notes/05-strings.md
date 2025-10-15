✅ **Tutorial 5: Working with Strings in Python**

---

### 🎯 **Objective:**

To understand how to work with **strings** — including indexing, slicing, and commonly used string methods — and build a small **Word Counter mini-project**.

---

## 🧩 **1. What is a String?**

A **string** is a sequence of characters enclosed in single (`'`) or double (`"`) quotes.

```python
name = "Python"
greeting = 'Hello, World!'
```

---

## 🪜 **2. Indexing in Strings**

Python treats strings as **arrays of characters**, where each character has an index.

| P   | y   | t   | h   | o   | n   |
| --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   |

You can access any character using its index.

### 🧮 **Example:**

```python
word = "Python"
print(word[0])  # First character
print(word[3])  # Fourth character
```

**Output:**

```
P
h
```

---

## ✂️ **3. Slicing Strings**

Slicing allows you to extract a **portion** of a string using:

```python
string[start:end]
```

> Note: `end` index is **exclusive**.

### 🧮 **Examples:**

```python
word = "Programming"
print(word[0:6])   # Output: Progra
print(word[3:])    # Output: gramming
print(word[:5])    # Output: Progr
print(word[-3:])   # Output: ing
```

---

## 🧮 **4. String Methods**

Python provides several **built-in string methods** to manipulate text easily.

| Method      | Description                  | Example                                          |
| ----------- | ---------------------------- | ------------------------------------------------ |
| `upper()`   | Converts string to uppercase | `"hello".upper()` → `"HELLO"`                    |
| `lower()`   | Converts string to lowercase | `"WORLD".lower()` → `"world"`                    |
| `strip()`   | Removes extra spaces         | `" hello ".strip()` → `"hello"`                  |
| `replace()` | Replaces substring           | `"blue sky".replace("blue","red")` → `"red sky"` |
| `split()`   | Splits string into list      | `"a,b,c".split(",")` → `['a','b','c']`           |
| `count()`   | Counts occurrences           | `"banana".count("a")` → `3`                      |
| `find()`    | Finds index of substring     | `"apple".find("p")` → `1`                        |

---

### 🧮 **Examples:**

```python
message = "   Python Programming is Fun!   "
print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("Fun", "Awesome"))
print(message.split())
```

**Output:**

```
   PYTHON PROGRAMMING IS FUN!
   python programming is fun!
Python Programming is Fun!
Python Programming is Awesome!
['Python', 'Programming', 'is', 'Fun!']
```

---

## 🧠 **5. Combining Indexing, Slicing & Methods**

### Example:

```python
text = "Learning Python"
print(text[0:8].upper())  # Take 'Learning' and convert to uppercase
```

**Output:**

```
LEARNING
```

---

## 💻 **Mini Project: Word Counter**

Let’s build a small program to **count the number of words** in a given sentence.

### 🧮 **Code:**

```python
# Word Counter Program

sentence = input("Enter a sentence: ")

# Remove extra spaces and split into words
words = sentence.strip().split()

# Count words
word_count = len(words)

print(f"Total words: {word_count}")
```

### 🧪 **Example Output:**

```
Enter a sentence: Python is easy to learn
Total words: 5
```

---

## 🧠 **6. Practice Exercises**

1. Print the first and last character of a given string.
2. Reverse a string using slicing.
3. Count how many vowels are in a given string.
4. Replace all spaces in a sentence with hyphens (`-`).
5. Write a program that checks if a string is a **palindrome** (same forwards and backwards).
