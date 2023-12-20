days = int(input())
hours = int(input())
daily_expenses = 0
total_expenses = 0

for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 != 0 and hour % 2 == 0:
            daily_expenses += 1.25
        elif day % 2 == 0 and hour % 2 != 0:
            daily_expenses += 2.50
        else:
            daily_expenses += 1
    print(f'Day: {day} - {daily_expenses:.2f} leva')
    total_expenses += daily_expenses
    daily_expenses = 0
print(f'Total: {total_expenses:.2f} leva')
