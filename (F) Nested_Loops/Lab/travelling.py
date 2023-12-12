total_savings = 0
while True:
    destination = input()
    if destination == 'End':
        break
    min_budget = float(input())
    while True:
        savings = float(input())
        total_savings += savings
        if total_savings >= min_budget:
            print(f'Going to {destination}!')
            total_savings = 0
            break
            