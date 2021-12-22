# -*- coding: utf-8 -*-
"""
1. Создайте функцию format_time(), которая в качестве аргументов принимает 3 аргумента: час, минута, секунда, разделитель (по умолчанию ":")
2. Функция format_time() должна возвращать время в формате:
        13:25:47
3. Вызовите функцию format_time() три раза, использовав разный разделитель.
"""

def format_time(hour, minutes, seconds, sep=':'):
    if minutes < 10:
        return str(hour) + sep + '0' + str(minutes) + sep + str(seconds)
    elif seconds < 10:
        return str(hour) + sep + str(minutes) + sep + '0' + str(seconds)
    elif seconds < 10 and minutes < 10:
        return str(hour) + sep + '0' + str(minutes) + sep + '0' + str(seconds)
    return str(hour) + sep + str(minutes) + sep + str(seconds)

print(format_time(13, 13, 30))
print(format_time(13, 13, 30, '/'))
print(format_time(13, 13, 30, '-'))
print(format_time(13, 13, 30, ' '))