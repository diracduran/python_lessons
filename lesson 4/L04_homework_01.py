# -*- coding: utf-8 -*-
"""
1. Используя вложенный цикл (nested loops) и функцию range() создайте таблицу умножения чисел от 2 до 9.
2. Само умножение от 1 до 10 для каждого числа.
    Пример:
        УМНОЖЕНИЕ ЧИСЛА 2:
            2 Х 1 = 2
            2 Х 2 = 4
            2 Х 3 = 6
            2 Х 4 = 8
            2 Х 5 = 10
            2 Х 6 = 12
            2 Х 7 = 14
            2 Х 8 = 16
            2 Х 9 = 18
            2 Х 10 = 20
            ------------------
        УМНОЖЕНИЕ ЧИСЛА 3:
            3 Х 1 = 3
            3 Х 2 = 6
            3 Х 3 = 9
            3 Х 4 = 12
            3 Х 5 = 15
            3 Х 6 = 18
            3 Х 7 = 21
            3 Х 8 = 24
            3 Х 9 = 27
            3 Х 10 = 30
            ------------------
    и так далее...............
"""
for i in range(2, 10, 1):
    print('УМНОЖЕНИЕ ЧИСЛА ' + str(i) + ':')
    for j in range(1, 11, 1):
        print(str(i) + ' * ' + str(j) + ' = ' + str(i*j))
    print('-'*18)