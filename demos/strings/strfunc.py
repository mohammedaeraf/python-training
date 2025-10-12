msg = "Hello World from Python"

# Convert to uppercase
print(msg.upper())

# Convert to lowercase
print(msg.lower())

# Split string into list of words
words = msg.split()
print(words)

# Count occurrences of a word or letter
print("Count of 'o':", msg.count('o'))

# Replace a word
print(msg.replace("Python", "AI"))

# Check if string starts or ends with something
print(msg.startswith("Hello"))
print(msg.endswith("Python"))
