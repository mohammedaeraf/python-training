# 🧩 **Python OOP – Inheritance & Method Overriding**

---

## 🔹 **1. What is Inheritance?**

Inheritance allows a **class (child/subclass)** to **reuse attributes and methods** of another **class (parent/superclass)**.
It promotes **code reusability**.

**Syntax:**

```python
class ChildClass(ParentClass):
    # additional attributes or methods
```

---

## 🔹 **2. Simple Inheritance Example**

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"{self.brand} {self.model}")

# Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # call parent constructor
        self.doors = doors

    def show_details(self):
        print(f"{self.brand} {self.model} with {self.doors} doors")

# Objects
v = Vehicle("Toyota", "Corolla")
v.show_info()

c = Car("BMW", "X5", 4)
c.show_info()
c.show_details()
```

✅ Output:

```
Toyota Corolla
BMW X5
BMW X5 with 4 doors
```

---

## 🔹 **3. Method Overriding**

A child class can **override** a method of the parent class by defining it again.

```python
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car engine is starting with a roar!")

v = Vehicle()
v.start()   # Vehicle method
c = Car()
c.start()   # Overridden method
```

✅ Output:

```
Vehicle is starting
Car engine is starting with a roar!
```

---

## 🔹 **4. `super()` Function**

- `super()` allows calling methods of the **parent class** inside the child class.
- Useful for extending parent functionality.

```python
class Car(Vehicle):
    def start(self):
        super().start()  # call parent method
        print("Car is ready to drive")
```

---

## 🔹 **5. Multiple Inheritance**

Python supports **multiple inheritance** — a class can inherit from **more than one parent**.

```python
class Engine:
    def engine_type(self):
        print("V8 Engine")

class Wheels:
    def wheel_count(self):
        print("4 wheels")

class Car(Engine, Wheels):
    pass

c = Car()
c.engine_type()
c.wheel_count()
```

✅ Output:

```
V8 Engine
4 wheels
```

---

## 🔹 **6. Mini Project – Employee Hierarchy**

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        super().show_info()
        print(f"Department: {self.department}")

m = Manager("Ali", 50000, "IT")
m.show_info()
```

✅ Output:

```
Name: Ali, Salary: 50000
Department: IT
```

---

## 🧠 **Assignment Ideas**

1. Create a `Shape` class with `area()` and `perimeter()` methods.

   - Derive `Rectangle` and `Circle` classes.
   - Override `area()` and `perimeter()` methods.

2. Create a `Vehicle` class and derive `Bike` and `Car` classes.

   - Add method `fuel_type()` and override it in child classes.

3. Create a `BankAccount` class.

   - Derive `SavingsAccount` and `CurrentAccount`.
   - Add method `calculate_interest()` and override it in subclasses.

4. Multiple inheritance example:

   - Create classes `Flyable` and `Swimmable`.
   - Create `Duck` class that inherits both.

5. Extend the **Employee Hierarchy** mini-project to include `Developer` and `Intern` classes with different roles and salaries.
