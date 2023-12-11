# Read input
age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_for_bday = 0
toys = 0
income = 0

# Logic
for i in range(1,age + 1):
    if i % 2 == 0:
        money_for_bday += 10
        income += money_for_bday - 1
    else:
        toys += 1


income += toys * toy_price
difference = abs(income - washing_machine_price)

# Print output
if income >= washing_machine_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
    