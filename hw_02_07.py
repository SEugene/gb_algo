"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


# рекурсивная функция для подсчета суммы натуральных чисел от 1 до limit
# сделал для тренировки навыка написания рекурсивных функций, цикл здесь эффективнее, так как
# если limit > 998 функция выбрасывает ошибку "RecursionError: maximum recursion depth exceeded in comparison"
def summary(limit):
    if limit == 1:
        return 1
    res = summary(limit-1) + limit
    return res


# abs - на случай, если пользователь введет отрицательное число
user_number = abs(int(input('Введите любое натуральное число: ')))
print(f'Итог суммирования: {summary(user_number)} \n'
      f'Итог сравнения способов суммирования: {summary(user_number) == user_number*(user_number+1)/2}')
