"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
user_number = int(input('Введите натуральное число: '))
user_number_list = []
while user_number > 0:   # разбиваю введенное число на цифры, записываю цифры в список
    digit = user_number % 10
    user_number_list.append(digit)
    user_number = user_number // 10
if len(user_number_list) > 0:
    odd_num = [el for el in user_number_list if el % 2 != 0]    # вытаскиваю нечетные цифры
    even_num = [el for el in user_number_list if el % 2 == 0]   # вытаскиваю четные цифры
    print(f'Количество нечетных цифр во введенном числе - {len(odd_num)} ({sorted(odd_num)})')
    print(f'Количество нечетных цифр во введенном числе - {len(even_num)} ({sorted(even_num)})')
else:
    print('Вспомни математику - отрицательное число не может быть натуральным!!!!!')
