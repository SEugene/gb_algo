user_number = int(input('Enter an integer positive three-digit number: '))
if user_number // 1000 == 0 and user_number > 0:
    digit_1 = user_number // 100
    digit_2 = user_number // 10 % 10
    digit_3 = user_number % 10
    print(f'The sum of the entered number digits is {digit_1 + digit_2 + digit_3} '
          f'and the product is {digit_1 * digit_2 * digit_3}')
else:
    print('Wrong number. You were to enter an integer positive three-digit number')
