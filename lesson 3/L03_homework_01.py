# -*- coding: utf-8 -*-
"""
SHOPPING
1. Дан список игр доступных для покупки items, элементами которого являются кортежи содержащие два элемента:
    первый элемент - название игры
    второй элемент - стоимость игры
2. Дан баланс (balance), на который Вы можете расчитывать при покупках.
3. Переменная my_shop_list - пустой список.
4. Переменная total_cost - общая стоимость выбранных игр
5. Выберите 3 любых игры (индексы сохраните в переменные first, second, third) из списка items и сохраните только название игры в список my_shop_list, если стоимость игры не превышает ваш баланс (balance)
Имейте ввиду, что баланс должнен уменьшаться после каждой покупки
6. Выведите список покупок my_shop_list  и общую стоимость total_cost на экран и общее количество купленных игр.
"""
items = [("PS4 игра Sony Человек-паук", 1349), ("PS4 игра Sony God of War", 1999),("PS4 игра Sony Detroit: Стать человеком", 1349),("PS4 игра Sony Одни из нас. Обновленная версия (Хиты PlayStation", 990), ("PS4 игра Sony Uncharted 4: Путь вора (Хиты PlayStation)", 990),("PS4 игра Sony Дожить до рассвета (Хиты PlayStation)", 990),  ("PS4 игра Sony Знание - сила: Эпохи", 690), ("PS4 игра Sony Gran Turismo Sport", 1349), ("PS4 игра Sony Жизнь После", 2590), ("PS4 игра Sony ASTRO BOT Rescue Mission (только для PS VR)", 1340),("PS4 игра Sony Gravity Rush 2", 1340)]

balance = 5000
my_shop_list = []
total_cost = 0
# Ваш код ниже
first = 0
second = 5

total_cost = items[first][1] + items[second][1]
# 1-я покупка
print('1-я покупка')
if total_cost > balance:
    print('\tне хватает денег :<')   
elif total_cost < balance:
    print('\tигры ваши :>')
    my_shop_list.append(items[first])
    my_shop_list.append(items[second])
    print("\tосталось: " + str(balance - total_cost) + ' р. можете купить ещё игр')

else:
    print('\tденьги кончились :<')
print('ваши покупки: ' + my_shop_list[0][0] + ', ' + my_shop_list[1][0])

# 2-я покупка
print('2-я покупка')
if balance - total_cost > 0:

    third = 10
    total_cost += items[third][1]

    if total_cost < balance:
        my_shop_list.append(items[third])
        print('\tигры ваши :>')
        print('\tосталось: ' + str(balance - total_cost) + ' р. можете купить ещё игр')
    elif total_cost > balance:
        print('\tне хватает денег :<')
    else:
        print('\tденьги кончились :<')
print('ваши покупки: ' + my_shop_list[0][0] + ', ' + my_shop_list[1][0] + ', ' + my_shop_list[2][0])
# 3-я покупка
print('3-я покупка')
if balance - total_cost > 0:

    fourth = 4
    total_cost += items[fourth][1]

    if total_cost < balance:
        my_shop_list.append(items[fourth])
        print('\tигры ваши :>')
        print('\tосталось: ' + str(balance - total_cost) + ' р.')
    elif total_cost > balance:
        print('\tне хватает денег :<')
    else:
        print('\tденьги кончились :<')

print('ваши покупки: ' + my_shop_list[0][0] + ', ' + my_shop_list[1][0] + ', ' + my_shop_list[2][0]+ ', ' + my_shop_list[3][0])