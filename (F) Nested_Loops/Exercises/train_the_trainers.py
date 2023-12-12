sum_rate = 0
average_rate = 0
average_rate_per_presentation = 0
total_rate = 0
count = 0
jury_num = int(input())
while True:
    presentation_name = input()
    if presentation_name == 'Finish':
        average_rate = total_rate / count
        print(f'Student\'s final assessment is {average_rate:.2f}.')
        break
    for grade in range(1, jury_num + 1):
        rate = float(input())
        sum_rate += rate
        count += 1
    total_rate += sum_rate
    average_rate_per_presentation = sum_rate / jury_num
    print(f'{presentation_name} - {average_rate_per_presentation:.2f}.')
    sum_rate = 0
    