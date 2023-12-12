num_1 = int(input())
num_2 = int(input())

for current_num in range(num_1, num_2 + 1):
    odd_sum = 0
    even_sum = 0
    current_num_str = str(current_num)
    for index, digit in enumerate(current_num_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(current_num, end=' ')
        