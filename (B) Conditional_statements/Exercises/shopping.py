budget = float(input())
video_card = int(input())
processor = int(input())
ram_memory = int(input())

video_card_price = 250 * video_card
processor_price = (video_card_price * 0.35) * processor
ram_memory_price = (video_card_price * 0.10) * ram_memory

total_expenses = (video_card_price + processor_price + ram_memory_price)

if video_card > processor:
    total_expenses -= (total_expenses * 0.15)

diff = abs(budget - total_expenses)

if budget >= total_expenses:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')