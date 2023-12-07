import math
record_sec = float(input())
distance = float(input())
sec_per_meter = float(input())

total_time = distance * sec_per_meter
delay = math.floor(distance / 15) * 12.5

total_time += delay
diff = abs(record_sec - total_time)

if total_time < record_sec:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')
