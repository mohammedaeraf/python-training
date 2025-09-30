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
course_count = len(courses)
print(course_count)

# loop through list
print("**** List of Courses *****")
for i in range(len(courses)):
    j = i + 1
    print("Course #" + str(j) + " -> " + courses[i])
