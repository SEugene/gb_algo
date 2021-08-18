"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
from random import uniform


def merge(left, right):
    """
    Функция, выполняющая сравнение двух частей массива и заполняющая результирующий массив по возрастанию
    """
    left_cur, right_cur = 0, 0
    merged = []
    while left_cur < len(left) and right_cur < len(right):
        # Сравниваем по одному элементу из левой и правой стороны, в итоговый массив помещаем тот, который меньше
        # Счетчик увеличиваем на 1 по той стороне, из которой элемент занесен в итог, чтобы не сравнивать его
        # повторно
        if left[left_cur] <= right[right_cur]:
            merged.append(left[left_cur])
            left_cur += 1
        else:
            merged.append(right[right_cur])
            right_cur += 1

    # служит для дозаполнения результирующего массива значениями, которые остались после выхода из предыдущего цикла
    for left_cur in range(left_cur, len(left)):
        merged.append(left[left_cur])
    for right_cur in range(right_cur, len(right)):
        merged.append(right[right_cur])

    return merged


def merged_sort(ar):
    # точка "разворота" рекурсии - когда достигается разбиение массива из N элементов на N массивов по 1-му элементу,
    # функция начинает "обратное" движение
    if len(ar) <= 1:
        return ar

    # рекурсивное разделение массива пополам с двух сторон
    middle = len(ar) // 2
    left, right = merged_sort(ar[:middle]), merged_sort(ar[middle:])

    # сортировка и обратное объединение, начиная с N массивов по 1-му элементу до массива из N элементов
    return merge(left, right)


array_to_sort = [round(uniform(0, 50)) for _ in range(8)]

print(array_to_sort)
print(merged_sort(array_to_sort))
