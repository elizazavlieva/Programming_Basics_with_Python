length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

capacity = length * width * height

liter = capacity * 0.001
liter_needed = liter - (liter * percent)

print(liter_needed)
