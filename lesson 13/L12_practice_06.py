# -*- coding: utf-8 -*-
# L12_practice_06.py
"""
1. Создайте классы Horse и Rider. Используйте композицию, чтобы смоделировать лошадь с всадником на ней.
"""
class Horse:
    def __init__(self, name, age, rider):
        self.name = name,
        self.age = age,
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

dirac = Rider('Dirac')
horse = Horse('Sunny', 3, dirac)
