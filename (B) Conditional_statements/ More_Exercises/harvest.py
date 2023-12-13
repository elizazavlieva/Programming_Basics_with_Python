from math import floor
from math import ceil
area_vineyard = int(input())
grapes_per_meter = float(input())
litres_vine_needed = int(input())
workers = int(input())

total_harvest = area_vineyard * grapes_per_meter
harvest = total_harvest * 0.40

vine_from_harvest = harvest / 2.5
difference = abs(vine_from_harvest - litres_vine_needed)
vine_per_person = difference / workers

if vine_from_harvest < litres_vine_needed:
    print(f'It will be a tough winter! More {floor(difference)} liters wine needed.')
elif vine_from_harvest >= litres_vine_needed:
    print(f'Good harvest this year! Total wine: {floor(vine_from_harvest)} liters.')
    print(f'{ceil(difference)} liters left -> {ceil(vine_per_person)} liters per person.')
    