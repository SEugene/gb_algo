"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, то надо вывести число 6843.
"""
user_number = int(input('Введите натуральное число: '))
user_number_list = []
while user_number > 0:      # разбиваю введенное число на цифры, в список цифры записываются "с конца" числа
    digit = user_number % 10
    user_number_list.append(digit)
    user_number = user_number // 10
if len(user_number_list) > 0:
    user_number_list = [el for el in user_number_list]    # собираю итоговое число через list comprehension
    print(int(''.join(map(str, user_number_list))))
else:
    print('Вспомни математику - отрицательное число не может быть натуральным!!!!!')