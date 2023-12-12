price_vegetables = float(input())
price_fruits = float(input())
vegetables = int(input())
fruits = int(input())

profit = (price_vegetables * vegetables) + (price_fruits * fruits)
profit_euro = profit / 1.94
print(f'{profit_euro:.2f}')
