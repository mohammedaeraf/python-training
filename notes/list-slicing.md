# 🧩 **Python Lists – Slicing Tutorial**

---

## 📘 **1️⃣ What is Slicing?**

Slicing in Python allows you to **extract a portion** (or sublist) from an existing list.
It is done using the **colon (`:`)** operator inside square brackets.

**Syntax:**

```python
list_name[start:end:step]
```

### Where:

* **start** → index where the slice begins (inclusive)
* **end** → index where the slice ends (exclusive)
* **step** → interval or jump between elements (optional)

---

## 🧮 **2️⃣ Basic Examples**

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

# Extract first three elements
print(numbers[0:3])    # [10, 20, 30]

# Extract elements from index 2 to 5
print(numbers[2:6])    # [30, 40, 50, 60]

# Extract elements from beginning to index 3
print(numbers[:4])     # [10, 20, 30, 40]

# Extract elements from index 3 to the end
print(numbers[3:])     # [40, 50, 60, 70]
```

✅ **Output:**

```
[10, 20, 30]
[30, 40, 50, 60]
[10, 20, 30, 40]
[40, 50, 60, 70]
```

---

## ⚙️ **3️⃣ Using Negative Indexes**

Negative indices count from the **end** of the list.

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

# Last 3 elements
print(numbers[-3:])     # [50, 60, 70]

# Slice from 3rd-last to 2nd-last
print(numbers[-3:-1])   # [50, 60]
```

✅ **Output:**

```
[50, 60, 70]
[50, 60]
```

---

## 🔁 **4️⃣ Using Step Value**

You can use a **step** value to skip elements while slicing.

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

# Every 2nd element
print(numbers[::2])     # [10, 30, 50, 70]

# Slice with start, end, and step
print(numbers[1:6:2])   # [20, 40, 60]
```

✅ **Output:**

```
[10, 30, 50, 70]
[20, 40, 60]
```

---

## 🔄 **5️⃣ Reverse a List using Slicing**

You can **reverse** a list easily using a step of `-1`.

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[::-1])
```

✅ **Output:**

```
[50, 40, 30, 20, 10]
```

---

## 🧠 **6️⃣ Modify List Portions**

You can also **assign new values** to a slice.

```python
fruits = ["apple", "mango", "banana", "orange"]
fruits[1:3] = ["kiwi", "grape"]
print(fruits)
```

✅ **Output:**

```
['apple', 'kiwi', 'grape', 'orange']
```

---

## 🧮 **7️⃣ Example: Extract Even-Indexed Elements**

```python
data = [5, 10, 15, 20, 25, 30, 35]
even_index_values = data[::2]

print("Original List:", data)
print("Even Index Values:", even_index_values)
```

✅ **Output:**

```
Original List: [5, 10, 15, 20, 25, 30, 35]
Even Index Values: [5, 15, 25, 35]
```

---

## 📝 **Practice Tasks for Students**

1. Print the last 4 elements of a list.
2. Print every 3rd element from a list.
3. Create a reversed copy of a list using slicing.
4. Replace the middle two elements of a list with new values.
5. Extract only the first and last 3 elements combined.