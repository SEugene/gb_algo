"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9
"""
from sys import getsizeof
from time import perf_counter
# Вариант 1. Как было реализовано в задании 1 к уроку 3
start_time = perf_counter()
list_1 = [el for el in range(2, 100)]
list_2 = [el for el in range(2, 10)]
result = {}

for digit in list_2:
    counter = 0
    for number in list_1:
        if number % digit == 0:
            counter += 1
    result[digit] = counter

print('Вариант 1')
print(result)
print('Размер объектов программы в байтах: ', getsizeof(list_1) + getsizeof(list_2) + getsizeof(result))    # 1384
print('Время выполнения в мс: ', (perf_counter() - start_time) * 1000)                                      # 0.11 mc

# Вариант 2. Списки list_1 и list_2 не создаем, прямо в цикле прописываем генератор
# Итого минус 2 списка по 40+8*100 + 40+8*10 байт (у меня 64-битная Windows) - 360 байт против 1384 байт
# Из-за того, что в Варианте 1 числа от 2 до 99 хранятся в списке, а в Варианте 2 приходится 10 раз их нерерировать,
# Вариант 2 более затратен по времени выполнения - 0.20 мс против 0.11 мс в Варианте 1. Чудес не бывает...

start_time = perf_counter()
result = {}
for digit in (el for el in range(2, 10)):
    counter = 0
    for number in (el for el in range(2, 100)):
        if number % digit == 0:
            if number % digit == 0:
                counter += 1
        result[digit] = counter

print('\nВариант 2')
print(result)
print('Размер объектов программы в байтах: ', getsizeof(result))                                              # 360
print('Время выполнения в мс: ', (perf_counter() - start_time) * 1000)                                        # 0.20 mc
