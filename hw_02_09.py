"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
его цифр.
"""


def count_sum(user_number):                         # Функция для суммирования цифр в натуральном числе
    res_list = []
    while user_number > 0:
        result = user_number % 10
        res_list.append(result)
        user_number //= 10
    return sum(res_list)


print('Введите натуральные числа в последовательность по одному или введите "Q" для завершения ввода')
idx = 1
number_list = []
while True:                                          # Решил немного усложнить задачу - пользователь вводит
    number = input(f'{idx}: ')                       # несколько натуральных чисел на свое усмотрение
    if number.lower() == 'q':                        # завершенние ввода - символ Q
        break
    number_list.append(abs(int(number)))             # регистр символа Q не важен
    idx += 1

max_num = 0
max_num_sum = 0
for iterator in range(len(number_list)):
    if count_sum(number_list[iterator]) > max_num_sum:
        max_num_sum = count_sum(number_list[iterator])
        max_num = number_list[iterator]

print(f'Наибольшее число по сумме цифр во введенной последовательности - {max_num},\n'
      f'Сумма его цифр - {max_num_sum}')
