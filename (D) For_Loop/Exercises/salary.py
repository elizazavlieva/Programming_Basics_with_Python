# Read input
import math

open_tabs = int(input())
salary = int(input())

# Logic
for i in range(open_tabs):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        break
# Print output
if salary > 0:
    print(f' {math.trunc(salary)}')
    