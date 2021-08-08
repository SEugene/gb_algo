"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
!!! Для упрощения в этом варианте сравнение убрал, оставил только саму операцию подсчета
!!! В задании 1 использовал модуль time для подсчета времени, в задании 2 - timeit
"""
from time import perf_counter


def time_taken(func, *args, **kwargs):
    # функция для подсчета времени выполнения операции в миллисекундах
    start_time = perf_counter()
    func_res = func(*args, **kwargs)
    fin_time = perf_counter()
    return (fin_time - start_time) * 1000, func_res


def sum_01(limit):
    # рекурсивная функция для подсчета суммы натуральных чисел от 1 до limit
    if limit == 1:
        return 1
    res = sum_01(limit - 1) + limit
    return res


def sum_02(limit):
    # цикл для подсчета суммы натуральных чисел от 1 до limit
    res = 0
    for idx in range(limit + 1):
        res = res + idx
    return res


# вывожу значения времени для нескольких заданных вариантов вместо ввода с клавиатуры
for user_number in (100, 300, 500, 700):
    print(f'Итог суммирования: {time_taken(sum_01, user_number)[1]}, '
          f'время операции в мс: {time_taken(sum_01, user_number)[0]}')
    print(f'Итог суммирования: {time_taken(sum_02, user_number)[1]}, '
          f'время операции в мс: {time_taken(sum_02, user_number)[0]}')

"""
время операции (число - 500) в мс вариант 1: 0.0898, сложность - О(2^n) - рекурсия
время операции (число - 500) в мс вариант 2: 0.0178, сложность - О(n) - проход по циклу
"""
