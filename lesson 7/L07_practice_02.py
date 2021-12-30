# -*- coding: utf-8 -*-
# L07_practice_02.py
"""
1. Создайте функцию animal_profile(), которая будет возвращать данные о животном в виде словаря profile = {}
2. В качестве аргументов функции используйте два обязательных аргумента: «Вид», «Цвет»
3. Остальные аргументы создать с помощью произвольного количества пар «ключ-значение» (**kwargs) (это может быть возраст, кличка и так далее)
4. Создайте не менее двух разных животных (animal_1, animal_2 ...), используя функцию animal_profile()
5. Выведите содержимое созднанных переменных на экран.
"""

def animal_profile(species, color, **additional_data):
    profile = {}
    profile['species'] = species
    profile['color'] = color
    profile['additional_data'] = additional_data
    return profile

animal_1 = print(animal_profile('собака', 'рыжий', name='Марта', age=5))
animal_1 = print(animal_profile('кошка', 'белая с чёрными пятнышками', name='Муся', age=15))
animal_1 = print(animal_profile('кот', 'коричневый в пятнышку и полоску', name='Юлиан', age=1, personality='ласковый хулиган'))