start = int(input())
end = int(input())
magic_num = int(input())
counter = 0
is_not_combination = True
for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter += 1
        if i + j == magic_num:
            print(f'Combination N:{counter} ({i} + {j} = {magic_num})')
            is_not_combination = False
            break
    if i + j == magic_num:
        break
if is_not_combination:
    print(f'{counter} combinations - neither equals {magic_num}')
    