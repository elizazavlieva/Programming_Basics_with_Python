# Read user input

budget = float(input())
season = input()
total_expense = 0
destination = ''
accommodation = ''
# Logic
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        accommodation = 'Camp'
        total_expense = budget * 0.30
    elif season == 'winter':
        accommodation = 'Hotel'
        total_expense = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        accommodation = 'Camp'
        total_expense = budget * 0.40
    elif season == 'winter':
        accommodation = 'Hotel'
        total_expense = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    accommodation = 'Hotel'
    total_expense = budget * 0.90

# Print output
print(f'Somewhere in {destination}')
print(f'{accommodation} - {total_expense:.2f}')
