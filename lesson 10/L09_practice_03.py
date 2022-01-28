# -*- coding: utf-8 -*-
# L09_practice_03.py
"""
1. Создайте текстовый файл my_short_bio.txt, который будет содержать 3 строки:

    1) Ваша Фамилия Имя и Отчество

    2) Город, в котором живете

    3) Ваши увлечения (не более трех)
2. Прочитайте ранее созданный файл my_short_bio.txt, используя метод readline()
3. Сохраните результат в переменную my_bio_by_line.
4. Выведите на экран содержимое переменной my_bio_by_line.
"""

with open('d:\\study_projects\\python_lessons\\lesson 10\\txt_files\\my_short_bio.txt', encoding='utf-8') as f:
    bio_by_line = f.readline() # 1) Ваша Фамилия Имя и Отчество
    print(bio_by_line)