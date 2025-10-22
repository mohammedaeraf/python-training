fruits = {"apple", "banana"}

# Add a single element
fruits.add("cherry")
print(fruits)
# Add multiple elements
fruits.update(["mango", "orange"])
print(fruits)
# Remove elements
fruits.remove("banana")    # Raises error if not found
print(fruits)
fruits.discard("kiwi")     # No error even if not found
print(fruits)