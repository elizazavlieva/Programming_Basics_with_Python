# Read user input

season = input()
type_of_group = input()
num_students = int(input())
num_nights = int(input())
expense = 0
sports = ''
# Logic

if season == 'Winter':
    if type_of_group == 'girls':
        sports = 'Gymnastics'
        expense = (num_students * num_nights) * 9.60
    elif type_of_group == 'boys':
        sports = 'Judo'
        expense = (num_students * num_nights) * 9.60
    elif type_of_group == 'mixed':
        sports = 'Ski'
        expense = (num_students * num_nights) * 10
elif season == 'Spring':
    if type_of_group == 'girls':
        sports = 'Athletics'
        expense = (num_students * num_nights) * 7.20
    elif type_of_group == 'boys':
        sports = 'Tennis'
        expense = (num_students * num_nights) * 7.20
    elif type_of_group == 'mixed':
        sports = 'Cycling'
        expense = (num_students * num_nights) * 9.50
elif season == 'Summer':
    if type_of_group == 'girls':
        sports = 'Volleyball'
        expense = (num_students * num_nights) * 15
    elif type_of_group == 'boys':
        sports = 'Football'
        expense = (num_students * num_nights) * 15
    elif type_of_group == 'mixed':
        sports = 'Swimming'
        expense = (num_students * num_nights) * 20

if num_students >= 50:
    expense *= 0.50
elif 20 <= num_students < 50:
    expense *= 0.85
elif 10 <= num_students < 20:
    expense *= 0.95

# Print output

print(f'{sports} {expense:.2f} lv.')
