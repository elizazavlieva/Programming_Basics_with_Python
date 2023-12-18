# Read input
game_turns = int(input())
result = 0
first_points = 0
second_points = 0
third_points = 0
fourth_points = 0
fifth_points = 0
invalid_points = 0

# Logic

for i in range(1, game_turns + 1):
    num = int(input())
    if 0 <= num <= 9:
        result += num * 0.20
        first_points += 1
    elif 10 <= num <= 19:
        result += num * 0.30
        second_points += 1
    elif 20 <= num <= 29:
        result += num * 0.40
        third_points += 1
    elif 30 <= num <= 39:
        result += 50
        fourth_points += 1
    elif 40 <= num <= 50:
        result += 100
        fifth_points += 1
    else:
        result /= 2
        invalid_points += 1

first_points_prs = first_points / game_turns * 100
second_points_prs = second_points / game_turns * 100
third_points_prs = third_points / game_turns * 100
fourth_points_prs = fourth_points / game_turns * 100
fifth_points_prs = fifth_points / game_turns * 100
invalid_points_prs = invalid_points / game_turns * 100

# Print output

print(f'{result:.2f}')
print(f'From 0 to 9: {first_points_prs:.2f}%')
print(f'From 10 to 19: {second_points_prs:.2f}%')
print(f'From 20 to 29: {third_points_prs:.2f}%')
print(f'From 30 to 39: {fourth_points_prs:.2f}%')
print(f'From 40 to 50: {fifth_points_prs:.2f}%')
print(f'Invalid numbers: {invalid_points_prs:.2f}%')