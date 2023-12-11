# Read input

actors_name = input()
academy_points = float(input())
rating_ppl = int(input())
current_points = 0
total_points = academy_points

# Logic
for i in range(rating_ppl):
    name_of_rating_ppl = input()
    points_from_rating_ppl = float(input())
    current_points = (len(name_of_rating_ppl) * points_from_rating_ppl) / 2
    total_points += current_points
    if total_points > 1250.5:
        break

# Print output
if total_points > 1250.5:
    print(f'Congratulations, {actors_name} got a nominee for leading role with {total_points:.1f}!')
else:
    difference = abs(1250.5 - total_points)
    print(f'Sorry, {actors_name} you need {difference:.1f} more!')