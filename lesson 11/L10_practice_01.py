# -*- coding: utf-8 -*-
# L10_practice_01.py
"""
1. Напишите функцию word_stat, которая принимает список из слов (строки str) и имя файла. Внутри функция сохраняет результат в виде списка словарей в файл json. 
2. Каждый словарь - это:
    {"слово из списка": ({"гласные": 5}, {"согласные": 8})}
3. Результат сохраняется в файл L10_practice_01.json
4. Список слов для проверки words.
5. гласные - vowels, согласные - consonants
"""
import json


words = ['sea', 'belt', 'garbage', 'river', 'house', 'school', 'boomerang', 'constructor', 'python', 'JavaScript', 'train']
vowels = 'aeuoiy'
consonants = 'qwrtpsdfghjklzxcvbnm'
filename = 'd:\\study_projects\\python_lessons\\lesson 11\\hw_files\\L10_practice_01.json'

def word_stat(some_list, fname):
    for word in some_list:
        vow_count = 0
        cons_count = 0
        for letter in word.lower():
            if letter in vowels:
                vow_count += 1
            if letter in consonants:
                cons_count += 1
        res = {
            word: ({
                'гласные': vow_count
            }, {
                'согласные': cons_count
            })
        } # {"train": [{"гласные": 2}, {"согласные": 3}]} - ИСПРАВИТЬ!!!
    
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False)


word_stat(words, filename)