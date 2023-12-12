trip_price = float(input())
savings = float(input())
count = 0
spending_days = 0

while True:
    if savings >= trip_price:
        print(f'You saved the money for {count} days.')
        break
    command = input()
    money = float(input())
    count += 1
    if command == 'save':
        savings += money
        spending_days = 0
    elif command == 'spend':
        spending_days += 1
        savings -= money
        if spending_days >= 5:
            print("You can't save the money.")
            print(f"{count}")
            break
        if savings < 0:
            savings = 0
