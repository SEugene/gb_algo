"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
user_length = abs(int(input('Введите количество чисел в последовательности: ')))
# abs + int - гарантируют ввод неотрицательного целого числа

# цикл используется для устранения возможной ошибки - ввод не цифры, а числа
while True:
    digit_to_find = abs(int(input('Введите цифру для поиска: ')))
    if digit_to_find < 10:
        break

print(f'Введите числа в последовательность по одному (всего чисел - {user_length})')
number_list = [float(input(f'{iterator + 1}: ')) for iterator in range(user_length)]  # Формирование последовательности
result = 0
for idx in range(user_length):
    result = result + int(str(number_list[idx]).count(str(digit_to_find)))
print(f'Сколько раз в заданной последовательности ({number_list}) встречается искомая цифра ({digit_to_find})?\n'
      f' Ответ: {result}')
