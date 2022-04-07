# -*- coding: utf-8 -*-
# L10_practice_07.py
"""
1. Напишите программу, которая в цикле запрашивает два числа и выполняет операцию деления первого на второе
2. В случае ошибки выводится сообщение об ошибке
3. В случае отсутствия ошибки выводится результат
4. В конце программа спрашивает: продолжить? (нет - выход из программы, отсальное продолжить)
P.S.!!! НЕОБХОДИМО использовать конструкцию try-except-else-finally
Введите первое число: qwerewr
Введите второе число: 3
Что-то пошло не так...
Продолжить? (введите 'нет' для выхода)
"""
while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
    except:
        print('Что-то пошло не так :<')
    else:
        print('Результат: ', a / b)
    finally:
        question = input('Продолжить? ')
        if question == 'нет':
            break