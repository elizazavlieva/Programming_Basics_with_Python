deposit = float(input())
time = int(input())
interest_rate = float(input()) / 100

result = deposit + time * ((deposit * interest_rate)/12)
print(result)
