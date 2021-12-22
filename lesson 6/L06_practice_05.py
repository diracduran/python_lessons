# -*- coding: utf-8 -*-
"""
1. Дана функция your_bank_account().
2. Вызовите функцию пятью разными способами. 
"""
def your_bank_account(name, year_of_birth, balance=0):
    print("Клиент: "  + name.title())
    print("Возраст: " + str(2021 - year_of_birth))
    print("Баланс: " + str(balance))



your_bank_account('Dirac', 1998, 25000)

your_bank_account(year_of_birth=1998, balance=25000, name='Dirac')

your_bank_account('Dirac', 1998, balance=25000)

your_bank_account('Dirac', 1998)

bal= 30000
your_bank_account('Dirac', 1998, bal)