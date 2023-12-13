from math import floor
from math import ceil
days = int(input())
food = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
turtle_food_day = float(input()) / 1000

total_food = (dog_food_day + cat_food_day + turtle_food_day) * days
difference = abs(total_food - food)
if total_food <= food:
    print(f'{floor(difference)} kilos of food left.')
else:
    print(f'“{ceil(difference)} more kilos of food are needed.')
