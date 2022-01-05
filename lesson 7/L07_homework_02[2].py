# -*- coding: utf-8 -*-
"""
1) Напишите функцию count_vowels_in_text(), которая принимает обязательный аргумент строку text, а также произвольное количество аргументов *letters. В качестве произвольных аргументов *letters функция должна принимать по 1 букве (например, 'а', 'и', 'з'), которые нужно посчитать в обязательном аргументе text.
2) Функция count_vowels_in_text(), должна возвращать словарь, который содержит в себе пары <"буква" : число букв> (например, {'и' : 2, 'ы' : 50, 'н' : 32}
    
3) выведите на экран результат работы программы используя переменную result_text и функцию count_vowels_in_text(). В качестве обязательного аргумента используйте переменную text_italy

            Резульат работы программы:
                
                ЗАДАНИЕ 2.4

                {'а': 30, 'и': 51, 'з': 3}
                --------------------------------------------------
    
"""
text_italy = "Знаменитый русский поэт Александр Блок, побывав в Италии, написал в 1909 году 24 стихотворения об этой удивительной стране, которые вошли в его цикл «Итальянские стихи». Такое же восторженное впечатление об Италии ощущает любой турист, посетивший ее, пусть даже он и не поэт. Древнеримские памятники архитектуры, уникальные дворцы, замки, соборы, музеи с картинами Рафаэля, Боттичелли, Леонардо да Винчи, Тициана, и Микеланджело, великолепные горнолыжные, пляжные и спа курорты привлекают в Италию ежегодно десятки миллионов туристов."




def count_vowels_in_text(string, *letters):
    vow_count = 0
    result = {}
    for word in string:
        word = word.lower()
        for char in word:
            for letter in letters:
                if char == letter:
                    vow_count += 1
                    result[letter] = vow_count

    return result



print(count_vowels_in_text(text_italy, 'п', 'б', 'а')) # {'а': 49, 'п': 47, 'б': 37}
