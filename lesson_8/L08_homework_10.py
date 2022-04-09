"""
У вас есть число и нужно определить какая цифра из этого числа является наибольшей.

Входные данные: Положительное целое число.

Выходные данные: Целое число (0-9).

Пример:

max_digit(0) == 0
max_digit(52) == 5
max_digit(634) == 6
max_digit(1) == 1
max_digit(10000) == 1
"""

def max_digit(number: int) -> int:
    num_str = str(number)
    max = 0
    for num in num_str:
        if int(num) > max:
            max = int(num)
    return max
    


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")