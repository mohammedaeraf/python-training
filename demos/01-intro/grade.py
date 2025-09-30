# Program to print grade based on percent (A >= 80; B >=60, C>=40, D)

# 1. Input
percent = 34.60
grade = ""

# 2. Processing
if percent >= 80:
    grade = "A"
elif percent >= 60:
    grade = "B"
elif percent >= 40:
    grade = "C"
else:
    grade = "D"

# 3. Output
print("Percent =", percent)
print("Grade =", grade)
