# Read user input
animal = input() . lower()
user_output = ''
#Logic
if animal == 'dog':
    user_output = 'mammal'
elif animal == 'crocodile':
    user_output = 'reptile'
elif animal == 'tortoise':
    user_output = 'reptile'

elif animal == 'snake':
    user_output = 'reptile'
else:
    user_output = 'unknown'

# print output
print(user_output)
