# Read user input

junior_biker = int(input())
senior_biker = int(input())
type_of_route = input()

tax = 0
total_bikers = 0
# Logic

if type_of_route == 'trail':
    tax = (junior_biker * 5.50) + (senior_biker * 7)
elif type_of_route == 'cross-country':
    total_bikers = junior_biker + senior_biker
    tax = (junior_biker * 8) + (senior_biker * 9.50)
    if total_bikers >= 50:
        tax *= 0.75
elif type_of_route == 'downhill':
    tax = (junior_biker * 12.25) + (senior_biker * 13.75)
elif type_of_route == 'road':
    tax = (junior_biker * 20) + (senior_biker * 21.50)

tax_without_expense = tax * 0.95

# Print output
print(f'{tax_without_expense:.2f}')