# Dictionary/Objects

# Key - Value Pairs
student = {
    "id":"A001",
    "name":"Arif Attar",
    "email":"arif@gmail.com",
    "age":21
}
print(student)
print(student["name"])

student["age"] = 22
print(student.get("age"))

for key in student:
    print(key, ":", student.get(key))

for key, value in student.items():
    print(key, "-", value)

# product, course