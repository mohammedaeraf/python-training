# Program to count unique words in a sentence

# 1. Input
sentence = input("Enter a sentence: ")

# 2. Processing
words = sentence.split()          # Split the sentence into a list of words
unique_words = set(words)         # Convert list to set to remove duplicates
count = len(unique_words)         # Count number of unique words

# 3. Output
print("Unique words:", unique_words)
print("Count:", count)
