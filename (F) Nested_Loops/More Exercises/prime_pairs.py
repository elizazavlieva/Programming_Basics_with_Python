import math
first_pair_start = int(input())
second_pair_start = int(input())
first_pair_end = int(input()) + first_pair_start
second_pair_end = int(input()) + second_pair_start


for i in range(first_pair_start, first_pair_end + 1):
    for j in range(second_pair_start, second_pair_end + 1):
        is_first_num_prime = True
        is_second_num_prime = True
        for k in range(2, int(math.sqrt(i)) + 1):
            if i % k == 0:
                is_first_num_prime = False
                break
        for k in range(2, int(math.sqrt(j)) + 1):
            if j % k == 0:
                is_second_num_prime = False
                break
        if is_first_num_prime and is_second_num_prime:
            print(f'{i}{j}')