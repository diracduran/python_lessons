# -*- coding: utf-8 -*-


# the2nd_l07_12_practice
"""
1. Дан API, генерирующий случайного человека (https://pipl.ir/v1/getPerson).
2. В переменную data сохранены 10 случайных людей.
3. Используя min и lambda, найдите самого младшего человека. Сохраните его в переменную min_age_person и выведите на экран.
4. Используя max и lambda, найдите самого высокого человека ('height'). Сохраните его в переменную max_height_person и выведите на экран.
* 5. Используя reduce, lambda и любые другие функции найдите среднюю зарплату ('salary') для всех полученных людей. Сохраните его в переменную average_salary и выведите на экран.
"""

from pip._vendor import requests
from functools import reduce
from pprint import pprint
BASE_URL = "https://pipl.ir/v1/getPerson"

data = [requests.get(BASE_URL).json() for i in range(10)]
pprint(data)

# Ваш код здесь
min_age_person = {}
print("min_age_person")
pprint(min_age_person)

print("max_height_person")
max_height_person = {}
pprint(max_height_person)

print("average_salary")
average_salary = 0 / len(data)
print(average_salary)
