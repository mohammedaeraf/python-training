# initial list
fruits = ["apple", "mango", "orange"]

# ✅ Remove the first element (like shift())
first_fruit = fruits.pop(0)
print(first_fruit)  # 👉 Output: apple
print(fruits)       # 👉 Remaining list: ["mango", "orange"]

# ✅ Insert an element at the beginning (like unshift())
fruits.insert(0, "kiwi")
print(fruits)       # 👉 ["kiwi", "mango", "orange"]

# ✅ Search for an element's position (like indexOf)
index = fruits.index("orange")
print("Position of orange =", index)  # 👉 2

# ✅ Check if an element exists (like includes)
search_fruit = "banana"
found = search_fruit in fruits
print(f"{search_fruit} present in array {found}")  # 👉 False

# ✅ Extract part of a list (like slice)
numbers = [19, 20, 30, 40, 50, 60, 70]
part = numbers[0:5]  # elements from index 0 to 4
print(part)           # 👉 [19, 20, 30, 40, 50]

# ✅ Combine two lists (like concat)
a = [1, 2]
b = [3, 4, 5]
c = a + b
print(c)  # 👉 [1, 2, 3, 4, 5]

# ✅ Insert element in the middle (like splice)
a.insert(1, 100)
print(a)  # 👉 [1, 100, 2]

b.insert(2, 1000)
print(b)  # 👉 [3, 4, 1000, 5]

# ✅ Calculate total using for loop
numbers2 = [10, 20, 30]
total = 0

for i in range(len(numbers2)):
    total += numbers2[i]

print("Total =", total)            # 👉 60
print(f"Total = {total}")          # Using f-string

# ✅ Calculate total using for-of equivalent (Python for-in loop)
total = 0
for n in numbers2:
    total += n

print("Total =", total)            # 👉 60
