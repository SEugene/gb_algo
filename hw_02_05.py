"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""
for row in range(10):
    res_dict = {}
    for idx in range(32+row*10, 42+row*10):   # вывожу по 10 пар в строке
        if idx <= 127:                        # 127 - верхняя граница диапазона по условию задания
            res_dict[idx] = chr(idx)
        else:
            break
    print(res_dict)
