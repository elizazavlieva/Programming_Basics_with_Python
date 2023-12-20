max_num_one = int(input())
max_num_two = int(input())
max_num_three = int(input())

for num_one in range(1, max_num_one + 1):
    for num_two in range(2, max_num_two + 1):
        for num_three in range(1, max_num_three + 1):
            if num_one % 2 == 0 and num_three % 2 == 0:
                if num_two == 2 or num_two == 3 or num_two == 5 or num_two == 7:
                    print(f'{num_one} {num_two} {num_three}')
