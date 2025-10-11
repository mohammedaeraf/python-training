# Arrays in Python are called Lists
age = 16

# a List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

# initial list
courses = ["Java", "Python", "MERN"]

# changing the value
courses[1] = "Golang"

# adding elements (similar to push in JS)
courses.append("MongoDB")
courses.append("ChatGPT & AI Tools")

print(courses)

# removing last element (like pop in JS)
last_course = courses.pop()
print(last_course)

# length of list
x = len(courses)
print(x)

# loop through list
print("**** List of Courses *****")
for i in range(x):
    j = i + 1
    print("Course #" + str(j) + " -> " + courses[i])
