# Step 1: Take input as text
data = input("Enter marks for 3 subjects (comma separated): ")   # Example: "75,82,68"

# Step 2: Split text into a list
marks_list = data.split(',')   # ['75', '82', '68']

# Step 3: Convert each item from string to integer
marks_int = []
for m in marks_list:
    marks_int.append(int(m))   # [75, 82, 68]

# Step 4: Convert list to tuple
marks = tuple(marks_int)       # (75, 82, 68)

total = sum(marks)
average = total / len(marks)  
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")