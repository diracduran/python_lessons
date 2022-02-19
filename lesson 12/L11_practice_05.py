# -*- coding: utf-8 -*-
# L11_practice_05.py
"""
1. Создайте класс Student(), который будет относиться ко всем студентам
2. У студентов есть общие атрибуты имя (name), фамилия (lastname), возраст (age)
3. Также есть атрибут изучаемых дисциплин, который хранится в виде списка по умолчанию (lessons):
["Программирование", "Базы Данных", "Алгоритмы"]
4. Добавьте 2 метода:
    1) show_student() - выводит на экран информацию о студенте: Фамилия, Имя, возраст
    2) show_disciplines() - выводит на экран Фамилию студента, далее построчно информацию об изучаемых дисциплинах
    
5. В созданном классе Student(), добавьте еще 1 метод:
    1) add_discipline() - добавляет новую дисциплину в список для обучения
6. Создайте экземпляры класса Student() в переменных student_3, student_4
7. Примените к student_3, student_4 методы show_student() и show_disciplines()
8. Вам дан список дисциплин на выбор:
disciplines = ["Основы Python", "Основы JavaScript", "Основы Java", "Основы С++"]
9. Добавьте по две дисциплины из списка disciplines к student_3, student_4, используя метод add_discipline() 
10. Выведите на экран изучаемые дисциплины для каждого студента (student_3 и student_4)

P.S. В задании пункты 1-4 выполняли в задании L11_practice_04.py
"""

class Student():
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.lessons = ["Программирование", "Базы Данных", "Алгоритмы"]
    
    def show_student(self):
        print(f'Full name: {self.name} {self.lastname}, age: {self.age}')
    def show_disciplines(self):
        print(f'Student {self.lastname}: \n')
        for lesson in self.lessons:
            print(lesson)
    def add_discipline(self, new_lesson):
        self.lessons.append(new_lesson)
        


student_3 = Student('John', 'Deacon', 22)
student_3.show_student()
student_3.show_disciplines()
student_4 = Student('Alice', 'Cooper', 21)
student_4.show_student()
student_4.show_disciplines()

disciplines = ["Основы Python", "Основы JavaScript", "Основы Java", "Основы С++"]

student_3.add_discipline(disciplines[0])
student_3.add_discipline(disciplines[1])
student_4.add_discipline(disciplines[2])
student_4.add_discipline(disciplines[3])
student_3.show_disciplines()
student_4.show_disciplines()