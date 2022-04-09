# -*- coding: utf-8 -*-
"""
1. Напишите функцию count_word_len(), которая будет принимать в качестве аргумента список слов и возвращать словарь, в котором ключ - слово из списка, значение - количество букв в слове. 
"""

def count_word_len(list):
    result = {}
    for word in list:
        result[word] = len(word)
    return result

items = ['кукла', 'песок', 'юла', 'ведёрко', 'мяч']
print(count_word_len(items))