import math

first_player = int(input())
second_player = int(input())
third_player = int(input())

time = first_player + second_player + third_player

minutes = math.floor(time // 60)
seconds = time % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
