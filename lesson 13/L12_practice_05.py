# -*- coding: utf-8 -*-
# L12_practice_05.py
"""
1. Используя концепцию Наследия напишите класс-родитель Building, с атрибутами: price (цена), city(город), address (адрес)
2. Далее создайте 2 класса-потомка Flat и House.
3. Используя функцию super(), определите все параметры класса-родителя для каждого из класса-потомка.
4. Добавьте собственные атрибуты каждому классу-потомку:
    Flat: rooms (количество комнат), square (площадь), floor (этаж)
    House: rooms (количество комнат), square (площадь), floors (количество этажей), lot_square (площадь участка), garage (гараж есть или нет True / False)
5. В каждом классе-потомке создайте метод detail_info(), который отобразит Полную информацию об объекте (то есть все атрибуты)
6. В каждом классе-потомке создайте метод change_price(new_price), который будет изменять цену объекта
"""

class Building:
    def __init__(self, price, city, address):
        self.price = price
        self.city = city
        self.address = address

class Flat(Building):
    def __init__(self, price, city, address, rooms, square, floor):
        super().__init__(price, city, address)
        self.rooms = rooms
        self.square = square
        self.floor = floor
    
    def detail_info(self):
        print(f'Квартира! Цена: {self.price}. Город: {self.city}. По адресу: {self.address}, кол-во комнат: {self.rooms}, площадь: {self.square}.')

    def change_price(self, new_price):
        self.price = new_price

flat = Flat(4000000, 'Сочи', 'Гагарина д.10', 3, 234, 7)
flat.detail_info()
flat.change_price(5000000)
flat.detail_info()

class House(Building):
    def __init__(self, price, city, address, rooms, square, floors, lot_square, garage):
        super().__init__(price, city, address)
        self.rooms = rooms
        self.square = square
        self.floors = floors
        self.lot_square = lot_square
        self.garage = garage

    
    def detail_info(self):
        print(f'Дом! Цена: {self.price}, площадь: {self.square}, кол-во комнат: {self.rooms}, кол-во этажей: {self.floors}, площадь участка: {self.lot_square}.')
        if self.garage == True: print('\tЕсть гараж.')
        else: print('\tГаража нет.')

    def change_price(self, new_price):
        self.price = new_price


house = House(10000000, 'Сочи', 'Земляничная, д.5', 7, 398, 2, 450, True)
house.detail_info()
house.change_price(25000000)
house.detail_info()