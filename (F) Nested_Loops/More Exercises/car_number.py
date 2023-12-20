start = int(input())
end = int(input())

for first_num in range(start, end + 1):
    for second_num in range(start, end + 1):
        for third_num in range(start, end + 1):
            for fourth_num in range(start, end + 1):
                if first_num % 2 == 0 and fourth_num % 2 != 0:
                    if first_num > fourth_num:
                        if (second_num + third_num) % 2 == 0:
                            print(f'{first_num}{second_num}{third_num}{fourth_num}', end=' ')
                elif first_num % 2 != 0 and fourth_num % 2 == 0:
                    if first_num > fourth_num:
                        if (second_num + third_num) % 2 == 0:
                            print(f'{first_num}{second_num}{third_num}{fourth_num}', end=' ')
                            