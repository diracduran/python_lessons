# -*- coding: utf-8 -*-
"""
1. Дан список с месяцами months
2. Заменить каждый из месяцев списка months на англоязычное:
    Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
3. Вывести измененный список на экран.
4. Для месяца вашего рождения сделать изменения в списке: сохранить его в верхнем регистре с применением метода upper().
5. Вывести список на экран.
"""
# Ваш код ниже
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
months[0] = 'Jan'
months[1] = 'Feb'
months[2] = 'Mar'
months[3] = 'Apr'
months[4] = 'May'
months[5] = 'Jun'
months[6] = 'Jul'
months[7] = 'Aug'
months[8] = 'Sep'
months[9] = 'Oct'
months[10] = 'Nov'
months[11] = 'Dec'
print(months) #['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months[6] = 'Jul'.upper()
print(months) #['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'JUL', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']