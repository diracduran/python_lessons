# -*- coding: utf-8 -*-
"""
ИГРА: ЛИШНЕЕ СЛОВО!
ПРАВИЛА ИГРЫ: ДАНЫ 5 СЛОВ, ОДНО ИЗ НИХ ЛИШНЕЕ ПО СМЫСЛУ. ЕГО НЕОБХОДИМО ВЫБРАТЬ ИЗ ИМЕЮЩИХСЯ ВАРИАНТОВ. ВСЕГО 15 РАУНДОВ. ПО ИТОГУ ВЫСТАВЛЯЕТСЯ ОЦЕНКА В ВИДЕ 80 % ИЛИ ЗАПИСИ 12/15.
1. Дан словарь the_fifth_wheel, который состоит из пар ключ - раунд, значения 5 слов в виде списка.
2. Неправильные слова в списке excess_word_list.
3. Словарь для сбора результатов игры game_results. Вам необходимо после каждого раунда (цикла) изменять его значения, в зависимости от результата:
    "correct: 0,
    "wrong": 0
P.S. Выбор ответа пользователя реализуйте с помощью input(). Рекомендую использовать индексы для каждого слова от 0 до 4. Выбранное слово проверяйте на наличие в списке excess_word_list. Если слово есть в списке, то обращайтесь к ключу "wrong", иначе ключ "correct".
4. После окончания 15 раундов игры выведите результаты на экран:
    Ваш Результат:
        12/15 ПРАВИЛЬНЫХ ОТВЕТОВ
P.S. Либо вывести в результат в %.
"""

the_fifth_wheel = {
        "round_1": ['кукла', 'песок', 'юла', 'ведёрко', 'мяч'],
        "round_2": ['стол', 'шкаф', 'ковёр', 'кресло', 'диван'],
        "round_3": ['пальто', 'шапка', 'шарф', 'сапоги', 'шляпа'],
        "round_4": ['слива', 'яблоко', 'помидор', 'абрикос', 'груша'],
        "round_5": ['роза', 'тюльпан', 'фасоль', 'василёк', 'мак'],
        "round_6": ['зима', 'апрель', 'весна', 'осень', 'лето'],
        "round_7": ['море', 'озеро', 'река', 'мост', 'пруд'],
        "round_8": ['круг', 'квадрат', 'карандаш', 'треугольник', 'прямоугольник'],
        "round_9": ['сыр', 'булка', 'мороженое', 'масло', 'творог'],
        "round_10": ['бутылка', 'банка', 'сковородка', 'кувшин', 'стакан'],
        "round_11": ['молоко', 'сливки', 'сыр', 'сало', 'сметана'],
        "round_12": ['берёза', 'сосна', 'дерево', 'дуб', 'ель'],
        "round_13": ['книга', 'альбом', 'блокнот', 'краски', 'тетрадь'],
        "round_14": ['торт', 'портфель', 'сумка', 'рюкзак', 'чемодан'],
        "round_15": ['месяц', 'день', 'год', 'небо', 'час']
        }

excess_word_list = ["песок", "ковёр", "сапоги", "помидор", "фасоль", "апрель", "мост", "карандаш", "булка", "сковородка", "сало", "дерево", "краски", "торт", "небо"]

game_results = {"correct": 0, "wrong": 0}

for words in the_fifth_wheel.values():
    question = input("Какое слово лишнее: " + ', '.join(words) + '? ')
    for excess_word in excess_word_list:
        if question in excess_word:
            game_results['wrong'] += 1
            continue
        elif  question not in excess_word:
            game_results['correct'] += 1
            continue

print('Ваш Результат: ' + '\n\t' + str(game_results['wrong']) + '/15 ПРАВИЛЬНЫХ ОТВЕТОВ')