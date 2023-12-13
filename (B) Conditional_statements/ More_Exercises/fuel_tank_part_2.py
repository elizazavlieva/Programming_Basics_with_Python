type_fuel = input() . lower()
fuel = float(input())
discount = input() . lower()

price_gasoline = 0
price_gas = 0
price_diesel = 0

if type_fuel == 'gasoline':
    price_gasoline = fuel * 2.22
    if discount == 'yes':
        price_gasoline -= (0.18 * fuel)
    if 20 <= fuel <= 25:
        price_gasoline *= 0.92
    elif fuel > 25:
        price_gasoline *= 0.90
    print(f'{price_gasoline:.2f} lv.')
elif type_fuel == 'diesel':
    price_diesel = fuel * 2.33
    if discount == 'yes':
        price_diesel -= (0.12 * fuel)
    if 20 <= fuel <= 25:
        price_diesel *= 0.92
    elif fuel > 25:
        price_diesel *= 0.90
    print(f'{price_diesel:.2f} lv.')
elif type_fuel == 'gas':
    price_gas = fuel * 0.93
    if discount == 'yes':
        price_gas -= (0.08 * fuel)
    if 20 <= fuel <= 25:
        price_gas *= 0.92
    elif fuel > 25:
        price_gas *= 0.90
    print(f'{price_gas:.2f} lv.')
