#Read user input

city = input() . lower()
sales = float(input())
commission = 0
is_correct_city = True
is_correct_sales = True

#Logic

if city == 'sofia':
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif sales <= 1000:
        commission = sales * 0.07
    elif sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
    else:
        is_correct_sales = False
elif city == 'varna':
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif sales <= 1000:
        commission = sales * 0.075
    elif sales <= 10000:
        commission = sales * 0.1
    elif sales > 10000:
        commission = sales * 0.13
    else:
        is_correct_sales = False
elif city == 'plovdiv':
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif sales <= 1000:
        commission = sales * 0.08
    elif sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
    else:
        is_correct_sales = False
else:
    is_correct_city = False

#Print output

if is_correct_city and is_correct_sales:
    print(f'{commission:.2f}')
else:
    print('error')
