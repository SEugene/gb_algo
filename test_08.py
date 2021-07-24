user_year = int(input('Введите год для анализа: '))
if not user_year % 4:
    if not user_year % 400 or user_year % 100:
        print("Год високосный")
    else:
        print('Год невисокосный')
else:
    print('Год невисокосный')
