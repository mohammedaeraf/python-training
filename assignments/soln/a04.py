numbers = [5, 10, 15, 20, 25, 30, 35, 40]
last_four = numbers[-4:]
print(last_four)

every_third = numbers[::3]
print(every_third)

fruits = ["apple", "banana", "cherry", "dates"]
fruits_reversed = fruits[::-1]
print(fruits_reversed)

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
colors_len = len(colors)
middle_index = colors_len // 2

colors[middle_index-1:middle_index + 1] = ["black", "white"]
print(colors)

