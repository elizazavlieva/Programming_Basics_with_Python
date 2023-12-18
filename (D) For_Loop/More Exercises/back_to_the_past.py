# Read input

inherited_money = float(input())
year_to_live = int(input())
money_needed = 0
age = 18

# Logic
for i in range(1800, year_to_live + 1):

    if i % 2 == 0:
        money_needed += 12000
    else:
        money_needed += 12000 + 50 * age
    age += 1
# Print output
difference = abs(inherited_money - money_needed)
if money_needed <= inherited_money:
    print(f'Yes! He will live a carefree life and will have {difference:.2f} dollars left.')
else:
    print(f'He will need {difference:.2f} dollars to survive.')