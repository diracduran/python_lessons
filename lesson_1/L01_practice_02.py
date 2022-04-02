# -*- coding: utf-8 -*-
"""
Используя функцию type() выведите тип данных для следующих значений:
    1) 12.2
    2) "0.0"
    3) "Python"
    4) '''This is an awesome Python tricks'''
    5) [1, 2, 3, 4]
    6) {1, 3, 5}
    7) {"a": 1, "b": 2, "c": 3}
Пример кода: 
print(type(111))
"""
print(type(12.2))  # <class 'float'>
print(type('0.0'))  # <class 'str'>
print(type("Python"))  # <class 'str'>
print(type('''This is an awesome Python tricks'''))  # <class 'str'>
print(type([1, 2, 3, 4]))  # <class 'list'>
print(type({1, 3, 5}))  # <class 'set'>
print(type({"a": 1, "b": 2, "c": 3}))  # <class 'dict'>
