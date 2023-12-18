n = int(input())
current_pair = 0
previous_pair = 0
max_diff_pair = 0

for i in range(2*n):
    num = int(input())
    current_pair += num
    if i % 2 != 0 and i >=3:
        max_diff_pair = max(max_diff_pair, abs(current_pair - previous_pair))
        previous_pair = current_pair
        current_pair = 0
    elif i % 2 != 0 and i >= 1:
        previous_pair = current_pair
        current_pair = 0

if max_diff_pair == 0:
    print(f'Yes, value={previous_pair}')
else:
    print(f'No, maxdiff={max_diff_pair}')