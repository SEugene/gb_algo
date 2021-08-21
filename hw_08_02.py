"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter


class MyNode:                                         # создаем класс "узел"
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(phrase):
    """
    Построение дерева для кодирования по алгоритму Хаффмана
    """
    # получаем список из пар буква - частота, отсортированный по убыванию частот
    letters_counter = Counter(phrase).most_common(len(phrase))

    while len(letters_counter) > 1:
        weight = letters_counter[0][1] + letters_counter[1][1]
        node = MyNode(left=letters_counter.pop()[0], right=letters_counter.pop()[0])         # формируем "узел"

        # Вставка пары "узел, вес" на нужное место в список
        for idx, item in enumerate(letters_counter):
            if weight > item[1]:
                continue
            else:
                letters_counter.insert(idx, (node, weight))
                break
        letters_counter.append((node, weight))

    return letters_counter[0][0]


code_table = {}


def haffman_code(tree, path=''):
    """
    Составление таблицы кодирования по дереву
    """

    if not isinstance(tree, MyNode):
        code_table[tree] = path
    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


string_to_code = 'Prowler is running'

# Формирование таблицы кодирования
haffman_code(haffman_tree(string_to_code))

for i in string_to_code:
    print(code_table[i], end=' ')
