# Word Counter Program

sentence = input("Enter a sentence: ")

# Remove extra spaces and split into words
words = sentence.strip().split()
print(words)

# Count words
word_count = len(words)

print(f"Total words: {word_count}")