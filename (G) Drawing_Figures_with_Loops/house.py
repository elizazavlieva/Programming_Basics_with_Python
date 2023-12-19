import math

n = int(input())
stars = 1
if n % 2 == 0:
    stars += 1
roof = math.ceil(n/2)

for i in range(roof):
    print('-'*((n - stars)//2) + '*' * stars + '-'*((n - stars)//2))
    stars += 2
for j in range((n//2)):
    print('|' + '*' * (n-2) + '|')