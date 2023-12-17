expected_money = int(input())
count = 0
count_in_cash = 0
count_with_card = 0
total_money = 0
money_in_cash = 0
money_with_card = 0
while expected_money > total_money:
    command = input()
    if command == 'End':
        break
    count += 1
    price = int(command)
    if count % 2 != 0:
        if price > 100:
            print('Error in transaction!')
        else:
            total_money += price
            money_in_cash += price
            count_in_cash += 1
            print('Product sold!')
    else:
        if price < 10:
            print('Error in transaction!')
        else:
            total_money += price
            money_with_card += price
            count_with_card += 1
            print('Product sold!')

average_cs = 0.0
if money_in_cash > 0:
    average_cs = money_in_cash / count_in_cash
average_cc = 0.0
if money_with_card > 0:
    average_cc = money_with_card / count_with_card

if total_money >= expected_money:
    print(f'Average CS: {average_cs:.2f}')
    print(f'Average CC: {average_cc:.2f}')
else:
    print("Failed to collect required money for charity.")