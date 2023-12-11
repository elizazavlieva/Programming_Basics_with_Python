# Read input
climber_groups = int(input())

musala_group = 0
monblan_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0
total_climbers = 0
# Logic
for group in range(1, climber_groups + 1):
    ppl_in_group = int(input())
    total_climbers += ppl_in_group
    if ppl_in_group < 6:
        musala_group += ppl_in_group
    elif ppl_in_group < 13:
        monblan_group += ppl_in_group
    elif ppl_in_group < 26:
        kilimanjaro_group += ppl_in_group
    elif ppl_in_group < 41:
        k2_group += ppl_in_group
    else:
        everest_group += ppl_in_group

musala_percent = (musala_group / total_climbers) * 100
monblan_percent = (monblan_group / total_climbers) * 100
kilimanjaro_percent = (kilimanjaro_group / total_climbers) * 100
k2_percent = (k2_group / total_climbers) * 100
everest_percent = (everest_group / total_climbers) * 100

# Print output

print(f'{musala_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')