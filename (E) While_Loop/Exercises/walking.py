total_steps = 0
while True:
    steps = input()
    if steps == 'Going home':
        steps_to_home = int(input())
        total_steps += steps_to_home
        diff = abs(total_steps - 10000)
        break
    current_steps = int(steps)
    total_steps += current_steps
    diff = abs(total_steps - 10000)
    if total_steps >= 10000:
        break

if total_steps >= 10000:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')