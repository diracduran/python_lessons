# -*- coding: utf-8 -*-
"""
1. Ниже написан код ИГРЫ "УГАДАЙ ЧИСЛО"
2. Измените, код игры так, чтобы использовать другой признак завершения
    Пример:
       Введите число от 1 до 20:

           15
           Загаданное число меньше, чем 15
           Введите число от 1 до 20:
               
               7
               Загаданное число меньше, чем 7
               Введите число от 1 до 20:
                   
                   2
                   Загаданное число меньше, чем 2
                   Введите число от 1 до 20:

                       1
                       Вы угадали, это число: 1
                       Вам понадобилось 4 попытка (-ок) 
"""
"""
Игра: «Угадай число»
Компьютер загадывает число в диапазоне от 1 до 20
Задача игрока угадать число за меньшее количество попыток
При неверно введенном числе должна выводиться подсказка (больше число или меньше)
При угадывании числа вывести сообщение о завершении игры
"""
import random # встроенный модуль для генерации случайных чисел

guess_number = random.randint(1, 20) # случайное число от 1 до 20

attempts = 1 # число попыток
while True:
    print("Введите число от 1 до 20:")
    user_number = int(input())
    if user_number == guess_number:
        print("Вы угадали, это число: " + str(user_number))
        print("Вам понадобилось "  + str(attempts) + " попытка (-ок)")
        break
    elif user_number > guess_number:
        print("Загаданное число меньше, чем "  + str(user_number))
    elif user_number < guess_number:
        print("Загаданное число больше, чем "  + str(user_number))
    attempts = attempts + 1
