import math

n = int(input())

print('*'*(2 * n) + ' ' * n + '*' * (n * 2))
middle_row = math.floor(((n - 2) -1) / 2)
for i in range( n - 2):
    if i == middle_row:
        print('*' + '/' * (2 * n - 2) + '*' + '|' * n + '*' + '/' * (2 * n - 2) + '*')
    else:
        print('*' + '/' * (2 * n - 2) + '*' + ' ' * n + '*' + '/' * (2 * n - 2) + '*')
print('*' * (2 * n) + ' ' * n + '*' * (n * 2))