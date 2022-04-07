# -*- coding: utf-8 -*-
"""
1. Создайте числовой список numbers от 1 до 462 с шагом 13.
2. В цикле for переберите числа и если число делиться и на 3 и на 2 целиком, то возьмите следующее число из списка (используйте continue), выведите I NEED NEXT NUMBER и число.
3. Если число делится только на 3 целиком (n % 3 == 0), то выведите число и слово THREE
4. Если число делится только на 4 целиком (n % 4 == 0), то выведите число и слово FOUR
5. Если число делится одновременно на 3, 4 и 6 целиком, то прервите цикл фразой FANTASTIC, число
    Пример:
        27 THREE
        40 FOUR
        I NEED NEXT NUMBER 66
        92 FOUR
        105 THREE
        FANTASTIC,  144
"""
for i in range(1, 475, 13):
    if i % 3 == 0 and i % 4 == 0 and i % 6 == 0:
        print('FANTASTIC, ' + str(i))
    elif i % 2 == 0 and i % 3 == 0:
        print('I NEED NEXT NUMBER ' + str(i))
    elif i % 3 == 0:
        print(i, ' THREE')
    elif i %4 == 0:
        print(i, ' FOUR')