# ==========================================
# Assignment 10: Files in Python - Solutions
# ==========================================

# 1. Create and Write to a File
print("1. Create and Write to a File")

with open("student.txt", "w") as file:
    file.write("Name: Ahmed\n")
    file.write("Class: 10\n")
    file.write("Grade: A\n")

print("Data written successfully.")

# ------------------------------------------

# 2. Read and Display File Contents
print("\n2. Read and Display File Contents")

with open("student.txt", "r") as file:
    content = file.read()

print(content)

# ------------------------------------------

# 3. Append Data to a File
print("\n3. Append Data to a File")

with open("student.txt", "a") as file:
    file.write("School: ABC Public School\n")

print("Updated File Contents:")

with open("student.txt", "r") as file:
    print(file.read())

# ------------------------------------------

# 4. Count the Number of Lines in a File
print("\n4. Count the Number of Lines in a File")

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total Lines =", len(lines))

# ------------------------------------------

# 5. Count the Number of Words in a File
print("\n5. Count the Number of Words in a File")

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total Words =", len(words))

# ------------------------------------------

# 6. Copy Contents from One File to Another
print("\n6. Copy Contents from One File to Another")

with open("student.txt", "r") as source:
    data = source.read()

with open("backup.txt", "w") as destination:
    destination.write(data)

print("File copied successfully.")

# ------------------------------------------

# 7. Search for a Word in a File
print("\n7. Search for a Word in a File")

search_word = "Ahmed"

with open("student.txt", "r") as file:
    content = file.read()

if search_word in content:
    print("Word found in the file.")
else:
    print("Word not found in the file.")

# ------------------------------------------

# 8. Store Multiple Student Names in a File
print("\n8. Store Multiple Student Names in a File")

with open("students.txt", "w") as file:
    file.write("Ahmed\n")
    file.write("Fatima\n")
    file.write("Rahul\n")
    file.write("Aisha\n")
    file.write("Zeeshan\n")

print("Names stored successfully.\n")

with open("students.txt", "r") as file:
    print(file.read())

# ------------------------------------------

# Bonus Question: Student Record System
print("\nBonus Question: Student Record System")

name = input("Enter Name: ")
marks = input("Enter Marks: ")

with open("records.txt", "a") as file:
    file.write(name + " - " + marks + "\n")

print("\nRecord saved successfully.\n")

print("All Records:")

with open("records.txt", "r") as file:
    print(file.read())