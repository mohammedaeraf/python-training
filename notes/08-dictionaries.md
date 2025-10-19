# 🧩 **Python Tutorial – Dictionaries**

---

## 🟢 **1. What is a Dictionary?**

A **dictionary** in Python is a collection of **key–value pairs**.
It is used to store related information where each **key** is unique.

👉 **Example:**

```python
student = {
    "name": "Ali",
    "age": 21,
    "course": "Python"
}
```

Here:

- `"name"`, `"age"`, `"course"` → keys
- `"Ali"`, `21`, `"Python"` → values

---

## 🟢 **2. Accessing Dictionary Values**

```python
print(student["name"])     # Output: Ali
print(student.get("course"))  # Output: Python
```

---

## 🟢 **3. Adding and Updating Elements**

```python
student["age"] = 22             # update
student["city"] = "Mangalore"   # add new key-value
print(student)
```

---

## 🟢 **4. Removing Elements**

```python
student.pop("city")   # removes a specific key
print(student)

student.clear()       # removes all items
print(student)
```

---

## 🟢 **5. Looping through a Dictionary**

```python
student = {"name": "Ali", "age": 21, "course": "Python"}

for key in student:
    print(key, ":", student[key])
```

or using `.items()`:

```python
for key, value in student.items():
    print(f"{key} → {value}")
```

---

## 🟢 **6. Useful Dictionary Methods**

| Method      | Description                     |
| ----------- | ------------------------------- |
| `.keys()`   | Returns all keys                |
| `.values()` | Returns all values              |
| `.items()`  | Returns all key–value pairs     |
| `.update()` | Updates from another dictionary |
| `.pop(key)` | Removes item with given key     |

---

## 🟢 **7. Nested Dictionaries**

Dictionaries can be stored **inside another dictionary**.

```python
students = {
    "s1": {"name": "Ali", "age": 20},
    "s2": {"name": "Sara", "age": 21}
}

print(students["s1"]["name"])  # Output: Ali
```

---

## 🧩 **Mini Project – Student Report**

```python
students = {
    "101": {"name": "Ali", "marks": 85},
    "102": {"name": "Sara", "marks": 78},
    "103": {"name": "John", "marks": 92}
}

roll = input("Enter roll number: ")

if roll in students:
    print("Name:", students[roll]["name"])
    print("Marks:", students[roll]["marks"])
else:
    print("Student not found.")
```

---

## 🧠 **Assignment Ideas**

1. Create a dictionary of 3 countries and their capitals.

   - Add a new country.
   - Remove one country.
   - Display all keys and values.

2. Make a dictionary of 3 students with their grades and find the student with the highest grade.

3. Write a program to count word frequencies in a sentence (using dictionary).
