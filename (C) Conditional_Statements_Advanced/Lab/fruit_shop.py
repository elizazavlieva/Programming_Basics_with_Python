fruit = input().lower()
day_of_week = input() .lower()
qty = float(input())
is_input_correct = True
price = 0

if day_of_week == 'monday' or day_of_week == 'tuesday'\
        or day_of_week == 'wednesday' or day_of_week == 'thursday'\
        or day_of_week == 'friday':
    if fruit == 'banana':
        price = qty * 2.50
    elif fruit == 'apple':
        price = qty * 1.20
    elif fruit == 'orange':
        price = qty * 0.85
    elif fruit == 'grapefruit':
        price = qty * 1.45
    elif fruit == 'kiwi':
        price = qty * 2.70
    elif fruit == 'pineapple':
        price = qty * 5.50
    elif fruit == 'grapes':
        price = qty * 3.85
    else:
        is_input_correct = False
elif day_of_week == 'saturday' or day_of_week == 'sunday':
    if fruit == 'banana':
        price = qty * 2.70
    elif fruit == 'apple':
        price = qty * 1.25
    elif fruit == 'orange':
        price = qty * 0.90
    elif fruit == 'grapefruit':
        price = qty * 1.60
    elif fruit == 'kiwi':
        price = qty * 3.00
    elif fruit == 'pineapple':
        price = qty * 5.60
    elif fruit == 'grapes':
        price = qty * 4.20
    else:
        is_input_correct = False
else:
    is_input_correct = False

if is_input_correct:
    print(f'{price:.2f}')
else:
    print('error')
