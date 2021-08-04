"""
Определить, какое число в массиве встречается чаще всего.
"""
# вариант 1 - простой, если несколько чисел встречаются одинаковое количество раз, будет выведено одно из них
from random import randint
list_to_search = [el + randint(-100, 100) for el in range(500)]
max_count = 0
most_frequent = list_to_search[0]
for el in list_to_search:
    if list_to_search.count(el) > max_count:
        max_count = list_to_search.count(el)
        most_frequent = el
print(f'Чаще всего в списке встречается число: {most_frequent} ({max_count} повт.)')

# вариант 2 - если в массиве несколько чисел, подпадающих под условие задания, выводятся они все
max_count = 0
frequency = {}
most_frequent = []
for el in list_to_search:
    frequency[el] = list_to_search.count(el)
for el in list_to_search:
    if list_to_search.count(el) > max_count:
        max_count = list_to_search.count(el)
for key, value in frequency.items():
    if value == max_count:
        most_frequent.append(key)

print(f'Чаще всего в списке встречается число: {most_frequent} ({max_count} повт.)')