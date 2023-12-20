last_sector = input()
row_num = int(input())
seats_num_odd_row = int(input())
seats_num_even_row = seats_num_odd_row + 2
sector_counter = 0
counter_seats = 0
start = ord('A')
end = ord(last_sector)
seat = 97
for first_symbol in range(start, end + 1):
    sector_counter += 1
    if sector_counter > 1:
        row_num += 1
    for second_symbol in range(1, row_num + 1):
        if second_symbol % 2 == 0:
            for third_symbol in range(1, seats_num_even_row + 1):
                print(f'{chr(first_symbol)}{second_symbol}{chr(seat)}')
                seat += 1
                counter_seats += 1
        else:
            for third_symbol in range(1, seats_num_odd_row + 1):
                print(f'{chr(first_symbol)}{second_symbol}{chr(seat)}')
                seat += 1
                counter_seats += 1

        seat = 97
print(counter_seats)
