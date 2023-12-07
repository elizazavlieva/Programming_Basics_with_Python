hours = int(input())
minutes = int(input()) + 15

if minutes <= 45:
    if minutes < 10:
        print(f'{hours}:0{minutes}')
    else:
        print(f'{hours}:{minutes}')

elif minutes > 45:
    if minutes <= 59:
        print(f'{hours}:{minutes}')
    else:
        hours += 1
        if hours > 23:
            hours = hours - 24
        minutes = minutes - 60
        if minutes < 10:
            print(f'{hours}:0{minutes}')
        else:
            print(f'{hours}:{minutes}')
