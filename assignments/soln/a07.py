# ==========================================
# Assignment 05: Set Solutions
# ==========================================

# 1. Create and Display a Set
print("1. Create and Display a Set")

fruits = {"Apple", "Mango", "Orange", "Banana", "Grapes"}

print("Fruits =", fruits)

# ------------------------------------------

# 2. Add an Element to a Set
print("\n2. Add an Element to a Set")

colors = {"Red", "Blue", "Green"}

print("Original Set =", colors)

colors.add("Yellow")

print("Updated Set =", colors)

# ------------------------------------------

# 3. Remove an Element from a Set
print("\n3. Remove an Element from a Set")

cities = {"Mumbai", "Delhi", "Bangalore"}

print("Original Set =", cities)

cities.remove("Delhi")

print("Updated Set =", cities)

# ------------------------------------------

# 4. Check if an Element Exists
print("\n4. Check if an Element Exists")

students = {"Ahmed", "Fatima", "Rahul"}

name = "Rahul"

if name in students:
    print(name, "is present in the set.")
else:
    print(name, "is not present in the set.")

# ------------------------------------------

# 5. Find the Union of Two Sets
print("\n5. Find the Union of Two Sets")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union_set = set_a.union(set_b)

print("Set A =", set_a)
print("Set B =", set_b)
print("Union =", union_set)

# ------------------------------------------

# 6. Find the Intersection of Two Sets
print("\n6. Find the Intersection of Two Sets")

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

intersection_set = set_a.intersection(set_b)

print("Set A =", set_a)
print("Set B =", set_b)
print("Intersection =", intersection_set)

# ------------------------------------------

# 7. Find the Difference Between Two Sets
print("\n7. Find the Difference Between Two Sets")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}

difference_set = set_a.difference(set_b)

print("Set A =", set_a)
print("Set B =", set_b)
print("Difference =", difference_set)

# ------------------------------------------

# 8. Remove Duplicate Values from a List
print("\n8. Remove Duplicate Values from a List")

numbers = [10, 20, 10, 30, 20, 40, 50]

unique_values = set(numbers)

print("List =", numbers)
print("Unique Values =", unique_values)

# ------------------------------------------

# Bonus Question: Common Subjects
print("\nBonus Question: Common Subjects")

student1 = {"Math", "Science", "English"}
student2 = {"Science", "English", "Computer"}
student3 = {"English", "Science", "History"}

common_subjects = student1.intersection(student2, student3)

print("Common Subjects =", common_subjects)
