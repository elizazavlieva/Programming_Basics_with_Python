import math
h = float(input()) * 100
w = float(input()) * 100

width = math.floor((w - 100) / 70)
height = math.floor(h / 120)

desks = (width * height) - 3
print(desks)
