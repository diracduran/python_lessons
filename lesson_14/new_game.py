

"""
СЛОВА ИЗ СЛОВ
Онлайн пример игры для понимания процесса:
https://ollgames.ru/slova-iz-slova/

ПРАВИЛА ИГРЫ

Цель игры – составить максимальное количество слов из предложенного длинного слова. Каждую букву длинного слова можно использовать в новом слове только один раз. Буквы можно использовать в произвольном порядке. Слова не менее 3-х букв.

Пример:
	Слово: мексиканец
	Буквы (в виде списка): ['м', 'е', 'к', 'с', 'и', 'к', 'а', 'н', 'е', 'ц']
	Возможные варианты: ['иена', 'икс', 'иск', 'каик', 'каин', 'камин', 'кан', 'кекс', 'кениец', 'кика', 'кикс', 'кница', 'маис', 'мак', 'мансиец', 'мекка', 'мексиканец', 'мена', 'миска', 'немец', 'самец', 'сан', 'сема', 'сиамец', 'сиена', 'синец', 'скена', 'смена', 'сцена', 'цена', 'цинк']
	В случае составленного слова выводим определение: иена - ж. Денежная единица Японии.

В требования к игре:
	- 30 % составленных слов для перехода на следующий уровень (округление в большую сторону, то есть 31 слово * 0.3 = 9.3 --> 10, значит для перехода на следующий уровень 10 слов)
	- если все слова составлены, то автоматический переход на следующий уровень (на последнем уровне выводить сообщение все слова составлены, для начала новой игры введите NEW) 
	- слово для уровня должно содержать не менее 30 вариантов (для проверки используйте help_functions.py - описание ниже)
	- игру создать минимум на 10 уровней
	- каждый уровень должен увеличиваться по сложности согласно количеству слов для составления. Например:
			1 уровень: 30 возможных слов (для перехода 9 слов);
			2 уровень: 35 возможных слов (для перехода 11 слов);
			...
			10 уровень: 75 возможных слов (для завершения 23 слова).
	- список слов для игры сохранить в глобальную переменную GAME_WORDS
	- реализовать интерфейс игры:
			NEXT - переход на следующий уровень (если вы угадали нужное количество слов)
			PREVIOUS - переход на предыдущий уровень (если хотите угадать большее количество слов)
			EXIT - выход и сохранение прогресса (для PLAYER)
			NEW - стирает весь прогресс и вы начинаете заново
			RULES - выводит правила игры
			RATING - выводит соотношение составленных слов к общему числу вариантов на текущий уровень (то есть, вы на 3 уровне всего 105 слов, угадано 50 - рейтинг 50 / 105 = 0.48 или 48 %, 
			HELP - выводит команды интерфейса игры
	- предусмотреть возможность сохранения игры (через сохранение в .json файл прогресс игрока, причем имя файла == имя игрока, например:
			имя nick - файл nick.json
	- если имя игрока не найдено (то есть файл json с именем не найден), то начинаем новую игру)
	- если имя игрока найдено (то есть файл json с именем найден), то продолжаем игру с того места где закончили
	- реализация игры через Классы:
		1) Класс Player - класс игрока
		2) Класс Game - класс процесса игры
	- при загрузке игры слова поместить в ГЛОБАЛЬНУЮ ПЕРЕМЕННУЮ WORDS_WITH_DEFINITIONS (далее использовать ее для проверки слов и вывода определений)


Вспомогательные данные:

Дан 1 файл:
1.    nouns.csv - таблица слов из существительных (word) 34263 слов, у каждого слова есть определение (definition), в качестве значения к слову
	пример: 
		"иена": "ж. Денежная единица Японии."
		
		
В файле help_functions.py написаны 3 функции:
1.    check_word(word: str) - функция принимает в качестве аргумента слово (str) и возвращает кортеж из 2-х элементов: (True или False, количество вариантов). Если первый элемент кортежа False, то слово не подходит для игры.
2.    get_word_letters(word: str) - функция принимает в качестве аргумента слово (str) и возвращает список букв в порядке их следования в переданном слове (понадобится для вывода на экран доступных букв)
3.    create_word_list(word: str) - функция принимает в качестве аргумента слово и возвращает список возможных слов, с учетом правила, где каждое слово >= 3 буквы (понадобится для составления списка вариантов слов на каждом уровне)

Профиль игрока:
1. Для создания нового игрока используется class Player:
	class Player:
		def __init__(self, name):
			self.name = name
			self.profile = {}

	Атрибут self.profile имеет структуру:
		
	{
		"current_level" : 1, # номер уровня (int)
		"level_1": {
			"word": "слово уровня 1", # сохранить слово уровня 1
			"letters": "буквы для слова", # используйте вспомогательную функцию
			"variants": 30, # количество вариантов для слова
			"answers": [], # угаданные слова в виде списка
			"guessed": 1, # количество угаданных слов
			"need_to_next_level": 9, # сколько слов до перехода на следующий уровень
			"is_done": False, # Пройден уровень - True, если нет - False (зависит от параметра "need_to_next_level")
			},
			...,
        "level_10": {}, # словарь до 10 уровня
	}

Игровой процесс:
1. Для создания процесса игры используется class Game:
		class Game:
			def __init__(self):
				self.player = Player() # игрок
				self.game_words = GAME_WORDS # слова для уровней игры по возрастанию количества вариантов
				self.word_list_definitions = WORDS_WITH_DEFINITIONS # словарь "слово": "определение"
				self.game_flag = True # управление процессом игры в цикле
				self.rules = '''ПРАВИЛА ИГРЫ
				не менее 3-х букв.
								Пример:
					Слово: мексиканец
					Буквы (в виде списка): ['м', 'е', 'к', 'с', 'и', 'к', 'а', 'н', 'е', 'ц']
					Возможные варианты: ['иена', 'икс', 'иск', 'каик', 'каин', 'камин', 'кан', 'кекс', 'кениец', 'кика', 'кикс', 'кница', 'маис', 'мак', 'мансиец', 'мекка', 'мексиканец', 'мена', 'миска', 'немец', 'самец', 'сан', 'сема', 'сиамец', 'сиена', 'синец', 'скена', 'смена', 'сцена', 'цена', 'цинк']
					В случае составленного слова выводим определение: иена - ж. Денежная единица Японии.'''
				self.command_list = [
					'NEXT',
					'PREVIOUS',
					'EXIT',
					'NEW',
					'RULES',
					'HELP',
					'RATING'
				]
2. В начале игры запрашивается имя игрока, если оно найдено в списке файлов username.json, то игра продолжается с того места, на котором вы остановились
3. Если игрок новый, то начинаете новую игру и все остальные поля игрока заполняются автоматически (self.profile)
4. Далее выведите на экран ПРАВИЛА ИГРЫ
5. После этого выведите номер уровня и СЛОВО, для которого подбираете слова
6. После каждой попытки выводите следующую информацию (можете оформить на свое усмотрение):
	УРОВЕНЬ: 1
	СЛОЖНОСТЬ: ЛЕГКИЙ
	СЛОВО: МЕКСИКАНЕЦ
	ВАРИАНТОВ: 30
	НЕОБХОДИМО УГАДАТЬ: 8
	УГАДАННО СЛОВ: 4
	ДО СЛЕДУЮЩЕГО УРОВНЯ: 4
	БУКВЫ: М Е К С И К А Н Е Ц
	УГАДАННЫЕ СЛОВА: ['иена', 'каин', 'кениец', 'миска']
	ВВЕДИТЕ СЛОВО: смена
	>>> ПОЗДРАВЛЯЕМ, username, Вы угадали!
7. При вводе вводе ключевых слов интерфейса (NEXT, PREVIOUS, NEW, EXIT, RULES, RATING, HELP) выполнять действия, описанные выше.

"""
from help_functions import get_word_letters, check_word, create_word_list, WORDS_WITH_DEFINITIONS
import csv
import json

