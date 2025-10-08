# Arrays in Python are called Lists
age = 16

# a List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

# initial list
courses = ["Java", "Python", "MERN"]

# changing the value
courses[2] = "Golang"
courses.append("MongoDB")
courses.append("ChatGPT & AI Tools")
print(courses)

last_course = courses.pop()
print(last_course)

last_course = courses.pop()
print(last_course)

print(courses)