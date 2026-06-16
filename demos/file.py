file = open("notes.txt", "w")
file.write("Python is a very powerful programming language.\n")
file.write("It is widely used for web development, data analysis, artificial intelligence, and more.\n")    
file.close()

file = open("notes.txt", "a")
file.write("Python has a large and active community that contributes to its growth and development.\n")
file.close()

file = open("notes.txt", "r")
content = file.read()
words = content.split()
print(f"Number of words: {len(words)}")

totalLetters = 0
for word in words:
    totalLetters = totalLetters + len(word)

print(f"Number of letters: {totalLetters}")
file.close()