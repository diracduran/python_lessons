"""
Ваша цель сейчас — создать функцию, которая принимает на вход кортеж и возвращает кортеж из 3 элементов: первого, третьего и второго с конца элементов заданного массива.

пример

Важно отметить, что вам нужно использовать индекс для извлечения элементов из массива. Обратите внимание, нумерация индексов начинается с 0, не с 1. Это означает, что если вы хотите получить первый элемент из массива elements , вам нужен elements[0] , а если второй — elements[1] .

Входные данные: Кортеж длиной не менее 3 элементов.

Выходные данные: Кортеж.

Пример:

easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
easy_unpack((6, 3, 7)) == (6, 7, 3)
"""

def easy_unpack(elements: tuple) -> tuple:
    first_el = elements[0]
    third_el = elements[2]
    negative_index_el = elements[-2]
    new_tuple = (first_el, third_el, negative_index_el)
    return new_tuple

if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')