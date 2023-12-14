# Read user input

budget = float(input())
season = input()
car_class = ''
type_of_car = ''
price = 0

# Logic
if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        type_of_car = 'Jeep'
        price = budget * 0.65
elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        type_of_car = 'Jeep'
        price = budget * 0.80
elif budget > 500:
    car_class = 'Luxury class'
    type_of_car = 'Jeep'
    price = budget * 0.90

# Print output

print(car_class)