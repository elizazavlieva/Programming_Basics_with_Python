trip_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_income = (puzzles * 2.60) + (talking_dolls * 3) \
               + (teddy_bears * 4.10) + (minions * 8.20) + (trucks * 2)
total_toys = puzzles + talking_dolls + teddy_bears + minions + trucks

if total_toys >= 50:
    total_income *= 0.75

total_income *= 0.90
money = abs(total_income - trip_price)
if total_income >= trip_price:
    print(f'Yes! {money:.2f} lv left.')
elif total_income < trip_price:
    print(f'Not enough money! {money:.2f} lv needed.')
