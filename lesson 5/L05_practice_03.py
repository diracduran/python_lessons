# -*- coding: utf-8 -*-
"""
1. Дан словарь month_dict, который содержит пары "месяц": <порядковый номер>
2. Добавьте в словарь month_dict недостающие пары месяцев (ключи) и их порядковые номера (значения)
3. Выведите сожержимое словаря month_dict на экран.
"""
month_dict = {"January": 1, "April": 4, "May": 5, "July": 7, "September": 9, "November": 11}

month_dict['February'] = 2
month_dict['March'] = 3
month_dict['June'] = 6
month_dict['August'] = 8
month_dict['October'] = 10
month_dict['December'] = 12

print("сожержимое словаря month_dict:\n", month_dict)