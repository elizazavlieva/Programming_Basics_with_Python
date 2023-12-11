# Read input
import sys

n = int(input())

# Logic
summary = 0
max_num = -sys.maxsize


for i in range (0, n):
    num = int(input())
    summary += num
    if num > max_num:
        max_num = num


# Print output
if max_num == (summary - max_num):
    print('Yes')
    print(f'Sum = {summary - max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - (summary - max_num))}')
    