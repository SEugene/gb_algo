"""
Определить, какое число в массиве встречается чаще всего.
"""
# вариант 1 - простой, если несколько чисел встречаются одинаковое количество раз, будет выведено одно из них
from random import randint
from collections import Counter
from sys import getsizeof
from time import perf_counter

start_time = perf_counter()
list_to_search = [el + randint(-100, 100) for el in range(500)]
max_count = 0
most_frequent = list_to_search[0]
for el in list_to_search:
    if list_to_search.count(el) > max_count:
        max_count = list_to_search.count(el)
        most_frequent = el

print('Вариант 1')
print(f'Чаще всего в списке встречается число: {most_frequent} ({max_count} повт.)')
print('Размер объектов программы в байтах: ', getsizeof(list_to_search) +
      getsizeof(max_count) + getsizeof(most_frequent))                                                  # 4320
print('Время выполнения в мс: ', (perf_counter() - start_time) * 1000)                                  # 2.5 mc

# вариант 2 - используем коллекцию Counter, вместо создания списка используем генератор прямо в Counter
# убрали 2 переменных (max_count и most_frequent), убрали список, убрали цикл
# в итоге сократили требуемый объем памяти с 4320 байт до 64 байт
# при этом сократили и время с 2,5 мс до 0,57 мс, в первую очередь за счет отказа от цикла

start_time = perf_counter()
print('\nВариант 2')
print(f'Чаще всего в списке встречается число: {Counter(list_to_search).most_common(1)[0][0]} '
      f'({Counter(list_to_search).most_common(1)[0][1]} повт.)')
print('Размер объектов программы в байтах: ',
      getsizeof(Counter(el + randint(-100, 100) for el in range(500)).most_common(1)))                   # 64
print('Время выполнения в мс: ', (perf_counter() - start_time) * 1000)                                   # 0.57 mc
