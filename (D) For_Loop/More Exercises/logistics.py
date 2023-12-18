# Read input
number_of_cargo = int(input())
total_tonnage = 0
average_price = 0
van_tonnage = 0
truck_tonnage = 0
train_tonnage = 0
price = 0

# Logic
for i in range( 1, number_of_cargo + 1):
    tonnage = int(input())
    total_tonnage += tonnage
    if tonnage <= 3:
        price += tonnage * 200
        van_tonnage += tonnage
    elif tonnage < 12:
        price += tonnage * 175
        truck_tonnage += tonnage
    elif tonnage >= 12:
        price += tonnage * 120
        train_tonnage += tonnage

average_price = price / total_tonnage

van_percent = van_tonnage / total_tonnage * 100
train_percent = train_tonnage / total_tonnage * 100
truck_percent = truck_tonnage / total_tonnage * 100

# Print output

print(f'{average_price:.2f}\n'
      f'{van_percent:.2f}%\n'
      f'{truck_percent:.2f}%\n'
      f'{train_percent:.2f}%')
