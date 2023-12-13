from math import ceil
from math import floor
magnolia_pieces = int(input())
hyacinths_pieces = int(input())
roses_pieces = int(input())
cactus_pieces = int(input())
present_price = float(input())

magnolias = 3.25
hyacinths = 4
roses = 3.50
cactus = 8

order_price = magnolias * magnolia_pieces + hyacinths_pieces * hyacinths \
              + roses * roses_pieces + cactus_pieces * cactus

income_without_tax = order_price * 0.95
difference = abs(income_without_tax - present_price)

if income_without_tax >= present_price:
    print(f'She is left with {floor(difference)} leva.')
else:
    print(f'She will have to borrow {ceil(difference)} leva.')
