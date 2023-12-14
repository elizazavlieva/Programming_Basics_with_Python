# Read user input
budget = float(input())
category = input()
num_of_ppl = int(input())

transport_expenses = 0
total_expenses = 0

# Logic
if 1 <= num_of_ppl <= 4:
    transport_expenses = budget * 0.75
elif 5 <= num_of_ppl <= 9:
    transport_expenses = budget * 0.60
elif 10 <= num_of_ppl <= 24:
    transport_expenses = budget * 0.50
elif 25 <= num_of_ppl <= 49:
    transport_expenses = budget * 0.40
elif 50<= num_of_ppl:
    transport_expenses = budget * 0.25

if category == 'VIP':
    total_expenses = transport_expenses + (499.99 * num_of_ppl)
elif category == 'Normal':
    total_expenses = transport_expenses + (249.99 * num_of_ppl)

difference = abs(total_expenses - budget)
# Print output

if total_expenses > budget:
    print(f'Not enough money! You need {difference:.2f} leva.')
else:
    print(f'Yes! You have {difference:.2f} leva left.')
