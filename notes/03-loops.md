# 🐍 **Python Tutorial – Loops (`for` and `while`)**

---

## 🔹 1. Introduction

In programming, **loops** allow us to repeat a block of code multiple times — useful when performing repetitive tasks such as printing numbers, processing lists, or calculating sums.

There are two main types of loops in Python:

1. `for` loop – used when you know how many times you want to repeat.
2. `while` loop – used when you want to repeat **until** a condition becomes false.

---

## 🔹 2. The `for` Loop

### 🧩 Syntax:

```python
for variable in sequence:
    statement(s)
```

Here,

* `sequence` can be a list, range of numbers, string, etc.
* The loop runs once for **each item** in the sequence.

---

### ✅ Example 1: Print numbers from 1 to 5

```python
for i in range(1, 6):
    print(i)
```

**Output:**

```
1
2
3
4
5
```

---

### ✅ Example 2: Print each letter of a word

```python
for ch in "Python":
    print(ch)
```

**Output:**

```
P
y
t
h
o
n
```

---

### ✅ Example 3: Print even numbers between 1 and 10

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

**Output:**

```
2
4
6
8
10
```

---

### ✅ Example 4: Sum of Natural Numbers

```python
n = int(input("Enter the last number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)
```

**Output (for n = 5):**

```
Sum = 15
```

---

## 🔹 3. The `while` Loop

### 🧩 Syntax:

```python
while condition:
    statement(s)
```

The loop continues **as long as** the condition is `True`.

---

### ✅ Example 1: Print numbers from 1 to 5

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

**Output:**

```
1
2
3
4
5
```

---

### ✅ Example 2: Print countdown

```python
i = 5
while i >= 1:
    print(i)
    i -= 1
```

**Output:**

```
5
4
3
2
1
```

---

### ✅ Example 3: Sum of even numbers

```python
n = int(input("Enter the limit: "))
total = 0
i = 2

while i <= n:
    total += i
    i += 2

print("Sum of even numbers =", total)
```

---

## 🔹 4. Loop Control Statements

### 🔸 `break`

Stops the loop immediately.

```python
for i in range(1, 10):
    if i == 6:
        break
    print(i)
```

**Output:**

```
1 2 3 4 5
```

---

### 🔸 `continue`

Skips the current iteration and continues with the next.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output:**

```
1 2 4 5
```

---

### 🔸 `else` with Loops

Python allows an `else` clause with loops that executes **after the loop ends normally** (not by break).

```python
for i in range(1, 4):
    print(i)
else:
    print("Loop completed successfully!")
```

**Output:**

```
1
2
3
Loop completed successfully!
```

---

## 🔹 5. Example Programs

### 🧮 Program 1: Print Multiplication Table

```python
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

---

### 🧠 Program 2: Factorial of a Number

```python
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)
```

---

### 💡 Program 3: Sum of Even and Odd Numbers (1 to 10)

```python
even_sum = 0
odd_sum = 0

for i in range(1, 11):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of Even =", even_sum)
print("Sum of Odd =", odd_sum)
```

---

## 🔹 6. Summary

✅ **for loop** → fixed number of repetitions
✅ **while loop** → repeats until condition fails
✅ **break** → stops the loop
✅ **continue** → skips iteration
✅ **else** → runs after normal loop completion

---

## 🧩 **Practice Assignment**

Write Python programs for the following:

1. Print all odd numbers between 1 and 30
2. Find the sum of digits of a number
3. Reverse a given number (e.g., 123 → 321)
4. Display multiplication table from 1 to 5 using nested loops
5. Print pattern:

```
*
* *
* * *
* * * *
* * * * *
```