# -*- coding: utf-8 -*-
# L09_practice_01.py
"""
1. Создайте текстовый файл full_name.txt, который в одну строку будет содержать Ваше Фамилию Имя и Отчество.
2. С помощью функции open() откройте созданный файл full_name.txt и выведите его содержимое на экран.
"""

# 1-й способ

opened_file = open('d:\\study_projects\\python_lessons\\lesson 10\\txt_files\\full_name.txt', encoding='utf-8')
read_file = opened_file.read()
print(read_file) # Романова Елизавета Евгеньевна
opened_file.close()

#2-й способ

with open('d:\\study_projects\\python_lessons\\lesson 10\\txt_files\\full_name.txt', encoding='utf-8') as f:
    print(f.read()) # Романова Елизавета Евгеньевна