# Read user input

temperature = int(input())
part_of_the_day = input() .lower()
outfit = ''
shoes = ''

#Logic

if part_of_the_day == 'morning':
    if temperature <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif part_of_the_day == 'afternoon':
    if temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif temperature >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif part_of_the_day == 'evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

#Print output

print(f'It\'s {temperature} degrees, get your {outfit} and {shoes}.')