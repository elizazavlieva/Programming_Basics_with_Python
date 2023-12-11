# Read input
n = int(input())
# Logic
left_sum = 0
right_sum = 0

for i in range(n):
    num = int(input())
    left_sum += num
for i in range(n):
    num = int(input())
    right_sum += num


# Print output
if right_sum == left_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')