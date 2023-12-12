import sys

prev_num = -sys.maxsize

while True:
    user_input = input()
    current_num = 0
    if user_input == 'Stop':
        print(prev_num)
        break
    else:
        current_num = int(user_input)
    if current_num > prev_num:
        prev_num = current_num
     

