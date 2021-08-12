"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque


def sum_hex(x, y):
    HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0                                                   # остаток, который переносим в следующий разряд

    if len(y) > len(x):                                            # первым должно идти число с большим числом рязрядов
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:
        if y:
            res = HEX_NUM[x.pop()] + HEX_NUM[y.pop()] + transfer
        else:
            res = HEX_NUM[x.pop()] + transfer
        transfer = 0
        if res < 16:
            result.appendleft(HEX_NUM[res])
        else:
            result.appendleft(HEX_NUM[res - 16])                     # если результат от сложения больше основания (16),
            transfer = 1                                             # оставляем разницу между результатом и основанием,
    if transfer:                                                     # добавляем к следующему разряду 1
        result.appendleft('1')
    return list(result)


num_1 = list(input('Введите 1-е шестнадцатиричное число: ').upper())
num_2 = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(*num_1, '+', *num_2, '=', *sum_hex(num_1, num_2))
