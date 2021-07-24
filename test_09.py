user_numbers = input('Введите три числа через пробел: ').split()
num_1, num_2, num_3 = map(float, user_numbers)
if num_1 > num_2:
    if num_1 < num_3:
        average_number = num_1
    elif num_2 > num_3:
        average_number = num_2
    else:
        average_number = num_3
elif num_2 < num_3:
    average_number = num_2
elif num_1 > num_3:
    average_number = num_1
else:
    average_number = num_3
print(average_number)
