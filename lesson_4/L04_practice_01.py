# -*- coding: utf-8 -*-
"""
1. Имеется список покупок buy_list, состоящий из кортежей ("наименование", стоимость)
2. Выведите наименование покупки и ее стоимость в цикле for
3. Выведите общую стоимость покупок, которую сохраните в переменной summa.
    Пример:
Наименование: хлеб | Цена: 35
Наименование: молоко | Цена: 55
Наименование: вода | Цена: 30
Итого: 120
"""
buy_list = [("хлеб", 35), ("молоко", 55), ("вода", 30)]
summa = 0
# Ваш код ниже

for item in buy_list:
    summa += item[1]
    print('Наименование: ' + item[0] + ' | ' + str(item[1]))
print('Итого: ' + str(summa))