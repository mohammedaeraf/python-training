f = open("data.txt", "r")
# content = f.read()
# print(content)

# for line in f:
#     print(line.strip())

lines = f.readlines()
print(lines)
for line in lines:
    print(line.strip())

f.close()

f2 = open("notes.txt", "w")
f2.write("This is a new note.\n")
f2.write("Remember to review and lint the code.\n")
f2.close()

f3 = open("notes.txt", "a")
f3.write("Adding another line to the notes.\n") 
f3.close()
# content_lines = content.splitlines()