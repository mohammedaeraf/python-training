# Dictionary introduction:
# A dictionary stores key/value pairs. Keys are typically strings,
# and values can be any Python object. Dictionaries are useful when
# you need to look up values by name.

# A dictionary representing a single student.
# Dictionary keys are strings and values can be different types.
student = {
    "name": "Ali",
    "age": 21,
    "course": "Python"
}

# Access values using the key.
print(student["name"])  # prints Ali
# get() is a safe way to retrieve a value; it returns None if the key does not exist.
print(student.get("age"))  # prints 21

# A dictionary representing a product with multiple fields.
product = {
    "id": 101,
    "name": "Laptop",
    "price": 799.99,
    "stock": 50
}

# Update an existing key value.
product["price"] = 749.99
print(product)  # price is updated to 749.99

# Remove a key/value pair from the dictionary.
product.pop("stock")
print(product)  # stock key is removed

# Clear empties the dictionary, leaving an empty dict.
product.clear()
print(product)  # prints {}

# Re-create the student dictionary for iteration examples.
student = {"name": "Ali", "age": 21, "course": "Python"}

# Looping over a dictionary iterates over its keys.
for key in student:
    print(key, ":", student.get(key))

# items() returns key/value pairs, which is useful for printing both together.
for key, value in student.items():
    print(f"{key} → {value}")

# Nested dictionaries can store more complex data structures.
students = {
    "s1": {"name": "Ali", "age": 20},
    "s2": {"name": "Sara", "age": 21}
}

# Access a nested dictionary value by chaining keys.
print(students["s1"]["name"])  # Output: Ali