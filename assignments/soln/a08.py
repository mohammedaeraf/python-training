# ==========================================
# Assignment 06: Dictionary Solutions
# ==========================================

# 1. Create and Display a Dictionary
print("1. Create and Display a Dictionary")

student = {
    "name": "Ahmed",
    "age": 16,
    "grade": "A"
}

print(student)

# ------------------------------------------

# 2. Access Dictionary Values
print("\n2. Access Dictionary Values")

book = {
    "title": "Python Basics",
    "author": "John Smith"
}

print("Book Title:", book["title"])
print("Author:", book["author"])

# ------------------------------------------

# 3. Add a New Key-Value Pair
print("\n3. Add a New Key-Value Pair")

employee = {
    "name": "Ali",
    "department": "IT"
}

print("Original Dictionary =", employee)

employee["salary"] = 50000

print("Updated Dictionary =", employee)

# ------------------------------------------

# 4. Update a Dictionary Value
print("\n4. Update a Dictionary Value")

product = {
    "product": "Laptop",
    "price": 45000
}

print("Original Dictionary =", product)

product["price"] = 50000

print("Updated Dictionary =", product)

# ------------------------------------------

# 5. Remove an Item from a Dictionary
print("\n5. Remove an Item from a Dictionary")

student = {
    "name": "Sara",
    "age": 15,
    "grade": "B"
}

print("Original Dictionary =", student)

student.pop("age")

print("Updated Dictionary =", student)

# ------------------------------------------

# 6. Display All Keys and Values
print("\n6. Display All Keys and Values")

countries = {
    "India": "New Delhi",
    "Japan": "Tokyo",
    "France": "Paris"
}

print("Countries:")
for country in countries.keys():
    print(country)

print("\nCapitals:")
for capital in countries.values():
    print(capital)

# ------------------------------------------

# 7. Iterate Through a Dictionary
print("\n7. Iterate Through a Dictionary")

marks = {
    "Math": 85,
    "Science": 90,
    "English": 78
}

for subject, mark in marks.items():
    print(subject, ":", mark)

# ------------------------------------------

# 8. Calculate Total Marks from a Dictionary
print("\n8. Calculate Total Marks from a Dictionary")

marks = {
    "Math": 85,
    "Science": 90,
    "English": 78
}

total = 0

for mark in marks.values():
    total = total + mark

print("Total Marks =", total)

# ------------------------------------------

# Bonus Question: Student Report Card
print("\nBonus Question: Student Report Card")

student = {
    "name": "Ahmed",
    "Math": 80,
    "Science": 90,
    "English": 85
}

print("Student Name:", student["name"])

print("Math:", student["Math"])
print("Science:", student["Science"])
print("English:", student["English"])

total = student["Math"] + student["Science"] + student["English"]
average = total / 3

print("Total Marks =", total)
print("Average Marks =", average)

