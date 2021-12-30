# -*- coding: utf-8 -*-
# L07_practice_09.py
"""
1. Дан список целых чисел numbers.
2. В списке numbers найдите минимальное число c помощью цикла for. Вам необходимо создать функцию find_min(lst), которая принимает список (lst), а возвращает целое число (минимальное из списка). Ответ сравните со встроенной функцией min(list).
3. В списке numbers найдите максимальное число c помощью цикла for. Вам необходимо создать функцию find_max(lst), которая принимает список (lst), а возвращает целое число (максимальное из списка). Ответ сравните со встроенной функцией max(list).
4. В списке numbers найдите сумму вcех чисел помощью цикла for. Вам необходимо создать функцию find_sum(lst), которая принимает список (lst), а возвращает целое число (сумму чисел из списка). Ответ сравните со встроенной функцией sum(list).
5. Используя встроенную функцию enumerate, найдите сумму только четных элементов списка numbers (индексы 0, 2, 4 ...). Создайте функцию sum_even_index_numbers(lst)
    
"""
numbers = [-22, 0, 13, -7, 42, -33, 17, 26, 8, 1, -9]

def find_min(lst):
    min_num = lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
    return min_num

def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

def find_sum(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum

def sum_even_index_numbers(lst):
    sum = 0
    for i, num in enumerate(lst):
        if i % 2 == 0:
            sum += num
    return sum

print('find_min(lst):', find_min(numbers))
print('min(lst):', min(numbers), '\n')

print('find_max(lst):', find_max(numbers))
print('max(lst):', max(numbers), '\n')

print('find_sum(lst):', find_sum(numbers))
print('sum(lst):', sum(numbers), '\n')

print('sum_even_index_numbers(lst):', sum_even_index_numbers(numbers))