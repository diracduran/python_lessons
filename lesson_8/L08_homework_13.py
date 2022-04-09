"""
Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').

Входные данные: Строка.

Выходные данные: Массив строк.

Пример:

split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']
1
2
Предварительное условие: 0<=len(str)<=100
"""

def split_pairs(a):
    b = []
    if len(a)%2 == 1:
        a += '_'
    for i in range(0, len(a), 2):
        b.append(a[i : i + 2])
    return b
        


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")