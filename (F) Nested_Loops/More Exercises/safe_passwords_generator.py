a = int(input())
b = int(input())
max_passwords = int(input())
counter = 0
first_and_last_symbol = 35
second_and_fifth_symbol = 64

for x in range(1, a + 1):
    for y in range(1, b + 1):
        counter += 1
        if counter > max_passwords:
            break
        if first_and_last_symbol > 55:
            first_and_last_symbol = 35
        if second_and_fifth_symbol > 96:
            second_and_fifth_symbol = 64
        print(f'{chr(first_and_last_symbol)}{chr(second_and_fifth_symbol)}{x}{y}'
              f'{chr(second_and_fifth_symbol)}{chr(first_and_last_symbol)}', end='|')
        first_and_last_symbol += 1
        second_and_fifth_symbol += 1
