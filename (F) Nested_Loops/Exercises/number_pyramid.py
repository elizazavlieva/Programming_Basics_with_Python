num = int(input())
count = 1
for i in range(1, num + 1):
    for j in range(1, i + 1):
        if count > num:
            break
        print(f'{count} ', end='')
        count += 1
    if count > num:
        break
    print()