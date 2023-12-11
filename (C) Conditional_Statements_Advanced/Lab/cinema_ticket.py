day = input() .lower()
result = 0
if day == 'monday' \
        or day == 'tuesday' or day == 'friday':
    result = 12

elif day == 'wednesday' or day == 'thursday':
    result = 14

elif day == 'saturday' or day == 'sunday':
    result = 16

print(result)
