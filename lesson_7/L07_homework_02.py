# -*- coding: utf-8 -*-
"""
1) Напишите функцию count_vowels_in_text(), которая принимает обязательный аргумент строку, а также произвольное количество аргументов.
2) Функция count_vowels_in_text(), должна возвращать словарь, который содержит в себе пары <"буква" : число букв> (например, {'и' : 2, 'ы' : 50, 'н' : 32}
    
3) выведите на экран результат работы программы используя переменную result_text и функцию count_vowels_in_text(). В качестве обязательного аргумента используйте переменную text_italy

            Резульат работы программы:
                
                ЗАДАНИЕ 2.4

                {'а': 30, 'и': 51, 'з': 3}
                --------------------------------------------------
    
"""
text_italy = "Знаменитый русский поэт Александр Блок, побывав в Италии, написал в 1909 году 24 стихотворения об этой удивительной стране, которые вошли в его цикл «Итальянские стихи». Такое же восторженное впечатление об Италии ощущает любой турист, посетивший ее, пусть даже он и не поэт. Древнеримские памятники архитектуры, уникальные дворцы, замки, соборы, музеи с картинами Рафаэля, Боттичелли, Леонардо да Винчи, Тициана, и Микеланджело, великолепные горнолыжные, пляжные и спа курорты привлекают в Италию ежегодно десятки миллионов туристов."

def count_vowels_in_text(string, *args):
    #vowels = 'ауоыиэяюёе'
    a_count = 0
    u_count = 0
    o_count = 0
    y_count = 0
    i_count = 0
    e_count = 0
    ya_count = 0
    yu_count = 0
    yo_count = 0
    ye_count = 0
    result = {}
    for word in string:
        word = word.lower()
        #vow_count = 0
        for letter in word:
            if letter == 'а':
                a_count += 1
                result['а'] = a_count
            elif letter == 'у':
                u_count += 1
                result['у'] = u_count
            elif letter == 'о':
                o_count += 1
                result['о'] = o_count
            elif letter == 'ы':
                y_count += 1
                result['ы'] = y_count
            elif letter == 'и':
                i_count += 1
                result['и'] = i_count
            elif letter == 'э':
                e_count += 1
                result['э'] = e_count
            elif letter == 'я':
                ya_count += 1
                result['я'] = ya_count
            elif letter == 'ю':
                yu_count += 1
                result['ю'] = yu_count
            elif letter == 'ё':
                yo_count += 1
                result['ё'] = yo_count
            elif letter == 'е':
                ye_count += 1
                result['е'] = ye_count
    for arg in args:
        arg = arg.lower()
        for letter in arg:
            if letter == 'а':
                a_count += 1
                result['а'] = a_count
            elif letter == 'у':
                u_count += 1
                result['у'] = u_count
            elif letter == 'о':
                o_count += 1
                result['о'] = o_count
            elif letter == 'ы':
                y_count += 1
                result['ы'] = y_count
            elif letter == 'и':
                i_count += 1
                result['и'] = i_count
            elif letter == 'э':
                e_count += 1
                result['э'] = e_count
            elif letter == 'я':
                ya_count += 1
                result['я'] = ya_count
            elif letter == 'ю':
                yu_count += 1
                result['ю'] = yu_count
            elif letter == 'ё':
                yo_count += 1
                result['ё'] = yo_count
            elif letter == 'е':
                ye_count += 1
                result['е'] = ye_count
    return result

print(count_vowels_in_text(text_italy, 'что-то')) # {'а': 30, 'е': 40, 'и': 51, 'ы': 12, 'у': 11, 'о': 41, 'э': 4, 'я': 6, 'ю': 3}