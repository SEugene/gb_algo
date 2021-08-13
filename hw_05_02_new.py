"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque

HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def sum_hex(x, y):
    # для корректной работы нужно точно понимать, какое число имеет больше разрядов
    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    result = deque()
    transfer = 0
    for _ in range(len(x)):                          # итерируемся по самому длинному элементу
        if y:
            res = HEX_NUM[x.pop()] + HEX_NUM[y.pop()] + transfer
        else:                                        # если элементы во 2 числе закончились
            res = HEX_NUM[x.pop()] + transfer
        transfer = res // 16                         # делим пром.рез-тат на основание, переносим в след.разряд
        result.appendleft(HEX_NUM[res - transfer * 16])
    if transfer:
        result.appendleft(HEX_NUM[transfer])         # добавляем остаток от предыдущей операции в начало итога

    return result


def mult_hex(x, y):
    # запускаем расчет промежуточных результатов умножения, итоги сводим в result_deq, промежуточные результаты
    # не переводим в шестнадцатеричную систему, при последующем суммировании опять переводить - экономим ресурсы
    result_deq = deque()
    y = deque(y)
    for idx in range(len(y)):
        rows = deque()                                 # промежуточный итог умножения
        factor = HEX_NUM[y.pop()]                      # начиная с последнего разряда 2го числа, берем множитель
        for idx_2 in range(len(x)-1, -1, -1):          # проходим по 1му множителю, начиная с его последнего разряда
            rows.appendleft(HEX_NUM[x[idx_2]] * factor)
        for _ in range(idx):                           # добавляем нули в качестве последних разрядов, начиная
            rows.append(0)                             # со 2го промежуточного результата
        result_deq.appendleft(rows)

    # запускаем суммирование элементов очереди result_deq
    result = deque()
    transfer = 0
    for _ in range(len(result_deq[0])):            # итерируемся по самому длинному элементу (рассчитанному последним)
        sum_iter = transfer                        # всегда добавляем к промежуточному итогу остаток от пред.операции
        for itr in range(len(result_deq)):         # суммируем последние элементы каждой из вложенных очередей
            if result_deq[itr]:
                sum_iter += result_deq[itr].pop()
        transfer = sum_iter // 16                  # делим пром.рез-тат на основание, переносим в след.разряд
        result.appendleft(HEX_NUM[sum_iter - transfer * 16])
    if transfer:
        result.appendleft(HEX_NUM[transfer])       # добавляем остаток от предыдущей операции в начало

    return result


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(''.join(a), '+', ''.join(b), '=', ''.join(sum_hex(a, b)))
print(''.join(a), '*', ''.join(b), '=', ''.join(mult_hex(a, b)))
