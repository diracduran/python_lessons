# -*- coding: utf-8 -*-
# L12_practice_03.py
"""
1. Используя концепцию Полиморфизм создайте 3 класса геометрических фигур:
    Circle - круг, обязательный аргумент radius
    Rectangle - прямоугольник, обязательные аргументы width, lenght
    Triangle - треугольник, обязательные аргументы - стороны a, b, c
2. Для каждой фигуры создайте 2 метода:
    1) perimetr - который возвращает значение периметра
    2) square - который возвращает значение площади

P.S.
Формулы для расчета периметра:
    Круг - 2 * pi * r, где pi = 3.14, r - радиус
    Прямоугольник - 2 * (w + l), где w - ширина, l - длина
    Треугольник - a + b + c, где a,b,c - стороны треугольника
Формулы для расчета площади:
    Круг - pi * r ** 2, где pi = 3.14, r - радиус
    Прямоугольник - w * l, где w - ширина, l - длина
    Треугольник - sqrt(p*(p-a)*(p-b)*(p-c)), где a,b,c - стороны треугольника, p - периметр, sqrt - корень квадратный
Для использования квадратного корня:
    from math import sqrt
    
"""
from math import sqrt


pi = 3.14

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimetr(self):
        return 2 * pi * self.radius

    def square(self):
        return pi * self.radius ** 2

circle = Circle(6)
print('circle:')
print(f'perimetr: {circle.perimetr()}')
print(f'square: {circle.square()}')
print('')

class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def perimetr(self):
        return 2 * (self.width + self.lenght)

    def square(self):
        return self.width * self.lenght

rectangle = Rectangle(4,8)
print('rectangle')
print(f'perimetr: {rectangle.perimetr()}')
print(f'square: {rectangle.square()}')
print('')

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr()
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

triangle = Triangle(5,8,2)
print('triangle')
print(f'perimetr: {triangle.perimetr()}')
print(f'square: {triangle.square()}')