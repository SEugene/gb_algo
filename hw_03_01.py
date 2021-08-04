"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9
"""

list_1 = [el for el in range(2, 100)]
list_2 = [el for el in range(2, 10)]
result = {}

for digit in list_2:
    counter = 0
    for number in list_1:
        if number % digit == 0:
            counter += 1
    result[digit] = counter

print(result)
