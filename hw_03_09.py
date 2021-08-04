"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import randint
MIN_RANGE = - 100
MAX_RANGE = 100
rows, elements = input('Введите размерность матрицы через пробел (количество столбцов и строк): ').split()
matrix = []
for _ in range(int(rows)):
    matrix.append([el + randint(MIN_RANGE, MAX_RANGE) for el in range(int(elements))])

for idx in range(len(matrix)):
    print(matrix[idx])

mins = []
for row in range(int(elements)):
    min_el = MAX_RANGE * 20
    for col in range(int(rows)):
        if matrix[col][row] < min_el:
            min_el = matrix[col][row]
    mins.append(min_el)

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max(mins)}')
