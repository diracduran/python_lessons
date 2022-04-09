# -*- coding: utf-8 -*-
# L10_homework_01.py
"""
1. В директории reports должны лежать отчеты с файлами расширения .txt, которые хранят данные о пользователях посетивших веб-приложение в формате:
<username>,<device>
где username - имя пользователя
device - устройсво, с которого зашел пользователь (Chrome, Mozilla, Safari, Edge, iOS, Android - все возможные варианты)
!!! P.S. чтобы обратиться файлам внутри директории укажите имя директории и имя файла, например:
    reports/1.txt
2. По задумке разработчика, отчет формируется 10 раз за месяц и имена файлов имеют названия r1.txt, r2.txt, ..., r10.txt
НО ИНОГДА РАЗРАБОТЧИК ЗАБЫВАЕТ ВЫЛОЖИТЬ ОТЧЕТ И НЕКОТОРЫЕ ФАЙЛЫ МОГУТ ОТСУТСТВОВАТЬ
3. Необходимо обработать отчеты (с условием возможного отсутствия файлов) и составить ежемесячный отчет в формате csv:
username;Chrome;Mozilla;Safari;Edge;iOS;Android;
johny;5;2;1;3;10;15;
"""

import csv


headers = [
    'username',
    'Chrome',
    'Mozilla',
    'Safari',
    'Edge',
    'iOS',
    'Android'
]

filenames = [
    'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\r1.txt',
    'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\r2.txt',
    'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\r3.txt',
    'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\r4.txt',
    'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\r5.txt',
    'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\r6.txt',
    'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\r7.txt',
    'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\r8.txt',
    'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\r9.txt',
    'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\r10.txt'
    ]

report = 'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\reports\\report.csv'


def read_files(fnames):
    chrome_count = 0
    mozilla_count = 0
    safari_count = 0
    edge_count = 0
    ios_count = 0
    android_count = 0
    for fname in fnames:
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                data = f.readlines()
        except:
            print('file not found')
        else:
            data_list = [d.replace('\n', '').split(',') for d in data]
            with open(report, 'w', encoding='utf-8') as r:
                writer = csv.writer(r, delimiter=',')
                writer.writerow(headers)

                for d in data_list:
                    username = d[0]
                    if d[1] == 'Chrome':
                        chrome_count += 1
                    elif d[1] == 'Mozilla':
                        mozilla_count += 1
                    elif d[1] == 'Safari':
                        safari_count += 1
                    elif d[1] == 'Edge':
                        edge_count += 1
                    elif d[1] == 'iOS':
                        ios_count += 1
                    elif d[1] == 'Android':
                        android_count += 1
                    
                    row = [username, chrome_count, mozilla_count, safari_count, edge_count, ios_count, android_count]

                    writer.writerow(row)


read_files(filenames)