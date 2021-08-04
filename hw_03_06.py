"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint
list_to_search = [el + randint(-100, 100) for el in range(20)]
print(f'Изначальный список: {list_to_search}')
# нахожу максимальное значение в списке и его индекс
max_el = max(list_to_search)
idx_max_el = list_to_search.index(max_el)
# нахожу минимальное значение в списке и его индекс
min_el = min(list_to_search)
idx_min_el = list_to_search.index(min_el)
# выясняю, какой элемент стоит в списке раньше - мин или макс
range_min = min(idx_min_el, idx_max_el)
range_max = max(idx_min_el, idx_max_el)
summary = sum(list_to_search[range_min + 1: range_max])
print(f'Минимальное значение: {min_el}, максимальное значение: {max_el}')
print(f'Сумма элементов, находящихся между мин и макс: {summary}')
