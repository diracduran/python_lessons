# the2nd_l07_10_practice
"""
1. Напишите заглавными буквами все имена домашних животных списка my_pets и распечатайте список, используя map.

2. Объедините 2 списка my_strings и my_numbers в список кортежей, но отсортируйте числа от самого низкого до самого высокого, используя zip и sorted.

3. Отфильтруйте баллы списка scores, которые превышают 50%, используя filter.

4. Объедините все числа, которые находятся в списке в этом файле, используя reduce (my_numbers and scores). Какова общая сумма?
"""

from functools import reduce

#1 Напишите заглавными буквами все имена домашних животных и распечатайте список, используя map.
my_pets = ['sisi', 'bibi', 'titi', 'carla']
upper_pets = list(map(lambda x: x.upper(), my_pets))
print(upper_pets) # ['SISI', 'BIBI', 'TITI', 'CARLA']


#2 Объедините 2 списка в список кортежей, но отсортируйте числа от самого низкого до самого высокого, используя zip и sorted.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()

united_tuples = sorted(zip(tuple(my_strings), tuple(my_numbers)))
print(united_tuples) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]


#3 Отфильтруйте баллы, которые превышают 50%, используя filter.
scores = [73, 20, 65, 19, 76, 100, 88]
filtered_scores = list(filter(lambda x: x > 50, scores))
print(filtered_scores) # [73, 65, 76, 100, 88]

#4 Объедините все числа, которые находятся в списке в этом файле, используя reduce (my_numbers and scores). Какова общая сумма?
united_numbers = reduce(lambda x,y: x+y, (my_numbers + scores)) 
print(united_numbers) # 456