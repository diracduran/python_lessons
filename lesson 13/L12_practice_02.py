# -*- coding: utf-8 -*-
# L12_practice_02.py
"""
1. Используя концепцию абстракции, создайте Класс User описывающий ползователя современного сайта.
2. Обязательно инкапсулируйте параметр is_active = True / False (характеризующий активна ли учетная запись или нет)
P.S. Подумайте какие именно атрибуты необходимы для авторизации, для восстановления пароля, для обращения к самому пользователю.
3. Создайте метод в классе User - show_details, который выводит на экран всю информацию о пользователе, если он активен.
4. Если он не активен, то выводить сообщение - "Учетная запись не активна".
5. Также создайте метод изменяющий информацию о статусе активности учетной записи change_activity.
"""

class User:
    def __init__(self, nickname, login, password):
        self.nickname = nickname
        self.login = login
        self.password = password
        self.is_active = True

    def show_details(self):
        if not self.is_active:
            print('Учетная запись не активна')
        else: print(self.nickname, self.login)

    def change_activity(self):
        if not self.is_active: self.is_active = True
        else: self.is_active = False

dirac = User('Dirac Duran', 'dirac@duran.io', 'blah242u598729')
dirac.show_details()
dirac.change_activity()
dirac.show_details()