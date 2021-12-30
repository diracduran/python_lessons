# -*- coding: utf-8 -*-
# L07_practice_01.py
"""
1. Создайте функцию my_memories(), которая в качестве позиционного аргумента будет использовать год (year), а в качестве произвольного набора аргументов (*args) Ваши воспоминания за указанный год
2. Функция должна осуществлять вывод на экран сообщения в виде:

«Коротко, о воспоминаниях YEAR года:», 
 «воспоминание 1»

«воспоминание 2»

«воспоминание 3»
3. Вызовите функцию my_memories() не менее трех раз
"""

def my_memories(year, *memories):
    print('Коротко, о воспоминаниях ' + str(year) + ' года:')
    for memory in memories:
        print('воспоминание ' + str(memories.index(memory) + 1) + ': \n\t' + memory)  
    print(' ')


my_memories(2020, 'закончила уник')
my_memories(2021, 'нашла работу', 'получила первую зп', 'появился кот')