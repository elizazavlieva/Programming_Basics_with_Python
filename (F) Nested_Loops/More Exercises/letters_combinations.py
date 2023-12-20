start = input()
end = input()
exclusive_symbol = input()
counter = 0
start_letter = ord(start)
end_letter = ord(end)
exclusive_letter = ord(exclusive_symbol)

for first_symbol in range(start_letter, end_letter + 1):
    for second_symbol in range(start_letter, end_letter + 1):
        for third_symbol in range(start_letter, end_letter + 1):
            if (first_symbol == exclusive_letter or second_symbol == exclusive_letter) \
                    or third_symbol == exclusive_letter:
                pass
            else:
                counter += 1
                print(f'{chr(first_symbol)}{chr(second_symbol)}{chr(third_symbol)}', end=' ')
print(counter, end= '')
