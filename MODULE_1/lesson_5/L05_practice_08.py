# -*- coding: utf-8 -*-
"""
1. Дан словарь workers (список сотрудников).
2. Обращаясь к словарю workers, найдите средний возраст ВСЕХ сотрудников (то есть нужно получить одну цифру). Результат сохраните в переменную avarage_age.
    формула для расчета: СУММА ВОЗРОСТА ВСЕХ СОТРУДНИКОВ / КОЛ-ВО СОТРУДНИКОВ
3. Под ключом "achievements" хранится список достижений для каждого сотрудника. Необходимо вывести на экран список всех достижений для каждого сотрудника, причем, если достижений нет, то вывести сообщение: Достижений нет!
    Пример:
        Леонов Александр (Менеджер по продажам).
        Достижения:
            Менеджер месяца (Март 2019)
            Лучшая промо активность (Апрель 2019)
        Иван Петров (Охранник).
        Достижения:
            Достижений нет!
4. Дан словарь clients (список клиентов).
5. Найдите сумму покупок для каждого клиента (buy_list). Суммы генерируются автоматически (на это не обращайте внимание). Сохраните сумму под ключом "summa" для каждого клиента (новая пара ключ-значение).
6. Создайте новую пару ключ-значение "discount" (скидка клиента), значение которой зависит от суммы ("summa"). Условия для скидки:
    a) до 1000: 0.0
    b) от 1000 до 5000: 0.02
    c) от 5000 до 10000: 0.05
    d) от 10000 до 25000: 0.1
    e) от 25000 и выше: 0.25
7. Выведите информацию о клиентах из словаря clients в виде:
    client_00001  Рябчиков Степан:
        Сумма: 13500
        Скидка: 10 %
P.S. Скидку нужно преобразовать в строку по формуле str(0.1 * 100) + " %"
"""
import random

def generate_random_num_list():
    res = []
    q = random.randint(1, 10)
    min_buy = 100
    max_buy = 3000
    for i in range(q):
        res.append(random.randint(min_buy, max_buy))
    return res

workers = [
        {"name": "Александр", "lastname": "Леонов", "age": 35, "role": "Менеджер по продажам", "achievements": ["Менеджер месяца (Март 2019)", "Лучшая промо активность (Апрель 2019)"]},
        {"name": "Иван", "lastname": "Петров", "age": 56, "role": "Охранник", "achievements": []},
        {"name": "Олег", "lastname": "Бубликов", "age": 32, "role": "Менеджер по продажам", "achievements": ["Менеджер месяца (Июнь 2019)", "Менеджер месяца (Июль 2019)", "Лучший старт продаж нового бренда (Август 2019)"]},
        {"name": "Анна", "lastname": "Ветрова", "age": 27, "role": "Бухгалтер", "achievements": []},
        {"name": "Геннадий", "lastname": "Сталеваров", "age": 45, "role": "Директор", "achievements": ["Лучшее предприятие года (2017)", "Лучшее предприятие года (2018)", "Лучшие показатели по дистрибьюции нового продукта XYZ (Март 2019)"]}
        ]

for worker in workers:
    name = worker['name']
    lastname = worker['lastname']
    age = worker['age']
    role = worker['role']
    achievements = worker['achievements']
    print(lastname, name + ' (' + role + ').\nДостижения:\t')
    for achievement in range(len(achievements)):
        print('\t' + achievements[achievement])
    if achievements == []:
        print('\tДостижений нет :<')
    print('\n')

            
        

clients = {
        "client_0001": {"name": "Степан", "lastname": "Рябчиков", "buy_list": generate_random_num_list()},
        "client_0002": {"name": "Борис", "lastname": "Иванов", "buy_list": generate_random_num_list()},
        "client_0003": {"name": "Алексей", "lastname": "Стриженов", "buy_list": generate_random_num_list()},
        "client_0004": {"name": "Игорь", "lastname": "Денисов", "buy_list": generate_random_num_list()},
        "client_0005": {"name": "Максим", "lastname": "Бориско", "buy_list": generate_random_num_list()},
        "client_0006": {"name": "Евгений", "lastname": "Овсиенко", "buy_list": generate_random_num_list()},
        "client_0007": {"name": "Артём", "lastname": "Макарчук", "buy_list": generate_random_num_list()}
        }

for client in clients.values():
    client['summa'] = 0
    client['discount'] = 0
    for buy in client['buy_list']:
        client['summa'] += buy
    if client['summa'] < 1000:
        client['discount'] = 0.0
    elif client['summa'] < 5000:
        client['discount'] = 0.02
    elif client['summa'] < 10000:
        client['discount'] = 0.05
    elif client['summa'] < 25000:
        client['discount'] = 0.1
    elif client['summa'] > 25000:
        client['discount'] = 0.25

for cl, data in clients.items():
    print(cl, data['lastname'], data['name'] + ': \n\tСумма: ' + str(data['summa']) + '\n\tСкидка: ' + str(data['discount']*100) + '%')


# print(workers)
# print(clients)
