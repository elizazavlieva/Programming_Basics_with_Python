num = int(input())
counter = 0

for num_one in range(0, num + 1):
    for num_two in range(num + 1):
        for num_three in range(num + 1):
            summary = num_one + num_two + num_three
            if summary == num:
                counter += 1
print(counter)
