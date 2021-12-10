# -*- coding: utf-8 -*-
import random  # библиотека для генерации случайных целых чисел

# все возможные варианты выбора в виде списка
"""
Правила игры:
    "камень" бьет "ножницы",
    "ножницы" режут "бумагу",
    "бумага" оборачивает "камень"
"""
variants = ["камень", "ножницы", "бумага"]

# ввод данных пользователя и компьютера
"""
для переменной user_name:
    - реализуйте возможность ввода имени с клавиатуры
    - сделайте так, чтобы данные user_name сохранялись с использованием title()
    - выведите на экране сообщение о том кто сегодня против кого играет

"""
user_name = input('Введите имя пользователя: ',
                  ).title()  # здесь должен быть Ваш код
cpu_name = "Компьютер"
print('Сегодня играет ' + user_name + ' против ' +
      cpu_name)  # здесь должен быть Ваш код

# логика игры Камень, Ножницы, Бумага
"""
Реализуйте ввод данных пользователя user_variant, учитывая, что:
    0 - камень, 1 - ножницы, 2 - бумага
    
    cpu_variant - произвольное значение от 0 <= cpu_variant <= 2 - НЕ ИЗМЕНЯЕМ!!!!
    
    Программа должна:
        - если ввели user_variant > 2, то выводить сообщение "Неверное значение" и прекращать программу
        - выводить варианты ответа user_name и cpu_name на экран в формате:
            user_name: "камень"
            cpu_name: "ножницы"
        - определять победителя
        - выводить сообщения с именем победителя на экран
        - если ничья ("камень" - "камень", "ножницы" - "ножницы", "бумага" - "бумага"), то выводить на экран сообщение "Победила дружба!!!"
    Результат на экране:
        
        Введите имя пользователя: Николай
        Сегодня играет Николай против Компьютера
        __________________________________________________
        Ваш выбор 0 - камень, 1 - ножницы, 2 - бумага : 2
        Николай: бумага
        Компьютер: ножницы
        Компьютер ПОБЕДИЛ
    
    Задание со *:
        - добавить возможность играть 1, 3, 5 раундов на выбор с помощью ввода дынных от пользователя с клавиатуры "Введите количество раундов (1, 3, 5): "
        - если число не равно числам 1, 3 или 5, то выводить сообщение "Столько раундов мы не играем"
    Задание с **:
        - реализовать задание со *
        - реальзовать фунций подсчета очков в игре, где 
        победа +1 очко
        поражение 0 очков
        ничья +1 очко каждому (user_name и cpu_name)
        - выводить счет после каждого раунда в формате:
            Счет в противостоянии: 
            user_name 0 : 1 cpu_name
    Задание с ***:
        - реализовать задания * и **
        - добавить в программу возможность в конце выводить сообщение о результате игры с показом счета только для пользователя user_name: 
            победа - user_name, ПОЗДРАВЛЯЕМ! ВЫ ПОБЕДИЛИ СО СЧЕТОМ x:x
            поражение - user_name, К СОЖАЛЕНИЮ! ВЫ ПРОИГРАЛИ СО СЧЕТОМ х:x
            ничья  - НИЧЬЯ! СЧЕТ х:x
        
        
    Результат на экране для задачи со звездами:
       
    Введите имя пользователя: николай
    Сегодня играет Николай против Компьютера
    Введите количество раундов (1, 3, 5): 3
    __________________________________________________
    Раунд номер:  1
    Ваш выбор 0 - камень, 1 - ножницы, 2 - бумага : 0
    Николай: камень
    Компьютер: бумага
    Компьютер ПОБЕДИЛ
    Счет в противостоянии: 
    Николай 0 : 1 Компьютер
    __________________________________________________
    Раунд номер:  2
    Ваш выбор 0 - камень, 1 - ножницы, 2 - бумага : 2
    Николай: бумага
    Компьютер: бумага
    НИЧЬЯ
    Счет в противостоянии: 
    Николай 1 : 2 Компьютер
    __________________________________________________
    Раунд номер:  3
    Ваш выбор 0 - камень, 1 - ножницы, 2 - бумага : 1
    Николай: ножницы
    Компьютер: камень
    Компьютер ПОБЕДИЛ
    Счет в противостоянии: 
    Николай 1 : 3 Компьютер
    __________________________________________________
    Николай, К СОЖАЛЕНИЮ! ВЫ ПРОИГРАЛИ СО СЧЕТОМ 1 : 3 
        
        
"""

# здесь должен быть Ваш код
cpu_variant = random.randint(0, 2)  # генерирует ответ Компьютера от 0 до 2

