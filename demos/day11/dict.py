student = {
    "name": "Ali",
    "age": 21,
    "course": "Python"
}

print(student["name"]) 
print(student.get("age"))

product = {
    "id": 101,
    "name": "Laptop",
    "price": 799.99,
    "stock": 50
}

product["price"] = 749.99
print(product)

product.pop("stock")
print(product)

product.clear()
print(product)

student = {"name": "Ali", "age": 21, "course": "Python"}

for key in student:
    print(key, ":", student.get(key))

for key, value in student.items():
    print(f"{key} → {value}")


students = {
    "s1": {"name": "Ali", "age": 20},
    "s2": {"name": "Sara", "age": 21}
}

students = {
    "s1": {"name": "Ali", "age": 20},
    "s2": {"name": "Sara", "age": 21}
}

print(students["s1"]["name"])  # Output: Ali