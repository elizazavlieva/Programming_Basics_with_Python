tax_for_training = int(input())

shoes_price = tax_for_training - (tax_for_training * 0.4)
outfit = shoes_price - (shoes_price * 0.2)
ball = outfit * 0.25
accessories = ball * 0.2

total = shoes_price + outfit + ball + accessories + tax_for_training

print(total)
