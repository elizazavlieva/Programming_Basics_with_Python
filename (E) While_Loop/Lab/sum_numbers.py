summary = int(input())
current_sum = 0

while True:
    num = int(input())
    current_sum += num
    if summary <= current_sum:
        print(current_sum)
        break
        