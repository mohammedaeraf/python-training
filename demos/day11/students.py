students = {
    "101": {"name": "Ali", "marks": 85},
    "102": {"name": "Sara", "marks": 78},
    "103": {"name": "John", "marks": 92}
}

roll = input("Enter roll number: ")

if roll in students:
    print("Name:", students[roll]["name"])
    print("Marks:", students[roll]["marks"])
else:
    print("Student not found.")