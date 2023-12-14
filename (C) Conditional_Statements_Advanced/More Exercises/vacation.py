# Read user input

budget = float(input())
season = input()
type_of_accommodation = ''
destination = ''
expense = 0
# Logic

if budget <= 1000:
    type_of_accommodation = 'Camp'
    if season == 'Summer':
        destination = 'Alaska'
        expense = budget * 0.65
    elif season == 'Winter':
        destination = 'Morocco'
        expense = budget * 0.45
elif 1000 < budget <= 3000:
    type_of_accommodation = 'Hut'
    if season == 'Summer':
        destination = 'Alaska'
        expense = budget * 0.80
    elif season == 'Winter':
        destination = 'Morocco'
        expense = budget * 0.60
elif budget > 3000:
    type_of_accommodation = 'Hotel'
    expense = budget * 0.90
    if season == 'Summer':
        destination = 'Alaska'
    elif season == 'Winter':
        destination = 'Morocco'

# Print output
print(f'{destination} - {type_of_accommodation} - {expense:.2f}')