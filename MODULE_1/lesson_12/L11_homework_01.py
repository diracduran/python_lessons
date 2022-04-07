# -*- coding: utf-8 -*-
# L11_homework_01.py
"""
Ниже даны 5 заданий. В каждом из них необходимо добавить по ОДНОЙ СТРОКЕ КОДА (НЕ БОЛЬШЕ!!!) вместо прочерков --------------- так, чтобы задание было выполнено в соответствии с условием
"""
# Задание 1.1
"""
Допишите код программы таким образом, чтобы в результатом ее работы было сообщение:
    
        Результат работы программы:
            
            ЗАДАНИЕ 1.1

            Иван: Сегодня отличный день!
            
"""

print("ЗАДАНИЕ 1.1")
print()

class Talk():
    
    def __init__(self, user, text): # Ваш код должен быть здесь
        self.user = user
        self.text = text
        
ivan_talk = Talk("Иван", "Сегодня отличный день!")
print(ivan_talk.user + ": " + ivan_talk.text)

print("-" * 50)
# Задание 1.2
"""
Допишите код программы таким образом, чтобы в результатом ее работы было сообщение: 
    
        Результат работы программы:
            
            ЗАДАНИЕ 1.2

            Анна Петрова | баланс: 0
            
"""


print("ЗАДАНИЕ 1.2")
print()

class Bank():
    
    def __init__(self, first_name, last_name, balance): 
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance# Ваш код должен быть здесь
        
anna_bank = Bank("Анна", "Петрова", 0)
print(anna_bank.first_name + " " + anna_bank.last_name + " | баланс: " + str(anna_bank.balance))

print('-'*50)        

# Задание 1.3
"""
Допишите код программы таким образом, чтобы в результатом ее работы было сообщение: 
    
        Результат работы программы:
            
            ЗАДАНИЕ 1.3

            Петр Иванов | баланс: 10000
            
"""
print("ЗАДАНИЕ 1.3")
print()

class Bank_1():
    
    def __init__(self, first_name, last_name, balance): 
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
    
    def show_balance(self): # Ваш код должен быть здесь
        print(self.first_name + " " + self.last_name + " | баланс: " + str(self.balance))
        
petr_bank = Bank_1("Петр", "Иванов", 10000)
petr_bank.show_balance()

print('-'*50)
# Задание 1.4
"""
Допишите код программы таким образом, чтобы в результатом ее работы было сообщение: 
    
        Результат работы программы:
            
            ЗАДАНИЕ 1.4

            Олег Степанов | баланс: 30000
            
"""
print("ЗАДАНИЕ 1.4")
print()

class Bank_2():
    
    def __init__(self, first_name, last_name, balance): 
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
    
    def add_money(self, money): # Ваш код должен быть здесь
        self.balance += money
        
oleg_bank = Bank_2("Олег", "Степанов", 10000)
oleg_bank.add_money(20000)
print(oleg_bank.first_name + " " + oleg_bank.last_name + " | баланс: " + str(oleg_bank.balance))

print('-'*50)

# Задание 1.5
"""
Допишите код программы таким образом, чтобы в результатом ее работы было сообщение: 
    
        Результат работы программы:
            
            ЗАДАНИЕ 1.5

            Майк Смит | зарплата: 72000
            
"""
print("ЗАДАНИЕ 1.5")
print()

class Salary():
    
    def __init__(self, first_name, last_name, salary_per_day, days): 
        self.first_name = first_name
        self.last_name = last_name
        self.salary_per_day = salary_per_day
        self.days = days
        
    def count_salary(self):
        return self.salary_per_day * self.days # Ваш код должен быть здесь
    
name = "Майк"
lastname = "Смит"
salary = 3000
days = 24
mike_salary = Salary(name, lastname, salary, days)
print(mike_salary.first_name + " " + mike_salary.last_name + " | зарплата: " + str(mike_salary.count_salary()))

print('-'*50)


print('-'*50)
