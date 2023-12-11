# Read user input
hour = int(input())
day = input().lower()
user_output = ''
# Logic
if 10 <= hour <= 18 and (day == 'monday' or day == 'tuesday'
                         or day == 'wednesday' or day == 'thursday'
                         or day == 'friday' or day == 'saturday'):
    user_output = 'open'
else:
    user_output = 'closed'

# Print output
print(user_output)
