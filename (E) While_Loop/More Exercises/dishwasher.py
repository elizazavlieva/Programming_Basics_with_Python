
bottles = int(input())
dish_detergent = bottles * 750
count = 0
total_plates = 0
total_pans = 0
used_dish_detergent= 0
while True:
    dishes = input()
    if dishes == 'End':
        print("Detergent was enough!")
        print(f'{total_plates} dishes and {total_pans} pots were washed.')
        print(f'Leftover detergent {diff} ml.')
        break
    count += 1
    num_dishes = int(dishes)
    if count % 3 == 0:
        used_dish_detergent += num_dishes * 15
        total_pans += num_dishes
    else:
        used_dish_detergent += num_dishes * 5
        total_plates += num_dishes
    diff = abs(used_dish_detergent - dish_detergent)
    if dish_detergent < used_dish_detergent:
        print(f'Not enough detergent, {diff} ml. more necessary!')
        break