triangle_sides = input('Введите длины трех отрезков через пробел: ').split()
side_1, side_2, side_3 = map(float, triangle_sides)
longest_side = side_1
sum_of_short = side_2 + side_3
if side_2 > longest_side:
    longest_side = side_2
    sum_of_short = side_1 + side_3
if side_3 > longest_side:
    longest_side = side_3
    sum_of_short = side_2 + side_1

if longest_side < sum_of_short:
    if side_1 == side_2 == side_3:
        print('Из пользовательских отрезков можно составить равносторонний треугольник')
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        print('Из пользовательских отрезков можно составить равнобедренный треугольник')
    else:
        print('Из пользовательских отрезков можно составить разносторонний треугольник')
else:
    print('Из пользовательских отрезков составить треугольник нельзя')
