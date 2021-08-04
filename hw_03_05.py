"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
from random import randint
MIN_RANGE = - 100
MAX_RANGE = 100
list_to_search = [el + randint(MIN_RANGE, MAX_RANGE) for el in range(20)]
max_number = MIN_RANGE * 20         # чтобы стартовое максимальное число было заведомо меньше любого числа в массиве
for el in list_to_search:
    if 0 > el > max_number:
        max_number = el

print(f'Заданный массив: {list_to_search}')
print(f'Максимальный отрицательный элемент: {max_number}')
