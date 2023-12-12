x = float(input())
y = float(input())
h = float(input())

house = (x * x) + (x * x) + (x * y) + (x * y) - (1.2 * 2) - (1.5 * 1.5)\
    - (1.5 * 1.5)

roof = ((x * h)/2) + ((x * h)/2) + (x * y) + (x * y)

green_paint = house / 3.4
red_paint = roof / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')