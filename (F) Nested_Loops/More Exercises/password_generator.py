n = int(input())
l = int(input())
third_symbol = 97 + l
for first_symbol in range(1, n + 1):
    for second_symbol in range(1, n+1):
        for x in range(97, third_symbol):
            for y in range(97, third_symbol):
                for z in range(1, n + 1):
                    if z > first_symbol and z > second_symbol:
                        print(f'{first_symbol}{second_symbol}{chr(x)}{chr(y)}{z}', end=' ')
