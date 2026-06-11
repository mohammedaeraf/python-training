# This file shows Python list slicing with English and Hinglish explanations.
# English: Slicing lets you extract parts of a list by index range.
# Hinglish: Slicing se list ke kuch hisson ko index range se nikal sakte hain.

list_main = [10, 20, 30, 40, 50, 60, 70]

# English: Take items from index 0 up to but not including index 3.
# Hinglish: Index 0 se lekar index 3 se pehle tak ka part.
list1 = list_main[0:3]
print(list1)

# English: Take items from index 3 up to but not including index 6.
# Hinglish: Index 3 se lekar index 6 se pehle tak ka part.
list2 = list_main[3:6] 
print(list2)

# English: Omit the start index, so slicing begins from index 0.
# Hinglish: Start index nahi diya, isliye slicing index 0 se start hota hai.
list3 = list_main[:4]
print(list3)

# English: Omit the end index, so slicing continues to the end of the list.
# Hinglish: End index nahi diya, isliye list ke end tak slice hota hai.
list4 = list_main[4:]
print(list4)

# English: Use step 2 to take every second item from the whole list.
# Hinglish: Step 2 se list ke har dusre item ko lete hain.
list5 = list_main[::2]
print(list5)

# English: Start from index 1 and take every second item.
# Hinglish: Index 1 se shuru karke har dusra item lo.
list6 = list_main[1::2]
print(list6)

# English: Use a negative step to reverse the list.
# Hinglish: Negative step se list reverse ho jati hai.
list7= list_main[::-1]
print(list7)