# the2nd_l07_01_practice.py
"""
Даны списки фильмов актеров angelina_jolie (Анджелина Джоли), brad_pitt (Брэд Питт) и george_clooney (Джордж Клуни).
Используя множества необходимо узнать в каких фильмах снимались вместе:
1) Брэд Питт и Анджелина Джоли (результат сохранить в список pitt_and_jolie)
2) Брэд Питт и Джордж Клуни (результат сохранить в список pitt_and_clooney)
3) Джордж Клуни и Анджелина Джоли (результат сохранить в список clooney_and_jolie)

"""
angelina_jolie = ["В поисках выхода", "Киборг 2: Стеклянная тень", "Хакеры",  "Без улик", "Луна пустыни", "Итальянские любовники", "Ложный огонь", "Изображая Бога", "Настоящие женщины", "Адский котёл", "Превратности любви", "Управляя полётами", "Власть страха", "Прерванная жизнь", "Угнать за 60 секунд", "Лара Крофт: Расхитительница гробниц",
                  "Соблазн", "Жизнь или что-то вроде того", "Лара Крофт: Расхитительница гробниц. Колыбель жизни", "За гранью", "Лихорадка", "Забирая жизни", "Небесный капитан и мир будущего", "Александр", "Мистер и миссис Смит", "Ложное искушение", "Беовульф", "Её сердце", "Особо опасен", "Подмена", "Солт", "Турист", "Малефисента", "Лазурный берег", "Малефисента 2"]


brad_pitt = ["Нет выхода", "Нейтральная полоса", "Меньше, чем ноль", "Тёмная сторона Солнца", "Счастливы вместе", "Пропуск занятий", "Гонки по кругу", "Джонни Замша", "Тельма и Луиза", "Контакт", "Параллельный мир", "Там, где течёт река", "Калифорния", "Настоящая любовь", "Услуга", "Интервью с вампиром: Хроника жизни вампира", "Легенды осени", "Семь", "12 обезьян", "Спящие", "Собственность дьявола", "Семь лет в Тибете", "Знакомьтесь, Джо Блэк", "Бойцовский клуб", "Большой куш", "Мексиканец", "Шпионские игры",
             "Одиннадцать друзей Оушена", "Признания опасного человека", "Троя", "Двенадцать друзей Оушена", "Мистер и миссис Смит", "Вавилон", "Тринадцать друзей Оушена", "Как трусливый Роберт Форд убил Джесси Джеймса", "После прочтения сжечь", "Загадочная история Бенджамина Баттона", "Бесславные ублюдки", "Древо жизни", "Человек, который изменил всё", "Ограбление казино", "Война миров Z", "12 лет рабства", "Советник", "Ярость", "Лазурный берег", "Игра на понижение", "Союзники", "Машина войны", "Дэдпул 2", "К звёздам", "Однажды в Голливуде"]


george_clooney = ["Возвращение в школу ужасов", "Возвращение помидоров-убийц", "Красный прибой", "Сансет Бит", "Урожай", "От заката до рассвета", "Один прекрасный день", "Бэтмен и Робин", "Миротворец", "Вне поля зрения", "Тонкая красная линия", "Три короля", "Взрыв", "О, где же ты, брат?", "Идеальный шторм", "Дети шпионов", "Одиннадцать друзей Оушена", "Добро пожаловать в Коллинвуд", "Солярис", "Признания опасного человека",
                  "Дети шпионов 3: Игра окончена", "Невыносимая жестокость", "Двенадцать друзей Оушена", "Доброй ночи и удачи", "Сириана", "Хороший немец", "Тринадцать друзей Оушена", "Майкл Клейтон", "Любовь вне правил", "После прочтения сжечь", "Безумный спецназ", "Мне бы в небо", "Американец", "Потомки", "Мартовские иды", "Гравитация", "Охотники за сокровищами", "Земля будущего", "Аве, Цезарь!", "Финансовый монстр"]

jolie_set = set(angelina_jolie)
pitt_set = set(brad_pitt)
clooney_set = set(george_clooney)

pitt_and_jolie = jolie_set.intersection(pitt_set)
pitt_and_clooney = pitt_set.intersection(clooney_set)
clooney_and_jolie = clooney_set.intersection(jolie_set)


print("Задание 1:", pitt_and_jolie)
print("Задание 2:", pitt_and_clooney)
print("Задание 3:", clooney_and_jolie)
