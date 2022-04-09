# -*- coding: utf-8 -*-
# L09_practice_06.py
"""
1. Напишите программу, которая будет сохранять введенную пользователем информацию в файл user_text.txt
"""
file = 'd:\\study_projects\\python_repos\\python_lessons\\lesson 10\\txt_files\\user_text.txt'

with open(file, mode='w', encoding='utf-8') as f:
    my_info = input('напишите что-нибудь. ')
    f.write(my_info)