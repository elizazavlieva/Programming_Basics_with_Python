days_off = int(input())

working_days = 365 - days_off
days_off_play = days_off * 127
working_days_play = working_days * 63
total_play = days_off_play + working_days_play
difference = abs(total_play - 30000)

hours = difference // 60
minutes = difference % 60

if total_play > 30000:
    print('Tom will run away\n'
          '{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well\n'
          '{hours} hours and {minutes} minutes less for play')
    