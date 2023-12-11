# Read input
name = input()
# logic
summary = 0
for i in range(len(name)):
    char = name[i]
    if char == 'a':
        summary += 1
    elif char == 'e':
        summary += 2
    elif char == 'i':
        summary += 3
    elif char == 'o':
        summary += 4
    elif char == 'u':
        summary += 5

# Print output
print(summary)
