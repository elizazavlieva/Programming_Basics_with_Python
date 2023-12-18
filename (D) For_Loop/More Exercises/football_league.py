# Read input

stadium_capacity = int(input())
num_of_fans = int(input())
first_sector = 0
second_sector = 0
third_sector = 0
fourth_sector = 0

# Logic

for i in range(1, num_of_fans + 1):
    sector = input()
    if sector == 'A':
        first_sector += 1
    elif sector == 'B':
        second_sector += 1
    elif sector == 'V':
        third_sector += 1
    elif sector == 'G':
        fourth_sector += 1

first_sector_prs = first_sector / num_of_fans * 100
second_sector_prs = second_sector / num_of_fans * 100
third_sector_prs = third_sector / num_of_fans * 100
fourth_sector_prs = fourth_sector / num_of_fans * 100

capacity_prs = num_of_fans / stadium_capacity * 100

# Print output

print(f'{first_sector_prs:.2f}%')
print(f'{second_sector_prs:.2f}%')
print(f'{third_sector_prs:.2f}%')
print(f'{fourth_sector_prs:.2f}%')
print(f'{capacity_prs:.2f}%')