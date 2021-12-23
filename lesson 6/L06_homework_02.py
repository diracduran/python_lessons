# -*- coding: utf-8 -*-
"""
1) Напишите функцию count_vowel(), которая принимает список в качестве аргумента.
2) Действием функции count_vowel() является подсчет гласных букв в элементе из списка, переданного в функцию.
3) Используйте гласные буквы: а, о, и, е, ю, я, ы, у, э, ё.
4) Функция count_vowel(), должна возвращать СЛОВАРЬ, который содержит в себе пары <"слово" : число гласных букв>
    
5) выведите на экран результат работы программы используя списки seawords и names, и функцию count_vowel().

            Резульат работы программы:
                

                seawords: {'море': 2, 'лодка': 2, 'корабль': 2, 'моряк': 2, 'удочка': 3, 'шторм': 1, 'краб': 1, 'палуба': 3, 'рак': 1, 'прилив': 2, 'океан': 3, 'акула': 3, 'медуза': 3, 'дельфин': 2, 'рыбак': 2, 'подлодка': 3, 'осминог': 3, 'капитан': 3, 'причал': 2}

                names: {'Иван': 2, 'Степан': 2, 'Анна': 2, 'Алёна': 3, 'Игорь': 2}
                --------------------------------------------------
    

"""
seawords = ["море", "лодка", "корабль", "моряк", "удочка", "шторм", "краб", "палуба", "рак", "прилив", "океан", "акула", "медуза", "дельфин", "моряк", "рыбак", "подлодка", "осминог", "капитан", "причал"]
names = ["Иван", "Степан", "Анна", "Алёна", "Игорь"]

def count_vowel(list):
    #vowels = 'ауоыиэяюёе'
    result = {}
    for word in list:
        vow_count = 0
        word = word.lower()
        for letter in word:
            if letter in 'ауоыиэяюёе':
                vow_count += 1
        result[word] = vow_count
    print(result)

count_vowel(names)
count_vowel(seawords)