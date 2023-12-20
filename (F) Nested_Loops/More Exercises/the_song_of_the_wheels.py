m = int(input())
counter = 0
summary = 0
a = 0
b = 0
c = 0
d = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                summary = i * j + k * l
                if i < j and k > l and summary == m:
                    print(f'{i}{j}{k}{l}', end=' ')
                    counter += 1
                    if counter == 4:
                        a = i
                        b = j
                        c = k
                        d = l
print()
if counter >= 4:
    print(f'Password: {a}{b}{c}{d}')
else:
    print('No!')
