"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint


def bubble_sort(array):
    for idx in range(1, len(array)):
        counter = 0
        for idx_2 in range(len(array) - idx):
            if array[idx_2] > array[idx_2 + 1]:
                array[idx_2], array[idx_2 + 1] = array[idx_2 + 1], array[idx_2]
                counter += 1
        if counter == 0:
            break
    return array


array_to_sort = [randint(-100, 100) for _ in range(15)]
print(f'Первоначальный  массив: {array_to_sort}')
print(f'Отсротированный массив: {bubble_sort(array_to_sort)}')
