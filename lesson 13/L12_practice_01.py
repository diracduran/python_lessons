# -*- coding: utf-8 -*-
# L12_practice_01.py
"""
1. Используя концепцию Инкапсуляции создайте класс Building (постройка), которая описывает строение. Значением по умолчанию должен служить параметр on_sale = False. Также при создании экземпляра Класса Building, необходимо учесть атрибуты:
        price (цена)
        city (город)
        address (адрес)
2. Напишите 2 метода:
    1) place_on_sale - который изменяет  атрибут on_sale на True
    2) remove_on_sale - который изменяет  атрибут on_sale на False
3. Смена полей должна сопровождаться сообщением:
    Постройка выставлена на продажу (on_sale = True)
    Постройка снята с продажи (on_sale = False)
4. Напишите метод, который выводит информацию о постройке на экран в том случае, только если она на продаже.
    Продажа:
    Цена: <price>
    Город: <city>
    Адрес: <address>

    Если же нет, то сообщение "Не продается".
"""

class Building:
    def __init__(self, price, city, address):
        self.price = price
        self.city = city
        self.address = address
        self.on_sale = False
    
    def place_on_sale(self):
        self.on_sale = True
        print('Постройка выставлена на продажу')
    def remove_on_sale(self):
        self.on_sale = False
        print('Постройка снята с продажи')
    def show_on_sale(self):
        if self.on_sale == True:
            print(f'Продажа: \n\t Цена: {self.price} \n\t Город: {self.city} \n\t Адрес: {self.address}')
        else:
            print('Не продается :<')

building = Building(1000000, 'Москва', 'Осенний б-р')
building.place_on_sale()
building.show_on_sale()
building.remove_on_sale()
building.show_on_sale()