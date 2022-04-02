# -*- coding: utf-8 -*-
"""
Ваша группировка - 5 хакеров.
Создайте 5 переменных, которые будет соответствовать каждому из 5 хакеров (вы и еще 4 человека).
Например: goldfish = "Goldfish", dirtymoney_666 = "dirtymoney-666" и тд.
Вы взломали электронную защиту крупнейшего банка BANK OF THE WORLD и перевели на секретный счет 1729920005126822 $ (hacked_amount)
Теперь Вам нужно раcпределить сумму на 5 равных частей среди хакеров.
За риски вы получаете 50 % от суммы.
Остальные хакеры получат равные доли от оставшейся суммы (по 25 %).
Вывести на экран для каждого хакера текст в формате используя переменные:
    'Goldfish: 216240000640852.75 $'
    'dirtymoney-666: 864960002563411.0 $'
    ...

"""

goldfish = 'Goldfish'
dirtymoney_666 = 'dirtymoney-666'
xrabbitx = 'x_Rabbit_x'
hsjfgs = 'HsJfGs'
kj21al = 'kj21al'

hacked_amount = 1729920005126822
risk_amount = hacked_amount / 2  # 50% от суммы за риск
# остальная сумма, которые должны получить хакеры
rest_amount = (hacked_amount - risk_amount) / 4

# Goldfish: 216240000640852.75 $
print(goldfish + ': ' + str(rest_amount) + ' $')
# dirtymoney-666: 864960002563411.0 $
print(dirtymoney_666 + ': ' + str(risk_amount) + ' $')
# x_Rabbit_x: 216240000640852.75 $
print(xrabbitx + ': ' + str(rest_amount) + ' $')
print(hsjfgs + ': ' + str(rest_amount) + ' $')  # HsJfGs: 216240000640852.75 $
print(kj21al + ': ' + str(rest_amount) + ' $')  # kj21al: 216240000640852.75 $