GAME_WORDS = []

with open("d:\\study_projects\\python_repos\\python_lessons\\lesson_14\\nouns.csv", "r", encoding="utf-8") as csv_file:
	reader = csv.reader(csv_file, delimiter=',') # объект csv для чтения функция reader
	data = [row for row in reader] # пустой список для сохранения прочитанных данных
	# for row in reader:
	# 	data.append(row) # добавление в список
	WORDS_WITH_DEFINITIONS = {w[0]: w[1] for w in data[1:]}

class Player:
    initial_level = 1
    def __init__(self):
        self.name = input('Ваше имя: ')
        self.profile = {}



class Game:
    
    def __init__(self):
        self.player = Player() # игрок
        self.current_level = 1
        self.game_words = GAME_WORDS # слова для уровней игры по возрастанию количества вариантов
        self.word_list_definitions = WORDS_WITH_DEFINITIONS # словарь "слово": "определение"
        self.game_flag = True # управление процессом игры в цикле
        self.rules = '''ПРАВИЛА ИГРЫ
        не менее 3-х букв.
                        Пример:
            Слово: мексиканец
            Буквы (в виде списка): ['м', 'е', 'к', 'с', 'и', 'к', 'а', 'н', 'е', 'ц']
            Возможные варианты: ['иена', 'икс', 'иск', 'каик', 'каин', 'камин', 'кан', 'кекс', 'кениец', 'кика', 'кикс', 'кница', 'маис', 'мак', 'мансиец', 'мекка', 'мексиканец', 'мена', 'миска', 'немец', 'самец', 'сан', 'сема', 'сиамец', 'сиена', 'синец', 'скена', 'смена', 'сцена', 'цена', 'цинк']
            В случае составленного слова выводим определение: иена - ж. Денежная единица Японии.'''
        self.command_list = [
            'NEXT',
            'PREVIOUS',
            'EXIT',
            'NEW',
            'RULES',
            'HELP',
            'RATING'
        ]
        self.min = 9

    def save_game_results(self):
        with open(f"d:\\study_projects\\python_repos\\python_lessons\\MODULE_1\\lesson_14\\{self.player.name}.json", 'w', encoding='utf-8') as f:
            json.dump(self.player.profile, f, ensure_ascii=False)

    def set_player(self):
        print(self.rules)
        
    def ask_word(self):
        self.word = input('Введите слово: ')
        if self.word not in self.command_list:
            print(f'Уровень: {self.current_level}, слово: {self.word}') 
        else: return

    def play_game(self):
        letters = get_word_letters(self.word)
        solution_list = []
        while len(solution_list) <= self.min:
            print(f"УРОВЕНЬ: {self.current_level}")
            print(f"СЛОЖНОСТЬ: {'ЛЕГКИЙ' if self.current_level < 5 else 'СЛОЖНЫЙ'}")
            print(f"СЛОВО:  {self.word}")
            print(f"ВАРИАНТОВ: 30")
            print(f"НЕОБХОДИМО УГАДАТЬ: 9")
            print(f"УГАДАННО СЛОВ: {len(solution_list)}")
            print(f"ДО СЛЕДУЮЩЕГО УРОВНЯ: {30 - len(solution_list)}")
            print(f"БУКВЫ: {letters}")
            print(f"УГАДАННЫЕ СЛОВА: {solution_list}")
            solution = input('Составьте слово: ')
            word_list = create_word_list(self.word)
            if solution in word_list:
                solution_list.append(solution)
            else:
                print(f"\nСлова '{solution}' нет в списке слов\n")
        self.player.profile['current_level'] = self.current_level
        self.player.profile.update({f"level_{self.current_level}": {
                "word": self.word, 
                "letters": letters, 
                "variants": 30, 
                "answers": solution_list, 
                "guessed": len(solution_list), 
                "need_to_next_level": self.min,
                "is_done": True if len(solution_list) >= self.min else False,
                }})
        self.save_game_results()
        self.game_flag = False
    
   
    def start_game(self):
        self.set_player()
        self.ask_word()

        while self.current_level != 10:
            if check_word(self.word) == False:
                self.game_flag = False
                break
            else: 
                while self.game_flag == True:
                    self.play_game()
                question = input('Вы угадали необходимое кол-во слов для перехода на следующий уровень. \nЕсли хотите продолжить, введите NEXT. \nЕсли хотите угадать побольше слов, введите PREVIOUS. \nЕсли хотите выйти из игры, введите EXIT. \nЕсли вы хотите начать игру с самого начала, введите NEW. \nЕсли нужно напомнить правила игры, введите RULES. \nЕсли хотите узнать ваш рейтинг, введите RATING. \nЕсли вам нужно вывести все команды интерфейса игры, введите HELP. ')
                if question == 'NEXT':
                    self.game_flag = True
                    self.ask_word()
                    self.current_level += 1
                    self.player.profile.update({self.player.profile['current_level']: self.current_level})
                    self.min += 2
                    self.play_game()
                elif question == 'PREVIOUS':
                    self.game_flag = True
                    self.ask_word()
                    self.current_level -= 1
                    self.min -= 2
                    self.player.profile.update({self.player.profile['current_level']: self.current_level})
                    self.play_game()
                elif question == 'EXIT':
                    self.game_flag = False
                    self.save_game_results()
                    self.current_level = 1
                    self.player.profile = {}
                elif question == 'NEW':
                    self.game_flag = True
                    self.player.profile = {}
                    self.current_level = 1
                    self.player.profile.update({self.player.profile['current_level']: self.current_level})
                    self.start_game()
                elif question == 'RULES':
                    print(self.rules)
                elif question == 'RATING':
                    print(f"RATING: {(self.player.profile[f'level_{self.current_level}']['guessed'] / self.player.profile[f'level_{self.current_level}']['variants'])*100} + %")
                elif question == 'HELP':
                    print("NEXT - переход на следующий уровень (если вы угадали нужное количество слов)\nPREVIOUS - переход на предыдущий уровень (если хотите угадать большее количество слов)\nEXIT - выход и сохранение прогресса (для PLAYER)\nNEW - стирает весь прогресс и вы начинаете заново\nRULES - выводит правила игры\nRATING - выводит соотношение составленных слов к общему числу вариантов на текущий уровень (то есть, вы на 3 уровне всего 105 слов, угадано 50 - рейтинг 50 / 105 = 0.48 или 48 %,\nHELP - выводит команды интерфейса игры")
                

if __name__ == '__main__':
    game = Game()
    game.start_game()