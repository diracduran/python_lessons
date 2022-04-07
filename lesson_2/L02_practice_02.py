# -*- coding: utf-8 -*-
"""
Установите для каждой переменной значение True или False в зависимости от того, каким будет результат. Вам необходимо заменить '' на True или False в каждой переменной.

Например, (2 > 1) and (3 < 4) будет True, потому что (2 > 1) —> True and (3 < 4) —> True, то есть True and True —> True (bool_zero = True).
"""
# Ваш код ниже
# 1) Установите bool_1 равным результату: False and False
bool_1 = 'false'
print("(1)", "False and False -->", bool_1)
# 2) Установите bool_2 равным результату: -(-(-(-2))) == -2 and 8 >= 2 ** 3
bool_2 = 'false'
print("(2)", "-(-(-(-2))) == -2 and 8 >= 2 ** 3 -->", bool_2) # false (-(-(-(-2)))=2) И true -> false
# 3) Установите bool_3 равным результату: (199 - 197) ** 2 != 400 / 10 / 10 and True
bool_3 = 'false'
print("(3)", "(199 - 197) ** 2 != 400 / 10 / 10 and True -->", bool_3) # false ((199 - 197) ** 2 = 4 и 400/10/10=4) и true -> false
# 4) Установите bool_4 равным результату: -(1 ** 2) < (2 ** 1) / 2 and 10 / 10 <= 20 - 10 ** 2
bool_4 = 'false'
print("(4)", "-(1 ** 2) < (2 ** 1) / 2 and 10 / 10 <= 20 - 10 ** 2 -->", bool_4) #true (-(1 ** 2) = -1, (2 ** 1) / 2 = 1) и false(10 / 10 = 1, 20 - 10 ** 2=-80 ) -> true
# 5) Установите bool_5 равным результату: True and True
bool_5 = 'true'
print("(5)", "True and True -->", bool_5)
# 6) Установите bool_6 равным результату: 2 ** 3 == (20 - 10) / 5 * 4 or 'Python' == 'Windows'
bool_6 = 'true'
print("(6)", "2 ** 3 == (20 - 10) / 5 * 4 or ('Python' == 'Windows') -->", bool_6) # 8 = 8 -> true or false -> true
# 7) Установите bool_7 равным результату: True or False
bool_7 = 'true'
print("(7)", "True or False -->", bool_7)
# 8) Установите bool_8 равным результату: (100 * 2) / 20 >= -(1 - 2) * 10 or False
bool_8 = 'true'
print("(8)", "(100 * 2) / 20 >= -(1 - 2) * 10 or False -->", bool_8) # 10 >= 10 -> true or false -> true
# 9) Установите bool_9 равным результату: True or True
bool_9 = 'true'
print("(9)", "True or True -->", bool_9)
# 10) Установите bool_10 равным результату: 3 * 2 * 1 != 3 + 2 + 1 or 1 ** 2 != 2 / 1
bool_10 = 'true'
print("(10)", "3 * 2 * 1 != 3 + 2 + 1 or 1 ** 2 != 2 / 1 -->", bool_10) # 6 = 6 -> true or 1 != 2 -> false -> true
# 11) Установите bool_11 равным результату: not True
bool_11 = 'false'
print("(11)", "not True -->", bool_11)
# 12) Установите bool_12 равным результату: not 3 ** 4 < 4 ** 3
bool_12 = 'true'
print("(12)", "not 3 ** 4 < 4 ** 3 -->", bool_12) # 81 < 64 = false, not false = true
# 13) Установите bool_13 равным результату: not 10 / 4 <= 5 / 2
bool_13 = 'false'
print("(13)", "not 10 / 4 <= 5 / 2 -->", bool_13)# 10/4 = 2.5, 5/2 = 2.5, 2.5 == 2.5 -> true, not true -> false
# 14) Установите bool_14 равным результату: not 3 ** 2 + 4 ** 2 != 5 ** 2
bool_14 = 'true'
print("(14)", "not 3 ** 2 + 4 ** 2 != 5 ** 2 -->", bool_14) # 3 ** 2 + 4 ** 2 = 9 + 16 = 25, 5 ** 2 = 25, 25 == 25 -> false, not false = true
# 15) Установите bool_15 равным результату: not not False
bool_15 = 'false'
print("(15)", "not not False -->", bool_15) # not false = true, not true = false
# 16) Установите bool_16 равным результату: not False and True or (True and False)
bool_16 = 'true'
print("(16)", "not False and True or (True and False) -->", bool_16) #true & true or false -> true
# 17) Установите bool_17 равным результату: (65 < 56 or 56 > 65) and ('True' == 'true' or False == False)
bool_17 = 'false'
print("(17)", "(65 < 56 or 56 > 65) and ('True' == 'true' or False == False) -->", bool_17) # (false or false -> false) & (false or true -> true) = false

