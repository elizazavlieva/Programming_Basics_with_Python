type_fuel = input() .lower()
tank = int(input())

if tank >= 25:
    if type_fuel == 'diesel' or type_fuel == 'gasoline' or type_fuel == 'gas':
        print(f'You have enough {type_fuel}.')
    else:
        print(f'Invalid fuel!')
elif tank < 25:
    if type_fuel == 'diesel' or type_fuel == 'gasoline' or type_fuel == 'gas':
        print(f'Fill your tank with {type_fuel}!')
    else:
        print(f'Invalid fuel!')
        