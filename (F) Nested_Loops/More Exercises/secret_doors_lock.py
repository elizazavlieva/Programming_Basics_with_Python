hundreds = int(input())
dozens = int(input())
units = int(input())

for num_1 in range(1, hundreds + 1):
    for num_2 in range(1, dozens + 1):
        for num_3 in range(1, units + 1):
            if num_1 % 2 == 0 and num_3 % 2 == 0:
                if num_2 == 2 or num_2 == 3 or num_2 == 5 or num_2 == 7:
                    print(f'{num_1} {num_2} {num_3}')
