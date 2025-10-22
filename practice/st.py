fruits = {"apple", "banana"}

# Add a single element
fruits.add("cherry")

# Add multiple elements
fruits.update(["mango", "orange"])

# Remove elements
fruits.remove("banana")    # Raises error if not found
fruits.discard("kiwi")     # No error even if not found

print(fruits)