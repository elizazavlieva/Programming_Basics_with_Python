#Read user input
type_of_movie = input() . lower()
rows = int(input())
columns = int(input())
ticket_price = 0
total_income = 0
seats = rows * columns

#Logic

if type_of_movie == 'premiere':
    ticket_price = 12.00
elif type_of_movie == 'normal':
    ticket_price = 7.5
elif type_of_movie == 'discount':
    ticket_price = 5.00
total_income = seats * ticket_price

#Print output
print(f'{total_income:.2f} leva')