# -*- coding: utf-8 -*-
# L10_practice_04.py
"""
1. Дан файл "_countries.csv".
2. Прочитайте его любым способом.
3. Напишите программу, которая открывает файл "_countries.csv" и сохраняет все страны (на русском языке) в другой файл "countries.json"
"""
import csv
import json


filename = 'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\_countries.csv'
json_filename = 'd:\\study_projects\\python_repos\\python_lessons\\lesson 11\\hw_files\\_countries.json'

with open(filename, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    data = []
    i = 1
    for row in reader:
        country = ','.join(row).split(',')[i]
        print(country)
        data.append(country)

with open(json_filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
