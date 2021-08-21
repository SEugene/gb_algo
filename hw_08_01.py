"""
Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""
import hashlib

string = 'abrakadabra'
result = set()
string = string.lower()                 # приводим данные к условию задачи - строчные латинские буквы

# проходим по строке, формируя подстроки от первой буквы до последней последовательно, по завершении начинаем со второй
# до последней и так далее...
# использование мнодества позволяет исключить дубляжи хэшей
for idx_1 in range(len(string)):
    for idx_2 in range(idx_1+1, len(string) + 1):
        result.add(hashlib.sha1(string[idx_1:idx_2].encode('utf-8')).hexdigest())

print(f'Количество уникальных подстрок в строке "{string}", не считая пустую строку и строку целиком:'
      f' {len(result) - 1}')