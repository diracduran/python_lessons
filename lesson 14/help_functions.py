

"""
В файле help_functions.py написаны 3 функции:
1.    check_word(word: str) - функция принимает в качестве аргумента слово (str) и возвращает кортеж из 2-х элементов: (True или False, количество вариантов). Если первый элемент кортежа False, то слово не подходит для игры.
2.    get_word_letters(word: str) - функция принимает в качестве аргумента слово (str) и возвращает список букв в порядке их следования в переданном слове
3.    create_word_list(word: str) - функция принимает в качестве аргумента слово и возвращает список возможных слов, с учетом правил (каждое слово >= 3 буквы)
"""
import csv



# считывание БД слов с определениями nouns.csv и сохранение в виде словаря "слово": "определение" в переменную WORDS_WITH_DEFINITIONS
with open("d:\\study_projects\\python_lessons\\lesson_14\\nouns.csv", "r", encoding='utf-8') as csv_file:
	reader = csv.reader(csv_file, delimiter=',') # объект csv для чтения функция reader
	data = [] # пустой список для сохранения прочитанных данных
	for row in reader:
		data.append(row) # добавление в список
	WORDS_WITH_DEFINITIONS = {w[0]: w[1] for w in data[1:]}


def get_word_letters(word: str):
	"""
	функция принимает в качестве аргумента слово (str) и возвращает список букв в порядке их следования в переданном слове (проверяет также, есть ли слово в БД)
	"""
	if word not in list(WORDS_WITH_DEFINITIONS.keys()):
		print(f"{word} нет в списке слов")
		return None # если слова нет в БД слов, то возвращает None
	return list(word)

def check_word(word: str):
	"""
	функция принимает в качестве аргумента слово (str) и возвращает кортеж из 2-х элементов: (True или False, количество вариантов). Если первый элемент кортежа False, то слово не подходит для игры.
	"""
	if word not in list(WORDS_WITH_DEFINITIONS.keys()):
		print(f"{word} нет в списке слов")
		return None
	word_list_len = len(create_word_list(word))
	if word_list_len >= 30:
		return (True, word_list_len)
	else:
		return (False, word_list_len)

def create_word_list(word: str):
	"""
	функция принимает в качестве аргумента слово и возвращает список возможных слов, с учетом правил (каждое слово >= 3 буквы)
	"""
	if word not in list(WORDS_WITH_DEFINITIONS.keys()):
		print(f"{word} нет в списке слов")
		return None
	word_list = []
	letters = list(word)
	for word_ in list(WORDS_WITH_DEFINITIONS.keys()):
		if len(word_) <= 2:
			continue
		letters_ = letters[:]
		flag = True
		for w in word_:
			if w not in letters_:
				flag = False
				break
			else:
				letters_.remove(w)
		if flag:
			word_list.append(word_)
	word_list.remove(word) # убираем из списка главное слово
	return word_list

print(get_word_letters('дриада'))
print(check_word('мексиканец'))
print(create_word_list('мексиканец'))
