## 🧩 **Tutorial: Object-Oriented Programming (OOP) – Classes and Objects**

### 🎯 **Objective:**

Understand the basic principles of Object-Oriented Programming and learn how to create and use **classes** and **objects** in Python.

---

## 🔹 1. What is OOP?

OOP (Object-Oriented Programming) is a way of structuring a program by bundling related data and behaviors into **objects**.

### Key Concepts:

* **Class** → A blueprint or template for creating objects.
* **Object** → An instance of a class that holds real data.
* **Attributes** → Variables that belong to a class or object.
* **Methods** → Functions that belong to a class or object.

---

## 🔹 2. Creating a Class and Object

### Example:

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"{self.color} {self.brand} engine started!")

# Creating objects
car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

# Accessing attributes and methods
car1.start_engine()
car2.start_engine()
```

✅ **Output:**

```
Red Toyota engine started!
Black BMW engine started!
```

---

## 🔹 3. The `__init__()` Method (Constructor)

* It automatically runs when a new object is created.
* Used for initializing object attributes.

### Example:

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

student1 = Student("Aisha", "A")
print(student1.name, student1.grade)
```

✅ Output:

```
Aisha A
```

---

## 🔹 4. Instance Attributes vs Class Attributes

* **Instance Attributes** → Belong to individual objects.
* **Class Attributes** → Shared by all objects of a class.

### Example:

```python
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name    # Instance attribute
        self.age = age

dog1 = Dog("Max", 3)
dog2 = Dog("Bella", 2)

print(dog1.name, dog1.species)
print(dog2.name, dog2.species)
```

✅ Output:

```
Max Canine
Bella Canine
```

---

## 🔹 5. Adding Methods to Classes

### Example:

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r1 = Rectangle(5, 3)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())
```

✅ Output:

```
Area: 15
Perimeter: 16
```

---

## 🔹 6. The `self` Keyword

* Refers to the current instance of the class.
* Used to access variables and methods that belong to the object.

Example:

```python
def greet(self):
    print("Hello, my name is", self.name)
```

---

## 🔹 7. Updating and Deleting Object Attributes

### Example:

```python
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

emp = Employee("Ali", "Developer")
print(emp.role)

emp.role = "Manager"   # update
print(emp.role)

del emp.role           # delete
```

✅ Output:

```
Developer
Manager
```

---

## 🧠 **Mini Project: Student Report Card**

### Problem:

Create a `Student` class that stores name, marks of 3 subjects, and has methods to calculate total, average, and grade.

### Example Code:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of 3 marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"

student1 = Student("Sara", [85, 92, 78])
print("Name:", student1.name)
print("Total:", student1.total())
print("Average:", student1.average())
print("Grade:", student1.grade())
```

✅ Output:

```
Name: Sara
Total: 255
Average: 85.0
Grade: B
```

---

## 🧩 **Assignment**

1. Create a `Book` class with attributes: `title`, `author`, and `price`. Add a method to display book details.
2. Write a class `Circle` with a method to calculate **area** and **circumference**.
3. Create a class `BankAccount` with methods to **deposit**, **withdraw**, and **display balance**.
4. Extend the Student Report Card mini-project to accept **multiple students** and display their reports.
5. Create a `Laptop` class that has attributes like brand, model, price, and a method to display specifications.
