# Read user input
type_of_flowers = input()
qty = int(input())
budget = int(input())
total_price = 0
price_roses = 5
price_dahlias = 3.8
price_tulips = 2.8
price_narcissus = 3
price_gladiolus = 2.5

# Logic
if type_of_flowers == 'Roses':
    if qty > 80:
        total_price = (qty * price_roses) * 0.90
    else:
        total_price = qty * price_roses
elif type_of_flowers == 'Dahlias':
    if qty > 90:
        total_price = (qty * price_dahlias) * 0.85
    else:
        total_price = qty * price_dahlias
elif type_of_flowers == 'Tulips':
    if qty > 80:
        total_price = (qty * price_tulips) * 0.85
    else:
        total_price = qty * price_tulips
elif type_of_flowers == 'Narcissus':
    if qty < 120:
        total_price = ((qty * price_narcissus) * 0.15) + (qty * price_narcissus)
    else:
        total_price = qty * price_narcissus
elif type_of_flowers == 'Gladiolus':
    if qty < 80:
        total_price = ((qty * price_gladiolus) * 0.20) + (qty * price_gladiolus)
    else:
        total_price = qty * price_gladiolus

# Print output
difference = abs(budget - total_price)
if budget >= total_price:
    print(f'Hey, you have a great garden with {qty} {type_of_flowers} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')
    