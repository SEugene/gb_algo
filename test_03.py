point_1 = input('Введите координаты первой точки через пробел: ')
point_2 = input('Введите координаты второй точки через пробел: ')
x1, y1 = map(float, point_1.split())
x2, y2 = map(float, point_2.split())
k = (y1 - y2) / (x1 - x2)
if y2 - k * x2 > 0:
    print(f'Функция: y = {k:.2f}*x + {y2 - k * x2:.2f}')
else:
    print(f'Функция: y = {k:.2f}*x - {abs(y2 - k * x2):.2f}')


