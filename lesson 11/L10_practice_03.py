# -*- coding: utf-8 -*-
# L10_practice_03.py
"""
1. Напишите программу, которая ведет журнал посещений в цикле while
2. Поля журнала посещений: Имя, Фамилия, Возраст, Документ, Номер
3. Все записи сохранить с файле visit_log.csv после выхода из цикла while (можно реализовать любым способом)
P.S. Файл csv можно создать любым способом...
"""
import csv


filename = 'd:\\study_projects\\python_lessons\\lesson 11\\hw_files\\visit_log.csv'

headers=['name', 'surname', 'age', 'document', 'number']

with open(filename, 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(headers)

    while True:
        print('Журнал посещений')
        name = input('Имя: ')
        surname = input('Фамилия: ')
        age = input('Возраст: ')
        document = input('Документ: ')
        number = input('Номер: ')

        row = [name, surname, age, document, number]
        writer.writerow(row)

        question = input('Хотите продолжить? ')
        if question == 'нет':
            break