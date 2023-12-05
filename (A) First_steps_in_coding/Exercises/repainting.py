nylon = int(input()) + 2
paint = int(input())
thinner = int(input())
working_hours = int(input())

paint = paint + (paint * 0.10)
subtotal = (nylon * 1.50) + (paint * 14.50) + (thinner * 5.00) + 0.40
payment_per_hour = subtotal * 0.30
total = subtotal + (payment_per_hour * working_hours)
print(total)
