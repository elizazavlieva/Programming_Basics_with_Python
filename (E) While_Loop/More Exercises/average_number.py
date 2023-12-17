user_input = int(input())
total_sum = 0
for i in range(1, user_input + 1):
    num = int(input())
    total_sum += num
total_sum /= user_input
print(f'{total_sum:.2f}')
