# -*- coding: utf-8 -*-
"""
Напишите программу, которая спрашивает:
    1) "Введите число, которое умножить на 10?"
    2) "Как Вас зовут?"
Выведите итоговый результат на экран в формате:
    <NAME>, если число <INPUT_NUMBER> умножить на 10, то получится <NEW_NUMBER_X10>!
    где <NAME> - введенное Вами имя
    <INPUT_NUMBER> - введенное Вами число
    <NEW_NUMBER_X10> - введенное число, умноженное на 10
"""
input_number = input('Введите число, которое умножить на 10? ')
name = input('Как Вас зовут? ')
print(name + ', если число ' + input_number + ' умножить на 10, то получится ' + str(int(input_number) * 10) + '!')