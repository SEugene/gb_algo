"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
"""
# создаю список из случайных целых чисел
from random import randint
list_to_search = [el + randint(-100, 100) for el in range(20)]
print(f'Изначальный список: {list_to_search}')
# нахожу максимальное значение в списке и его индекс
max_el = max(list_to_search)
idx_max_el = list_to_search.index(max_el)
# нахожу минимальное значение в списке и его индекс
min_el = min(list_to_search)
idx_min_el = list_to_search.index(min_el)

list_to_search.insert(idx_min_el, max_el)         # вставляю на позицию мин значение макс, мин сдвигается вправо на 1
list_to_search.pop(idx_min_el + 1)                # удаляю значение с позиции, на которую сдвинулся мин
list_to_search.insert(idx_max_el, min_el)         # тоже самое провожу с индексом макс и значением мин
list_to_search.pop(idx_max_el + 1)

print(f'Измененный список:  {list_to_search}')
