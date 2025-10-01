# 🔄 Python vs JavaScript – Structural Differences

Both **Python** and **JavaScript (JS)** are popular, beginner-friendly languages, but their **syntax differs a lot**.
Below is a **side-by-side comparison** of key programming constructs.

---

## 1. ✅ Variable Declaration

**JavaScript**

```javascript
// Three ways to declare
var x = 10;      // function-scoped (older)
let y = 20;      // block-scoped (preferred)
const z = 30;    // block-scoped, cannot be reassigned
```

**Python**

```python
x = 10     # No 'var', 'let', or 'const'
y = 20     # Just assign
z = 30
```

🔑 **Key Differences**

* JS has `var`, `let`, `const` for **scope and mutability**.
* Python uses **only assignment (`=`)** — variable type and scope are inferred.

---

## 2. ✅ If / Else If

**JavaScript**

```javascript
let percent = 75;

if (percent >= 80) {
  console.log("A");
} else if (percent >= 60) {
  console.log("B");
} else {
  console.log("C");
}
```

**Python**

```python
percent = 75

if percent >= 80:
    print("A")
elif percent >= 60:    # 'elif' instead of 'else if'
    print("B")
else:
    print("C")
```

🔑 **Key Differences**

* JS uses `{}` to group blocks; Python uses **indentation**.
* Python uses `elif` instead of `else if`.

---

## 3. ✅ For Loop

**JavaScript**

```javascript
// Classic for loop
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

**Python**

```python
# range(start, stop+1)
for i in range(1, 6):
    print(i)
```

🔑 **Key Differences**

* JS requires `let i=...; i<=...; i++`.
* Python uses `range()` with **iteration directly**.

---

## 4. ✅ Arrays (JS) vs Lists (Python)

**JavaScript**

```javascript
let fruits = ["apple", "banana", "mango"];
console.log(fruits[0]);   // "apple"
fruits.push("orange");    // add element
console.log(fruits);
```

**Python**

```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])          # "apple"
fruits.append("orange")   # add element
print(fruits)
```

🔑 **Key Differences**

* JS arrays = Python lists (dynamic, can hold mixed data).
* Methods differ slightly: `push()` (JS) → `append()` (Python).

---

## 5. ✅ Functions

**JavaScript**

```javascript
// Normal function
function greet(name) {
  return `Hello ${name}!`;
}

// Arrow function
const greet2 = (name) => `Hello ${name}!`;

console.log(greet("Ali"));
console.log(greet2("Sara"));
```

**Python**

```python
# Normal function
def greet(name):
    return f"Hello {name}!"

# Lambda (like arrow function, but limited to one expression)
greet2 = lambda name: f"Hello {name}!"

print(greet("Ali"))
print(greet2("Sara"))
```

🔑 **Key Differences**

* JS has **`function`** keyword and **arrow functions** `() =>`.
* Python defines functions with **`def`**, and **lambdas** (one-liners).

---

# 🎯 Summary Table

| Feature        | JavaScript                 | Python                       |
| -------------- | -------------------------- | ---------------------------- |
| Variables      | `var`, `let`, `const`      | simple `=` assignment        |
| If / Else If   | `if () { } else if () { }` | `if ...: elif ...: else ...` |
| For Loop       | `for(init; cond; inc)`     | `for i in range()`           |
| Arrays / Lists | `[]`, `.push()`, `.pop()`  | `[]`, `.append()`, `.pop()`  |
| Functions      | `function` & `()=>`        | `def` & `lambda`             |

