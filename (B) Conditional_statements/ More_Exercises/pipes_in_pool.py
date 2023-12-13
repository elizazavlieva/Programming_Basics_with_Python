v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_litres = h * p1
p2_litres = h * p2

total_litres = p2_litres + p1_litres
pool_percent = (total_litres / v) * 100
p1_percent = (p1_litres / total_litres) * 100
p2_percent = (p2_litres / total_litres) * 100
difference = abs(total_litres - v)

if total_litres <= v:
    print(f'The pool is {pool_percent:.2f}% full. '
          f'Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.')
else:
    print(f'For {h:.2f} hours the pool overflows with {difference:.2f} liters.')
