# -*- coding: utf-8 -*-
"""
Задача 1 (int --> str).
Стоимость за аренду офиса в месяц rent_monthly = 15000.
Рассчитайте стоимость годовой аренды (* 12 месяцев) в переменной rent_annum
Выведите на экран сообщение в формате:
    'Стоимость аренды офиса 15000 рублей / мес (180000 рублей / год)'
"""
rent_monthly = 15000
rent_annual = rent_monthly * 12
print('Стоимость аренды офиса ' + str(rent_monthly) + ' рублей / мес ' + '(' + str(rent_annual) + ' рублей / год' + ')') # Стоимость аренды офиса 15000 рублей / мес (180000 рублей / год)


"""
Задача 2 (str --> int, float).
Даны две переменные в разных типах:
epoch = "2000" # эпоха
offset = 19 # год
Используя print() и приведение типов вычислите какой сейчас год путем сложения epoch + offset
Ответ: 2019
"""
epoch = "2000" # эпоха
offset = 19 # год
print(int(epoch) + offset) # 2019
