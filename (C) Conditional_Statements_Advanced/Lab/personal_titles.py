age = float(input())
gender = input().lower()

if age >= 16:
    if gender == 'm':
        print(f'Mr.')
    elif gender == 'f':
        print(f'Ms.')
elif age < 16:
    if gender == 'm':
        print(f'Master')
    elif gender == 'f':
        print(f'Miss')
        