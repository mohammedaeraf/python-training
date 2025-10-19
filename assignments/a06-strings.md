# 🧩 **Assignment 06 – Strings in Python**

### ⏱ Duration: 20–25 minutes

### 🎯 Objective:

To strengthen your understanding of **indexing, slicing, and string methods** in Python.

---

## 🧠 **1️⃣ Accessing Characters**

Write a Python program that:

* Takes a string input from the user.
* Displays:

  1. The first and last character
  2. The third character from the end
  3. Every second character in the string

**Example:**

```
Enter a word: Programming
First: P
Last: g
Third from end: n
Every second character: Pormig
```

---

## 🧩 **2️⃣ String Slicing**

Write a program to:

* Take a word as input.
* Print the first half and the second half of the word separately.

**Hint:** Use slicing (`len(word)//2`) to find the midpoint.

**Example:**

```
Enter a word: Python
First half: Pyt
Second half: hon
```

---

## 🧰 **3️⃣ String Methods**

Take a sentence as input and perform the following:

* Convert it to uppercase and display it
* Count how many times the word `"the"` appears (use `.count()`)
* Replace `"Python"` with `"AI"`

**Example:**

```
Enter a sentence: Python is the best. The world loves Python!
UPPERCASE: PYTHON IS THE BEST. THE WORLD LOVES PYTHON!
Count of 'the': 2
Replaced: AI is the best. The world loves AI!
```

---

## 🧮 **4️⃣ String Analysis**

Write a program that takes a string and:

* Checks if it’s all alphabets (`isalpha()`)
* Checks if it’s all digits (`isdigit()`)
* Checks if it’s alphanumeric (`isalnum()`)

**Example:**

```
Enter a value: Python3
Contains only alphabets? False
Contains only digits? False
Contains letters and numbers? True
```

---

## 💬 **5️⃣ Mini Project: Word Counter (Enhanced)**

Extend the earlier **Word Counter** project:

* Input a sentence
* Remove punctuation (optional challenge: use `.replace()` or `strip()`)
* Count and display how many times each word appears
* Show the **most frequent word** at the end

**Example:**

```
Enter a sentence: Python is easy, and Python is fun!
Word counts:
python : 2
is : 2
easy : 1
and : 1
fun : 1

Most frequent word: python
```

---

## 🏁 **Submission Tips**

✅ Test each program with multiple inputs
✅ Use clear variable names and comments
✅ Display output in a readable format
