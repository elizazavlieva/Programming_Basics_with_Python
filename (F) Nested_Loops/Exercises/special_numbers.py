n = int(input())
is_special = False
counter = 0
for num in range(1111, 10000):
    number = str(num)
    for index, digit in enumerate(number):
        symbol = int(digit)
        if symbol == 0:
            break
        else:
            if n % symbol == 0:
                counter += 1
                if counter == 4:
                    is_special = True
                else:
                    is_special = False
    counter = 0
    if is_special:
        print(num, end=' ')