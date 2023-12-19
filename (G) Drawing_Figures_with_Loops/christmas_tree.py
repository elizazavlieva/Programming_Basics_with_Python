n = int(input())

print(' ' * (n + 1) + '|' + ' ' * (n + 1))

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i + ' | ' + '*' * i + ' ' * (n - i))