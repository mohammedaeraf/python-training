# ==========================================
# Assignment 09: Functions - Solutions
# ==========================================

# 1. Create Your First Function
print("1. Create Your First Function")

def welcome():
    print("Welcome to Python Functions")

welcome()

# ------------------------------------------

# 2. Function to Add Two Numbers
print("\n2. Function to Add Two Numbers")

def add_numbers(a, b):
    print("Sum =", a + b)

add_numbers(10, 20)

# ------------------------------------------

# 3. Function to Calculate Area of a Rectangle
print("\n3. Function to Calculate Area of a Rectangle")

def area(length, width):
    print("Area =", length * width)

area(10, 5)

# ------------------------------------------

# 4. Function to Check Even or Odd
print("\n4. Function to Check Even or Odd")

def check_even_odd(number):
    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

check_even_odd(15)

# ------------------------------------------

# 5. Function to Find the Largest of Two Numbers
print("\n5. Function to Find the Largest of Two Numbers")

def largest(a, b):
    if a > b:
        print("Largest Number =", a)
    else:
        print("Largest Number =", b)

largest(25, 40)

# ------------------------------------------

# 6. Function to Calculate Square of a Number
print("\n6. Function to Calculate Square of a Number")

def square(number):
    return number * number

result = square(8)
print("Square =", result)

# ------------------------------------------

# 7. Function to Display a Multiplication Table
print("\n7. Function to Display a Multiplication Table")

def table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

table(5)

# ------------------------------------------

# 8. Function to Calculate Total and Average Marks
print("\n8. Function to Calculate Total and Average Marks")

def calculate_result(marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    print("Marks =", marks)
    print("Total =", total)
    print("Average =", average)

calculate_result([78, 85, 92, 67, 88])

# ------------------------------------------

# Bonus Question: Student Grade Calculator
print("\nBonus Question: Student Grade Calculator")

def grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "D"

marks = 72

print("Marks =", marks)
print("Grade =", grade(marks))