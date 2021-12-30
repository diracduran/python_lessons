# -*- coding: utf-8 -*-
# L07_practice_04.py
"""
1. Дана функция generate_password(), которая генерирует случайные пароли.
2. Данная функция испоьзует встроенный в Python модель random и использует функции randint и choice:
    randint(x,y) --> z, принимает целые числа x, y (где y >= x) и возвращает случайное число
    choice(list) --> element, принимает список или строку или кортеж и возвращает случайный элемент принимаемого списка
3. Используя <Импортирование всего модуля> отредактируйте функцию generate_password, обращаясь к функциям модуля random --> choice и randint
P.S. в комментариях вида # Ваш код здесь указано, какой аргумент в строке принимает функция
"""
# Ваш код ниже
import random

def generate_password(s=6, f=12):
    symbols = "!@#$%^&*()-_=+/.,;:"
    letters = "qwertyuiopasdfghjklzxcvbnm"
    digits = "1234567890"
    randomizer = [symbols, letters, digits]
    password = ''
    password_length = random.randint(s, f)
    for i in range(password_length):
        random_symbol = random.choice(randomizer)
        one_symbol = random.choice(random_symbol)
        password += one_symbol
    return password

print(generate_password())

