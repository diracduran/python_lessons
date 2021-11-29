# -*- coding: utf-8 -*-
"""
Даны переменные:
    first_name, middle_name, last_name, full_name, message
1. В переменную first_name сохраните Выше имя
2. В переменную middle_name сохраните Ваше отчество
3. В переменную last_name сохраните Вашу фамилию
4. Подсчитайте количество букв:
    в имени (first_name);
    в отчестве (middle_name);
    в фамилии (last_name);
    всего;
5. В переменную full_name сохраните Ваше ФИО из переменных first_name, middle_name, last_name
6. Примените методы lower(), upper(), title() и capitzlize() к full_name и выведите на экран
"""

# Ваш код ниже
first_name = "Елизавета"
middle_name = "Евгеньевна"
last_name = "Романова"
print("Количество букв в имени:", len(first_name))
print("Количество букв в отчестве:", len(middle_name))
print("Количество букв в фамилии:", len(last_name))
print("Общее количество букв в ФИО:", len(first_name)+len(middle_name)+len(last_name))
full_name = last_name + " " + first_name + " " + middle_name
print(full_name)
print("full_name lower -->", full_name.lower())
print("full_name upper -->", full_name.upper())
print("full_name title -->", full_name.title())
print("full_name capitalize -->", full_name.capitalize())
