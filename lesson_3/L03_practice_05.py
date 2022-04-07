# -*- coding: utf-8 -*-
"""
1. Дан список с месяцами months и пустые списки означающие времена года (winter - зима, spring - весна, summer - лето, autumn - осень).
2. Используя метод .append() наполните списки spring и autumn, обращаясь по индексу к списку months.
3. Используя метод .insert() наполните списки winter и summer, обращаясь по индексу к списку months.
4. Выведите все списки сезонов на экран.
"""
# Ваш код ниже
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
winter = []
spring = []
summer = []
autumn = []

spring.append('Март')
spring.append('Апрель')
spring.append('Май')
print(spring)

autumn.append('Сентябрь')
autumn.append('Октябрь')
autumn.append('Ноябрь')
print(autumn)

winter.insert(0, 'Декабрь')
winter.insert(1, 'Январь')
winter.insert(2, 'Февраль')
print(winter)

summer.insert(0, 'Июнь')
summer.insert(1, 'Июль')
summer.insert(2, 'Август')
print(summer)