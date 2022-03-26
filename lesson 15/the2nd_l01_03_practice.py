# -*- coding: utf-8 -*-
# the2nd_l01_03_practice.py
"""
Используя библиотеку requests и метод get необходимо программу для получения изображений, используя pixabay API

1) Программа должна запросить у пользователя категорию изображения - <category> (обязательно учесть отказ от использования категории для получения случайной категории изображения)
2) Далее программа должна запросить у пользователя условие поиска - <q> (также учесть отказ от поиска - случайное изображение)
3) Сам запрос реализовать в виде функции с двумя обязательными аргументами category и q - get_image(category, q)
4) Программа должна работать до тех пор пока пользователь не захочет ее прервать (использовать цикл while) и логику также реализовать в виде функции - collect_images()
P.S. if __name__ == '__main__' - информацию можно узнать перейдя по ссылке:

https://zen.yandex.ru/media/id/5bbcd4ab48032300ab7460a6/chto-delaet-if-name--main-v-python-5eb5731aa19aea5aa92fdcf5
"""
from tkinter.messagebox import QUESTION
from pip._vendor import requests

def get_image(category, q):
    pass

def collect_images():
    while True:
        break


if __name__ == '__main__':
    CATEGORIES = ['fashion', 'nature', 'backgrounds', 'science', 'education', 'people', 'feelings', 'religion', 'health', 'places', 'animals', 'industry', 'food', 'computer', 'sports', 'transportation', 'travel', 'buildings', 'music']

    question = input('Choose category. Or enter "random". ')
    flag = False
    if question in CATEGORIES or question == 'random':
        flag = True
        collect_images()
