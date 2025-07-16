# Side-by-side comparison of **Python** and **TypeScript** 

## 🔁 1. **Hello World**

| **Python**             | **TypeScript**                |
| ---------------------- | ----------------------------- |
| \`\`\`python           | \`\`\`ts                      |
| print("Hello, World!") | console.log("Hello, World!"); |
| \`\`\`                 | \`\`\`                        |

---

## 🔣 2. **Variables and Data Types**

| **Python**         | **TypeScript**                 |
| ------------------ | ------------------------------ |
| \`\`\`python       | \`\`\`ts                       |
| name = "Alice"     | let name: string = "Alice";    |
| age = 25           | let age: number = 25;          |
| is\_student = True | let isStudent: boolean = true; |
| \`\`\`             | \`\`\`                         |

---

## 🔄 3. **If/Else Condition**

| **Python**                | **TypeScript**                   |
| ------------------------- | -------------------------------- |
| \`\`\`python              | \`\`\`ts                         |
| x = 10                    | let x: number = 10;              |
| if x > 5:                 | if (x > 5) {                     |
| print("Greater")          | console.log("Greater");          |
| else:                     | } else {                         |
| print("Smaller or Equal") | console.log("Smaller or Equal"); |
| \`\`\`                    | }                                |
|                           | \`\`\`                           |

---

## 🔁 4. **Loops**

### For Loop

| **Python**         | **TypeScript**                |
| ------------------ | ----------------------------- |
| \`\`\`python       | \`\`\`ts                      |
| for i in range(5): | for (let i = 0; i < 5; i++) { |
| print(i)           | console.log(i);               |
| \`\`\`             | }                             |
|                    | \`\`\`                        |

### While Loop

| **Python**   | **TypeScript**  |
| ------------ | --------------- |
| \`\`\`python | \`\`\`ts        |
| i = 0        | let i = 0;      |
| while i < 5: | while (i < 5) { |
| print(i)     | console.log(i); |
| i += 1       | i++;            |
| \`\`\`       | }               |
|              | \`\`\`          |

---

## 🧮 5. **Functions**

| **Python**             | **TypeScript**                         |
| ---------------------- | -------------------------------------- |
| \`\`\`python           | \`\`\`ts                               |
| def greet(name):       | function greet(name: string): string { |
| return "Hello " + name | return "Hello " + name;                |
|                        | }                                      |
| print(greet("Alice"))  | console.log(greet("Alice"));           |
| \`\`\`                 | \`\`\`                                 |

---

## 📦 6. **Classes and Objects**

| **Python**                     | **TypeScript**                                          |
| ------------------------------ | ------------------------------------------------------- |
| \`\`\`python                   | \`\`\`ts                                                |
| class Person:                  | class Person {                                          |
| def **init**(self, name, age): | constructor(public name: string, public age: number) {} |
| self.name = name               | }                                                       |
| self.age = age                 | const p = new Person("Alice", 25);                      |
|                                | console.log(p.name);                                    |
| p = Person("Alice", 25)        | \`\`\`                                                  |
| print(p.name)                  |                                                         |
| \`\`\`                         |                                                         |

---

## 📂 7. **List / Array**

| **Python**           | **TypeScript**                       |
| -------------------- | ------------------------------------ |
| \`\`\`python         | \`\`\`ts                             |
| numbers = \[1, 2, 3] | let numbers: number\[] = \[1, 2, 3]; |
| print(numbers\[0])   | console.log(numbers\[0]);            |
| \`\`\`               | \`\`\`                               |

---

## 🔍 8. **Dictionary / Object**

| **Python**                             | **TypeScript**                            |
| -------------------------------------- | ----------------------------------------- |
| \`\`\`python                           | \`\`\`ts                                  |
| student = {"name": "Alice", "age": 25} | let student = { name: "Alice", age: 25 }; |
| print(student\["name"])                | console.log(student.name);                |
| \`\`\`                                 | \`\`\`                                    |

---

## 📘 Summary Table

| Concept              | Python             | TypeScript                     |
| -------------------- | ------------------ | ------------------------------ |
| Variable Declaration | `x = 10`           | `let x: number = 10;`          |
| Print Output         | `print("Hi")`      | `console.log("Hi")`            |
| Function             | `def func():`      | `function func():`             |
| List/Array           | `[]`               | `[]` with type annotation      |
| Dictionary/Object    | `{"key": "value"}` | `{ key: "value" }`             |
| Class                | `class MyClass:`   | `class MyClass {}`             |
| Type System          | Dynamic            | Static (with type annotations) |