flag = True
rounds = int(input("Введите количество раундов (1, 3, 5): ", ))
counter = 0
user_points = 0
cpu_points = 0

while flag:
    if rounds == 0 or rounds == 2 or rounds == 4 or rounds > 5:
        print("Столько раундов мы не играем")
        flag = False
        break
    else:
        while counter <= rounds:
            user_variant = int(
                input('Ваш выбор 0 - камень, 1 - ножницы, 2 - бумага : ', ))
            if user_variant > 2:
                print('Неверное значение')
            elif user_variant == 0:
                user_variant = 'камень'
            elif user_variant == 1:
                user_variant = 'ножницы'
            else:
                user_variant = 'бумага'

            if cpu_variant == 0:
                cpu_variant = 'камень'
            elif cpu_variant == 1:
                cpu_variant = 'ножницы'
            else:
                cpu_variant = 'бумага'

            if user_variant == cpu_variant:
                print(user_name + ': ' + str(user_variant))
                print(cpu_name + ': ' + str(cpu_variant))
                print("-"*20)
                user_points += 1
                cpu_points += 1
                print('Счет в противостоянии:')
                print(user_name + ' ' + str(user_points) + ':' + str(cpu_points) + ' ' + cpu_name)
                print("Победила дружба!!!")
                counter += 1
            elif user_variant == 'камень':
                if cpu_variant == 'ножницы':
                    print(user_name + ': ' + str(user_variant))
                    print(cpu_name + ': ' + str(cpu_variant))
                    print("-"*20)
                    user_points += 1
                    print('Счет в противостоянии:')
                    print(user_name + ' ' + str(user_points) + ':' + str(cpu_points) + ' ' + cpu_name)
                    print(user_name + ' ПОБЕДИЛ')
                    counter += 1
                elif cpu_variant == 'бумага':
                    print(user_name + ': ' + str(user_variant))
                    print(cpu_name + ': ' + str(cpu_variant))
                    print("-"*20)
                    cpu_points += 1
                    print('Счет в противостоянии:')
                    print(user_name + ' ' + str(user_points) + ':' + str(cpu_points) + ' ' + cpu_name)
                    print(cpu_name + ' ПОБЕДИЛ')
                    counter += 1

            elif user_variant == 'ножницы':
                if cpu_variant == 'камень':
                    print(user_name + ': ' + str(user_variant))
                    print(cpu_name + ': ' + str(cpu_variant))
                    print("-"*20)
                    cpu_points += 1
                    print('Счет в противостоянии:')
                    print(user_name + ' ' + str(user_points) + ':' + str(cpu_points) + ' ' + cpu_name)
                    print(cpu_name + ' ПОБЕДИЛ')
                    counter += 1
                elif cpu_variant == 'бумага':
                    print(user_name + ': ' + str(user_variant))
                    print(cpu_name + ': ' + str(cpu_variant))
                    print("-"*20)
                    user_points += 1
                    print('Счет в противостоянии:')
                    print(user_name + ' ' + str(user_points) + ':' + str(cpu_points) + ' ' + cpu_name)
                    print(user_name + ' ПОБЕДИЛ')
                    counter += 1
            elif user_variant == 'бумага':
                if cpu_variant == 'камень':
                    print(user_name + ': ' + str(user_variant))
                    print(cpu_name + ': ' + str(cpu_variant))
                    print("-"*20)
                    user_points += 1
                    print('Счет в противостоянии:')
                    print(user_name + ' ' + str(user_points) + ':' + str(cpu_points) + ' ' + cpu_name)
                    print(user_name + ' ПОБЕДИЛ')
                    counter += 1
                elif cpu_variant == 'ножницы':
                    print(user_name + ': ' + str(user_variant))
                    print(cpu_name + ': ' + str(cpu_variant))
                    print("-"*20)
                    cpu_points += 1
                    print('Счет в противостоянии:')
                    print(user_name + ' ' + str(user_points) + ':' + str(cpu_points) + ' ' + cpu_name)
                    print(cpu_name + ' ПОБЕДИЛ')
                    counter += 1
            if counter >= rounds:
                flag = False
                break

print('-'*20)

if user_points > cpu_points:
    print(user_name + ', ПОЗДРАВЛЯЕМ! ВЫ ПОБЕДИЛИ СО СЧЕТОМ ' + str(user_points) + ':' + str(cpu_points))
elif user_points < cpu_points:
    print(user_name + ', К СОЖАЛЕНИЮ! ВЫ ПРОИГРАЛИ СО СЧЕТОМ ' + str(user_points) + ':' + str(cpu_points))
else:
    print('НИЧЬЯ! СЧЕТ ' + str(user_points) + ':' + str(cpu_points))