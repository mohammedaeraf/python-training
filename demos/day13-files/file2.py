f = open("data.txt", "r")
i = 1
for line in f:
    print(f"line {i} => {line.strip()}")
    i += 1
f.close()