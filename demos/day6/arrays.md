
### 🧮 **1️⃣ Program to Find the Sum of All Elements in an Array**

```python
numbers = [5, 10, 15, 20, 25]
total = 0

for n in numbers:
    total += n

print("Sum of all elements =", total)
```

---

### 🔍 **2️⃣ Program to Find the Maximum and Minimum Element**

```python
numbers = [22, 5, 99, 15, 47]

max_num = max(numbers)
min_num = min(numbers)

print("Maximum =", max_num)
print("Minimum =", min_num)
```

---

### 🔁 **3️⃣ Program to Reverse an Array**

```python
numbers = [10, 20, 30, 40, 50]

reversed_array = numbers[::-1]
print("Original Array:", numbers)
print("Reversed Array:", reversed_array)
```

---

### 🎯 **4️⃣ Program to Count Even and Odd Numbers in an Array**

```python
numbers = [12, 7, 9, 20, 33, 42, 50]
even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
```

---

### 🔢 **5️⃣ Program to Search for an Element in an Array**

```python
numbers = [10, 25, 30, 45, 50]
search = int(input("Enter a number to search: "))

if search in numbers:
    print(search, "is found in the array.")
else:
    print(search, "is not found in the array.")
```
