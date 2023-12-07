import math
series = input()
series_time = int(input())
lunch_break = int(input())

lunch_time = lunch_break * 1/8
relax_time = lunch_break * 1/4

free_time = lunch_break - lunch_time - relax_time
diff = abs(series_time - free_time)

if free_time >= series_time:
    print(f'You have enough time to watch '
          f'{series} and left with '
          f'{math.ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch "
          f"{series}, you need {math.ceil(diff)} "
          f"more minutes.")
