"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
"""
enterprises_number = int(input('Введите количество предприятий: '))
enterprises = {}
for idx in range(enterprises_number):
    name, profit_1, profit_2, profit_3, profit_4 = input('Введите наименование предприятия и прибыль за 4 квартала'
                                                         ' поквартально, все данные - через пробел: ').split()
    enterprises[name] = {
                        #'name': name,
                        'profit_1': float(profit_1),
                        'profit_2': float(profit_2),
                        'profit_3': float(profit_3),
                        'profit_4': float(profit_4),
                        'average': (float(profit_1) + float(profit_2) + float(profit_3) + float(profit_4)) / 4
                        }
sum_all = 0
for names in enterprises:
    sum_all += enterprises[names]['average']

max_profit = 0
for names_2 in enterprises:
    if enterprises[names_2]['average'] > max_profit:
        max_profit = enterprises[names_2]['average']

more = [enterprises[names_3]['average'] for names_3 in enterprises
        if enterprises[names_3]['average'] > sum_all / len(enterprises)]
less = [enterprises[names_3]['average'] for names_3 in enterprises
        if enterprises[names_3]['average'] < sum_all / len(enterprises)]

more_names = []
less_names = []
for keys, values in enterprises.items():
    if values['average'] in more:
        more_names.append(keys)
    elif values['average'] in less:
        less_names.append(keys)

print(f'Предприятия с прибылью, выше среднего значения: {more_names}')
print(f'Предприятия с прибылью, ниже среднего значения: {less_names}')
