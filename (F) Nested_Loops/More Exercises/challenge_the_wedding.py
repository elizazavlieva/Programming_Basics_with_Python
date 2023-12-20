men_num = int(input())
women_num = int(input())
tables_num = int(input())
counter = 0

for man in range(1, men_num + 1):
    for women in range(1, women_num + 1):
        counter += 1
        if counter <= tables_num:
            print(f'({man} <-> {women})', end=' ')
        else:
            break
    if counter > tables_num:
        break
