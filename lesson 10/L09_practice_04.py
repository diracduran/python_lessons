# -*- coding: utf-8 -*-
# L09_practice_04.py
"""
1. Создайте текстовый файл my_short_bio_2.txt, который будет содержать 3 строки:

    1) Ваша Фамилия Имя и Отчество

    2) Город, в котором живете

    3) Ваши увлечения (не более трех)
2. Прочитайте ранее созданный файл my_short_bio_2.txt, используя метод readlines(), который сохранит результат в список my_bio_list
3. Выведите на экран Ваши увлечения в формате: «Мои увлечения: <Ваши увлечения>»
"""
with open('d:\\study_projects\\python_lessons\\lesson 10\\txt_files\\my_short_bio2.txt', encoding='utf-8') as f:
    my_bio_list = f.readlines() # ['1) Романова Е. Е.\n', '\n', '2) Мск\n', '\n', '3) python, react']
    print(my_bio_list)
    print('Мои увлечения: ', my_bio_list[4])