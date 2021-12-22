# -*- coding: utf-8 -*-
"""
1) Напишите функцию common_elements(), которая принимает 2 аргумента (два разных списка)
2) Функция common_elements() должна возаращать новый список, который содержит в себе общие элементы. Например, даны 2 списка
    list_1 = ['python', 'windows', 'linux', 'macOS']
    list_2 = ['python', 'JavaScript', 'HTML', 'linux']
    
    result_list = ['python', 'linux']

3) выведите на экран результат работы программы используя переменную result_common и функцию common_elements(). В качестве аргументов используйте списки cars_1, cars_2

            Резульат работы программы:
                
                ['bmw', 'lexus']
                --------------------------------------------------
"""
cars_1 = ['bmw', 'mercedes', 'lexus', 'mazda'] # для проверки
cars_2 = ['lexus', 'opel', 'bmw', 'kia', 'volvo'] # для проверки

def common_elements(list1, list2):
    result = []
    for el1 in list1:
        for el2 in list2:
            if el1 == el2:
                result.append(el1)
    print(result)

common_elements(cars_1, cars_2)