# -*- coding: utf-8 -*-
# L12_practice_04.py
"""
1. Используя концепцию Наследия напишите класс-родитель Building, с атрибутами: price (цена), city(город), address (адрес)
2. Далее создайте 2 класса-потомка Flat и House.
3. Для каждого потомка создайте метод advertise(), который выводит сообщение об объекте:
    Пример для квартиры:
        Продается Квартира! Цена: 4000000. Город: Сочи. По адресу: Гагарина д.10
    Пример для дома:
        Продается Дом! Цена: 10000000. Город: Сочи. По адресу: Земляничная, д.5
"""

class Building:
    def __init__(self, price, city, address):
        self.price = price
        self.city = city
        self.address = address

class Flat(Building):
    def __init__(self, price, city, address):
        super().__init__(price, city, address)

    def advertise(self):
        print(f'Продается Квартира! Цена: {self.price}. Город: {self.city}. По адресу: {self.address}')

flat = Flat(4000000, 'Сочи', 'Гагарина д.10')
flat.advertise()

class House(Building):
    def __init__(self, price, city, address):
        super().__init__(price, city, address)

    def advertise(self):
        print(f'Продается Дом! Цена: {self.price}. Город: {self.city}. По адресу: {self.address}')

house = House(10000000, 'Сочи', 'Земляничная, д.5')
house.advertise()