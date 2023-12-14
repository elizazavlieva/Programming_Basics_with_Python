# Read user input

season = input()
kilometers_monthly = float(input())

salary = 0

# Logic

if kilometers_monthly <= 5000:
    if season == 'Spring' or season == 'Autumn':
        salary = (kilometers_monthly * 0.75) * 4
    elif season == 'Summer':
        salary = (kilometers_monthly * 0.90) * 4
    elif season == 'Winter':
        salary = (kilometers_monthly * 1.05) * 4
elif 5000 < kilometers_monthly <= 10000:
    if season == 'Spring' or season == 'Autumn':
        salary = (kilometers_monthly * 0.95) * 4
    elif season == 'Summer':
        salary = (kilometers_monthly * 1.10) * 4
    elif season == 'Winter':
        salary = (kilometers_monthly * 1.25) * 4
elif 10000 < kilometers_monthly <= 20000:
    salary = (kilometers_monthly * 1.45) * 4

salary *= 0.90

# Print output
print(f'{salary:.2f}')