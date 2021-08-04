"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
matrix = []
for row in range(4):
    rows = []
    for el in range(4):
        rows.append(float(input('Введите элемент матрицы: ')))
    rows.append(sum(rows))
    matrix.append(rows)

for idx in range(len(matrix)):
    print(matrix[idx])
