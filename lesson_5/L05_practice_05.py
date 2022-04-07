# -*- coding: utf-8 -*-
"""
1. Дан словарь month_dict. В нем перепутаны ключи и значения.
2. Приведите пары в словаре month_dict к единому формату:
    "Месяц": <порядковый номер>
3. Удалите лишние пары ключ-значение в словаре month_dict.
3. Выведите содержимое словаря month_dict на экран.
"""

month_dict = {"January": 1, 2 : "February", 3: "March", "April": 4, "May": 5, "June": 6, 7: "July", "August": 8, "September": 9, 10: "October", "November": 11, 12: "December"}
month_dict['February'] = 2
month_dict['March'] = 3
month_dict['July'] = 7
month_dict['October'] = 10
month_dict['December'] = 12

del month_dict[2]
del month_dict[3]
del month_dict[7]
del month_dict[10]
del month_dict[12]

print("Отредактированный словарь month_dict:\n", month_dict)
