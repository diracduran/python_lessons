"""
Попробуйте выяснить какое количество нулей содержит данное число в конце.

Входные данные: Положительное целое число (int).

Выходные данные: Целое число (int).

Пример:

end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
"""

def end_zeros(num: int) -> int:
    string_num = str(num)
    zeros = len(string_num) - len(string_num.rstrip('0'))
    return zeros


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")