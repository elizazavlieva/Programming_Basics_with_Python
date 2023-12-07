budget = float(input())
statists = int(input())
cloths_price_per_statist = float(input())

decore_price = budget * 0.10
price_for_clothing = statists * cloths_price_per_statist

if statists > 150:
    price_for_clothing *= 0.90

expenses = decore_price + price_for_clothing
diff = abs(expenses - budget)

if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
