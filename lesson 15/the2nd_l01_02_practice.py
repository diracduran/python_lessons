# -*- coding: utf-8 -*-
# the2nd_l01_02_practice.py
"""
Используя библиотеку requests и метод get получить список из 7 шуток с сайта https://icanhazdadjoke.com
Данные необходимо получить используя 1 запрос, то есть нужно изучить документацию API в разделе Search for dad jokes
Данные сохранить в список jokes и вывести все шутки на экран.
Описанное выше задание полностью соответствует заданию pybc_l01_01.py

Из полученных данных необходимо сохранить 7 изображений в формате .png
Названия изображений должны полностью соответствовать id шутки.
"""
from pip._vendor import requests

URL = 'https://icanhazdadjoke.com/'


HEADERS = {'Accept': 'application/json'}

res = requests.get(URL, headers=HEADERS)

data = res.json()

jokes = []

for joke in data['results']:
    jokes.append(joke['joke'])
    PNG_PATH = f"j/{joke['id']}.png"
    png_res = requests.get(URL + PNG_PATH)
    png_content = png_res.content

    png_item = PNG_PATH + '.png'

    with open(f'd:\\study_projects\\python_lessons\\lesson_15\\jokes_pngs\\{png_item}', 'wb', encoding='utf-8') as f:
        f.write(png_content)




print("Задание 2:\n" + "Все изображения успешно сохранены")
