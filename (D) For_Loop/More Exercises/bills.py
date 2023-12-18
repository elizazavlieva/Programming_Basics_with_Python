# Read input

months = int(input())
total_electricity_bills = 0
total_water_bills = 0
total_internet_bills = 0
other_expenses = 0
total_other_expenses = 0
average_expenses = 0
# Logic
for i in range(1, months + 1):
    electricity_bill = float(input())
    total_electricity_bills += electricity_bill
    total_water_bills += 20
    total_internet_bills += 15
    other_expenses = (electricity_bill + 15 + 20) + (electricity_bill + 15 + 20) * 0.20
    total_other_expenses += other_expenses
average_expenses = (total_other_expenses + total_internet_bills + total_water_bills\
                    + total_electricity_bills) / months
# Print output

print(f'Electricity: {total_electricity_bills:.2f} lv')
print(f'Water: {total_water_bills:.2f} lv')
print(f'Internet: {total_internet_bills:.2f} lv')
print(f'Other: {total_other_expenses:.2f} lv')
print(f'Average: {average_expenses:.2f} lv')