days = int(input())
type_of_room = input()
rating = input()
expenses = 0
if type_of_room == 'room for one person':
        expenses = (days - 1) * 18.00
elif type_of_room == 'apartment':
    expenses = (days - 1) * 25.00
    if days < 10:
        expenses *= 0.70
    elif days <= 15:
        expenses *= 0.65
    elif days > 15:
        expenses *= 0.50
elif type_of_room == 'president apartment':
    expenses = (days - 1) * 35.00
    if days < 10:
        expenses *= 0.80
    elif days == 10 or days <= 15:
        expenses *= 0.85
    elif days > 15:
        expenses *= 0.80

if rating == 'positive':
    expenses += (expenses * 0.25)
elif rating == 'negative':
    expenses *= 0.90

print(f'{expenses:.2f}')