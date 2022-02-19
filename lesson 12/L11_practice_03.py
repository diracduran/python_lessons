# -*- coding: utf-8 -*-
# L11_practice_03.py
"""
1. Создайте класс Dog, который будет обладать 2 атрибутами name - кличка и age - возраст и описывать Собаку.
2. В имеющийся класс Dog(), добавьте два метода:
    1) show_details(), который выводит на экран информацию о собаке в формате: «Кличка: <кличка>. Возраст: <возраст>»
    2) sit_down(), который выводит на экран информацию о том, что собака выполнила команду сидеть: «<кличка> сейчас сидит!»
3. Создайте экземпляр класса Dog() в переменной pretty_dog
4. Примените два метода show_details() и sit_down() к экземпляру pretty_dog
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        return f'Кличка: {self.name}. Возраст: {self.age}'
    def sit_down(self):
        return f'{self.name} сейчас сидит'

pretty_dog = Dog('Марта', 6)
print(pretty_dog.show_details())
print(pretty_dog.sit_down())