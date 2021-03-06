"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
from random import randint
from heapq import nlargest
M = 30
list_to_search = [randint(-100, 100) for _ in range(2 * M + 1)]

# Для нахождения медианы отбираем М + 1 наибольших элементов, минимальный из них и будет медианой
print(f'Медиана числового ряда из {2 * M + 1} элемента: {min(nlargest(M + 1, list_to_search))}')
