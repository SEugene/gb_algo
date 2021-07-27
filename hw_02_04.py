"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""
iterations = int(input('Введите количество итераций: '))
result = 1
res_dict = {1: result}
for idx in range(1, iterations):
    result = - result / 2
    res_dict[idx + 1] = result
summary = sum(res_dict.values())
print(f'Числовой ряд: {res_dict}')
print(f'Сумма элементов ряда: {summary}')
