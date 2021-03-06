# -*- coding: utf-8 -*-
# L12_practice_08.py
"""
1. Создайте класс Square так, чтобы когда вы выводите объект Square, выводилось сообщение с длинами всех четырех сторон фигуры. Например, если вы создадите квадрат при помощи Square(13) и осуществите вывод, Python должен вывести строку 13 на 13 на 13 на 13.
    square = Square(13)
    print(square) --> 13 на 13 на 13 на 13
"""

class Square:
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'{self.a} на {self.a} на {self.a} на {self.a}'

square = Square(13)
print(square) # 13 на 13 на 13 на 13
