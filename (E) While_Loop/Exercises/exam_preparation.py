limit_fail_grades = int(input())
count = 0
last_task = ''
fail_grades = 0
total_grades = 0
while True:
    task_name = input()
    if task_name == 'Enough':
        average_score = total_grades / count
        print(f'Average score: {average_score:.2f}\n'
              f'Number of problems: {count}\n'
              f'Last problem: {last_task}')
        break
    grade = int(input())
    count += 1
    if grade <= 4:
        fail_grades += 1
    last_task = task_name
    total_grades += grade
    if fail_grades >= limit_fail_grades:
        print(f'You need a break, {fail_grades} poor grades.')
        break
