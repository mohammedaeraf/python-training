numbers = [12, 7, 9, 20, 33, 42, 50, 100, 200, 300]

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd +=1

print(f"Odd Numbers = {odd}")
print(f"Even Numbers = {even}")
