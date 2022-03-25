# -*- coding: utf-8 -*-
# the2nd_l01_01_practice.py
"""
Используя библиотеку requests и метод get получить список из 7 шуток с сайта https://icanhazdadjoke.com
Данные необходимо получить используя 1 запрос, то есть нужно изучить документацию API в разделе Search for dad jokes
Данные сохранить в список jokes и вывести все шутки на экран. 
"""
from pip._vendor import requests

URL = 'https://icanhazdadjoke.com/'

HEADERS = {'Accept': 'application/json'}

res = requests.get(URL, headers=HEADERS)

json_res = res.json()

jokes_dict = {k: v for k, v in json_res.items()}

jokes = [joke for joke in jokes_dict if joke == jokes_dict['joke']][:8]

print("Задание 1:\n" + "\n".join(jokes))
