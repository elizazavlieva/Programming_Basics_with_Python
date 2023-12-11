# Read user input
budget = int(input())
season = input()
fishermen = int(input())

total_expense = 0
spring_price = 3000
summer_autumn_price = 4200
winter_price = 2600

# Logic

if season == 'Spring':
    if fishermen <= 6:
        total_expense = spring_price * 0.90
    elif 7 <= fishermen <= 11:
        total_expense = spring_price * 0.85
    elif fishermen >= 12:
        total_expense = spring_price * 0.75
    else:
        total_expense = spring_price
elif season == 'Summer' or season == 'Autumn':
    if fishermen <= 6:
        total_expense = summer_autumn_price * 0.90
    elif 7 <= fishermen <= 11:
        total_expense = summer_autumn_price * 0.85
    elif fishermen >= 12:
        total_expense = summer_autumn_price * 0.75
    else:
        total_expense = summer_autumn_price
elif season == 'Winter':
    if fishermen <= 6:
        total_expense = winter_price * 0.90
    elif 7 <= fishermen <= 11:
        total_expense = winter_price * 0.85
    elif fishermen >= 12:
        total_expense = winter_price * 0.75
    else:
        total_expense = winter_price

if fishermen % 2 == 0 and (season == 'Spring' or
                          season == 'Summer' or season == 'Winter'):
    total_expense *= 0.95
difference = abs(budget - total_expense)
# Print output
if budget >= total_expense:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')
    