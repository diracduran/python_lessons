# -*- coding: utf-8 -*-
# L09_practice_07.py
"""
1. Напишите программу, которая в цикле while будет сохранять построчно введенные данные в текстовый файл noties.txt
2. Программа после внесения данных должна спросить продолжить или нет?
3. В случае нет - закройте файл и завершите цикл while.
4. В случае продолжить - продолжайте, но имейте в виду, что каждая запись в файле должна быть с новой строки. 
"""

file = 'd:\\study_projects\\python_repos\\python_lessons\\lesson 10\\txt_files\\noties.txt'

with open(file, mode='a', encoding='utf-8') as f:
    while True:
        type_smt = input('напишите что-нибудь. ')
        f.write(type_smt + '\n')
        question = input('хотите продолжить? ')
        if question.lower() == 'нет':
            break