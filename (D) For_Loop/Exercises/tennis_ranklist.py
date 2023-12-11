# Read input
import math

num_of_tournaments = int(input())
points = int(input())
total_points = 0
won_tournament = 0
# Logic

for i in range(1, num_of_tournaments + 1):
    stage_of_tournament = input()
    if stage_of_tournament == 'W':
        total_points += 2000
        won_tournament += 1
    elif stage_of_tournament == 'F':
        total_points += 1200
    elif stage_of_tournament == 'SF':
        total_points += 720

total_points += points
average_points = (total_points - points) / num_of_tournaments
won_tournament_prs = won_tournament / num_of_tournaments * 100

# Print output
print(f'Final points: {total_points }')
print(f'Average points: {math.trunc(average_points)}')
print(f'{won_tournament_prs:.2f}%')