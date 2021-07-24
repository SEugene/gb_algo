from random import randint, uniform
user_range_int = input('Введите через пробел границы диапазона для генерации случайного целого числа: ')
user_range_flt = input('Введите через пробел границы диапазона для генерации случайного вещественного числа: ')
user_range_chr = input('Введите через пробел границы диапазона для генерации случайной буквы английского алфавита: ')

r_int_1, r_int_2 = map(int, user_range_int.split())
f_int_1, f_int_2 = map(float, user_range_flt.split())
ch_int_1, ch_int_2 = user_range_chr.split()

print(f'Случайное целое число в заданном диапазоне - {randint(r_int_1, r_int_2)}')
print(f'Случайное вещественное число в заданном диапазоне - {uniform(f_int_1, f_int_2):.2f}')
print(f'Случайная буква английского алфавита в заданном диапазоне - {chr(randint(ord(ch_int_1), ord(ch_int_2)))}')
