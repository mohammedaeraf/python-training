# 🔄 Python vs JavaScript – Problem Solving Examples

---

## 1️⃣ Print Multiplication Table of a Number (e.g., 5)

**JavaScript**

```javascript
let n = 5;
for (let i = 1; i <= 10; i++) {
  console.log(`${n} x ${i} = ${n * i}`);
}
```

**Python**

```python
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

---

## 2️⃣ Factorial of a Number

**JavaScript**

```javascript
function factorial(n) {
  let fact = 1;
  for (let i = 1; i <= n; i++) {
    fact *= i;
  }
  return fact;
}
console.log(factorial(5)); // 120
```

**Python**

```python
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))  # 120
```

---

## 3️⃣ Sum of Elements in an Array / List

**JavaScript**

```javascript
let numbers = [10, 20, 30, 40];
let sum = 0;

for (let n of numbers) {
  sum += n;
}
console.log("Sum =", sum);
```

**Python**

```python
numbers = [10, 20, 30, 40]
sum = 0

for n in numbers:
    sum += n

print("Sum =", sum)
```

*(Python shortcut: `sum(numbers)`) ✅*

---

## 4️⃣ Reverse a String

**JavaScript**

```javascript
let str = "hello";
let reversed = str.split("").reverse().join("");
console.log(reversed); // "olleh"
```

**Python**

```python
str = "hello"
reversed = str[::-1]
print(reversed)  # "olleh"
```

---

## 5️⃣ Find Maximum in an Array / List

**JavaScript**

```javascript
let nums = [3, 7, 2, 9, 5];
let max = nums[0];

for (let n of nums) {
  if (n > max) {
    max = n;
  }
}
console.log("Max =", max);
```

**Python**

```python
nums = [3, 7, 2, 9, 5]
max_num = nums[0]

for n in nums:
    if n > max_num:
        max_num = n

print("Max =", max_num)
```

*(Python shortcut: `max(nums)`) ✅*

---

# 🎯 Key Takeaways

* **Loops**: JS uses `for (let i = ...)`, Python uses `for i in range()`.
* **Arrays vs Lists**: JS arrays and Python lists are similar but with **different methods**.
* **Functions**: JS → `function` or `()=>`, Python → `def` and `lambda`.
* **Shortcuts**: Python often provides **built-in functions** (`sum()`, `max()`, slicing).
