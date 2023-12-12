prime_sum = 0
non_prime_sum = 0
while True:
    user_input = input()
    if user_input == 'stop':
        print(f'Sum of all prime numbers is: {prime_sum}\n'
              f'Sum of all non prime numbers is: {non_prime_sum}')
        break
    number = int(user_input)
    if number < 0:
        print('Number is negative.')

    else:
        current_number_is_prime = True
        for i in range(2, number):
            if number % i == 0:
                current_number_is_prime = False
                break
        if current_number_is_prime:
            prime_sum += number
        else:
            non_prime_sum += number
