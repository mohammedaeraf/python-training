# 📂 **Python Tutorial – File Handling**

---

## 🟢 **1. Introduction**

File handling allows your Python programs to **read**, **write**, and **modify** files (like `.txt`, `.csv`, etc.).
You can store data permanently and process it later.

The key built-in function for file handling is **`open()`**.

---

## 🟢 **2. Opening a File**

```python
file = open("example.txt", "r")
```

### **File Modes**

| Mode   | Description                                     |
| ------ | ----------------------------------------------- |
| `"r"`  | Read (default) – file must exist                |
| `"w"`  | Write – overwrites file if it exists            |
| `"a"`  | Append – adds data to the end of file           |
| `"x"`  | Create – creates a new file, error if it exists |
| `"r+"` | Read and write                                  |

---

## 🟢 **3. Reading from a File**

Let’s assume `data.txt` contains:

```
Hello Students
Welcome to Python Course
```

### **Read Entire File**

```python
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()
```

### **Read Line by Line**

```python
f = open("data.txt", "r")
for line in f:
    print(line.strip())
f.close()
```

### **Read into a List**

```python
f = open("data.txt", "r")
lines = f.readlines()
print(lines)
f.close()
```

---

## 🟢 **4. Writing to a File**

```python
f = open("notes.txt", "w")
f.write("Python File Handling Example\n")
f.write("This will overwrite existing content.")
f.close()
```

✅ Creates `notes.txt` and writes into it.

---

## 🟢 **5. Appending to a File**

```python
f = open("notes.txt", "a")
f.write("\nThis line is appended.")
f.close()
```

✅ Adds new text to the end without deleting previous content.

---

## 🟢 **6. Reading and Writing Together**

```python
f = open("sample.txt", "r+")
print("Before:", f.read())

f.write("\nAdded new content.")
f.close()
```

---


## 🧩 **Mini Project – Save User Notes**

```python
# Program to save user notes (without using 'with open')

filename = "user_notes.txt"

note = input("Enter your note: ")

# Open the file in append mode
f = open(filename, "a")

# Write the note to the file
f.write(note + "\n")

# Always close the file after writing
f.close()

print("Note saved successfully!")

```

✅ Run it multiple times — each note will be appended.

---

## 🧠 **Assignment Ideas**

1. Write a program to read a file and count how many lines it has.
2. Write a program that takes user input and saves it in a file.
3. Write a program to copy content from one file to another.
4. Write a program to display all words in a file and count total words.
5. Create a “To-Do List” app where users can add and view tasks saved in a file.
