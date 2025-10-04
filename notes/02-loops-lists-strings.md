# 🐍 Python Week 2 Notes & Cheat Sheet (Days 6–10)

---

## **Day 6 – While Loop**

### Syntax

```python
while condition:
    # code block
```

### Example – Countdown

```python
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
```

### Example – Sum of digits

```python
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print("Sum of digits:", sum_digits)
```

✅ Exercise: Print all numbers from 1 to 10 using `while`.

---

## **Day 7 – For Loop with range()**

### Syntax

```python
for variable in range(start, end, step):
    # code block
```

### Example – Multiplication Table

```python
n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
```

### Example – Sum of first 10 numbers

```python
total = 0
for i in range(1, 11):
    total += i
print("Sum =", total)
```

✅ Exercise: Print even numbers between 1–20 using `for`.

---

## **Day 8 – Lists (Arrays in JS)**

### Create a list

```python
fruits = ["apple", "mango", "orange"]
numbers = [10, 20, 30]
mixed = [1, "two", True]
```

### Access & Update

```python
print(fruits[0])  # apple
fruits[1] = "banana"
```

### Add & Remove Elements

```python
fruits.append("kiwi")  # add to end
fruits.insert(1, "grapes")  # add at index 1
fruits.pop()  # remove last
fruits.remove("banana")  # remove by value
```

✅ Exercise: Create a list of 5 favorite foods and print the first and last items.

---

## **Day 9 – List Operations & Iteration**

### Length & Membership

```python
numbers = [10, 20, 30]
print(len(numbers))     # 3
print(20 in numbers)    # True
```

### Iteration

```python
for n in numbers:
    print(n)
```

### Slicing

```python
nums = [1, 2, 3, 4, 5]
print(nums[0:3])  # [1,2,3]
print(nums[2:])   # [3,4,5]
print(nums[:3])   # [1,2,3]
```

✅ Exercise: Print all items of a list in reverse order.

---

## **Day 10 – Strings in Depth**

### String Basics

```python
s = "Hello Python"
print(s[0])     # H
print(s[-1])    # n
print(s[0:5])   # Hello
```

### String Methods

```python
s = "hello world"
print(s.upper())      # HELLO WORLD
print(s.lower())      # hello world
print(s.title())      # Hello World
print(s.split())      # ['hello','world']
print(s.replace("world","Python"))  # hello Python
```

### Example – Word Counter

```python
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))
```

✅ Exercise: Reverse a string entered by the user.

---

# 🎯 Week 2 Quick Reference Cheat Sheet

| Concept         | Syntax / Example                             |
| --------------- | -------------------------------------------- |
| While Loop      | `while condition: ...`                       |
| For Loop        | `for i in range(start,end): ...`             |
| List Create     | `fruits = ["apple","mango"]`                 |
| Access List     | `fruits[0]`                                  |
| Update List     | `fruits[1]="banana"`                         |
| Add Elements    | `append()`, `insert()`                       |
| Remove Elements | `pop()`, `remove()`                          |
| List Length     | `len(list)`                                  |
| Membership      | `item in list`                               |
| Slicing         | `list[start:end]`                            |
| String Index    | `s[0]`, `s[-1]`                              |
| String Methods  | `upper()`, `lower()`, `split()`, `replace()` |