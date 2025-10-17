# 🧠 Python Strings – Complete Tutorial

---

## 📘 1. Introduction to Strings

A **string** in Python is a sequence of characters enclosed in either **single quotes** (`'`) or **double quotes** (`"`).

```python
name = "Ayesha"
city = 'Mangalore'
```

You can also create **multi-line strings** using triple quotes (`'''` or `"""`).

```python
message = """Welcome to Python Programming!
This is a multi-line string."""
print(message)
```

---

## 🧩 2. String Indexing

Each character in a string has a position (called **index**), starting from **0**.

| Character | A | y | e | s | h | a |
| --------- | - | - | - | - | - | - |
| Index     | 0 | 1 | 2 | 3 | 4 | 5 |

Example:

```python
word = "Python"
print(word[0])   # P
print(word[3])   # h
print(word[-1])  # n (last character)
```

📝 **Note:**

* Positive indexes start from **0** (left to right).
* Negative indexes start from **-1** (right to left).

---

## ✂️ 3. String Slicing

Slicing allows you to extract a **portion** of a string using the syntax:

```python
string[start:end:step]
```

Example:

```python
word = "Programming"
print(word[0:6])    # Progra (characters from index 0 to 5)
print(word[:6])     # same as above (start index is 0)
print(word[3:])     # gramming (from index 3 to end)
print(word[::2])    # Pormig (every 2nd character)
print(word[::-1])   # gnimmargorP (reversed string)
```

---

## 🧰 4. Common String Methods

Python provides many **built-in string methods** for common operations.

| Method          | Description                       | Example                                   |
| --------------- | --------------------------------- | ----------------------------------------- |
| `upper()`       | Converts to uppercase             | `"python".upper()` → `"PYTHON"`           |
| `lower()`       | Converts to lowercase             | `"PyThOn".lower()` → `"python"`           |
| `title()`       | Converts to title case            | `"hello world".title()` → `"Hello World"` |
| `strip()`       | Removes spaces from both ends     | `"  hi  ".strip()` → `"hi"`               |
| `replace(a, b)` | Replaces substring `a` with `b`   | `"apple".replace("a", "A")` → `"Apple"`   |
| `split()`       | Splits string into list of words  | `"a,b,c".split(",")` → `['a', 'b', 'c']`  |
| `join()`        | Joins list elements into string   | `"-".join(['a','b','c'])` → `"a-b-c"`     |
| `find()`        | Returns index of first occurrence | `"hello".find("e")` → `1`                 |
| `count()`       | Counts number of occurrences      | `"banana".count("a")` → `3`               |

Example:

```python
sentence = "   Python Programming is Fun!   "
print(sentence.strip())          # Removes spaces
print(sentence.upper())          # Converts to uppercase
print(sentence.lower())          # Converts to lowercase
print(sentence.replace("Fun", "Powerful"))
print(sentence.split())          # Splits into words
```

---

## 🔍 5. Checking String Content

These methods return **True** or **False** based on content.

| Method         | Example                      | Result |
| -------------- | ---------------------------- | ------ |
| `isalpha()`    | `"abc".isalpha()`            | ✅ True |
| `isdigit()`    | `"123".isdigit()`            | ✅ True |
| `isalnum()`    | `"abc123".isalnum()`         | ✅ True |
| `isspace()`    | `"   ".isspace()`            | ✅ True |
| `startswith()` | `"python".startswith("py")`  | ✅ True |
| `endswith()`   | `"hello.py".endswith(".py")` | ✅ True |

Example:

```python
text = "Python3"
if text.isalpha():
    print("Contains only letters")
elif text.isalnum():
    print("Contains letters and numbers")
```

---

## 🧮 6. Mini Project – Word Counter

Let’s build a small program that counts the **number of words** and **each word’s frequency** in a sentence.

### ✅ Program: Word Counter

```python
# Word Counter Program

sentence = input("Enter a sentence: ")

# Step 1: Clean and split sentence
words = sentence.lower().split()

# Step 2: Count total words
print("Total words:", len(words))

# Step 3: Count frequency of each word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 4: Display word counts
print("\nWord Frequency:")
for word, count in word_count.items():
    print(word, ":", count)
```

### 🧠 Sample Output:

```
Enter a sentence: Python is fun and Python is powerful
Total words: 7

Word Frequency:
python : 2
is : 2
fun : 1
and : 1
powerful : 1
```

---

## 🏁 Summary

| Concept                  | Description                                              |
| ------------------------ | -------------------------------------------------------- |
| **Indexing**             | Access individual characters                             |
| **Slicing**              | Extract portions of strings                              |
| **String Methods**       | Modify and process text                                  |
| **Word Counter Project** | Practice using loops, conditionals, and string functions |
