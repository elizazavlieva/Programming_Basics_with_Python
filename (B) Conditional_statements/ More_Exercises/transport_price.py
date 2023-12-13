kilometers = int(input())
time_of_day = input().lower()

price_taxi = 0
price_bus = 0
price_train = 0

if time_of_day == 'day':
    price_taxi = (kilometers * 0.79) + 0.70
    if 20 <= kilometers < 100:
        price_bus = 0.09 * kilometers
        if price_taxi > price_bus:
            print(f'{price_bus:.2f}')
        else:
            print(f'{price_taxi:.2f}')
    elif kilometers >= 100:
        price_train = kilometers * 0.06
        if price_taxi > price_train:
            print(f'{price_train:.2f}')
        else:
            print(f'{price_taxi:.2f}')
    else:
        print(f'{price_taxi:.2f}')

elif time_of_day == 'night':
    price_taxi = (kilometers * 0.90) + 0.70
    if 20 <= kilometers < 100:
        price_bus = 0.09 * kilometers
        if price_taxi > price_bus:
            print(f'{price_bus:.2f}')
        else:
            print(f'{price_taxi:.2f}')
    elif kilometers >= 100:
        price_train = kilometers * 0.06
        if price_taxi > price_train:
            print(f'{price_train:.2f}')
        else:
            print(f'{price_taxi:.2f}')
    else:
        print(f'{price_taxi:.2f}')
