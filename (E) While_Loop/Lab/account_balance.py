total = 0
while True:
    increase = input()
    if increase == 'NoMoreMoney':
        break
    money = float(increase)
    if money < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {money:.2f}')
    total += money
print(f'Total: {total:.2f}')
