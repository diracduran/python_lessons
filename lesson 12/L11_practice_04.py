# -*- coding: utf-8 -*-
# L11_practice_04.py
"""
1. Создайте класс Student(), который будет относиться ко всем студентам
2. У студентов есть общие атрибуты имя (name), фамилия (lastname), возраст (age)
3. Также есть атрибут изучаемых дисциплин, который хранится в виде списка по умолчанию (lessons):
["Программирование", "Базы Данных", "Алгоритмы"]
4. Добавьте 2 метода:
    1) show_student() - выводит на экран информацию о студенте: Фамилия, Имя, возраст
    2) show_disciplines() - выводит на экран Фамилию студента, далее построчно информацию об изучаемых дисциплинах
5. Создайте экземпляры класса Student() в переменных student_1, student_2
6. Примените к student_1, student_2 методы show_student() и show_disciplines()
7. Вам дан список дисциплин на выбор:
disciplines = ["Основы Python", "Основы JavaScript", "Основы Java", "Основы С++"]
8. Добавьте по две дисциплины из списка disciplines к student_1, student_2, изменяя атрибут lessons напрямую
9. Выведите на экран изучаемые дисциплины для каждого студента
"""

class Student:
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


student_1 = Student('John', 'Deacon', 22)
student_1.show_student()
student_1.show_disciplines()
student_2 = Student('Alice', 'Cooper', 21)
student_2.show_student()
student_2.show_disciplines()

disciplines = ["Основы Python", "Основы JavaScript", "Основы Java", "Основы С++"]

student_1.lessons.append(disciplines[0])
student_1.lessons.append(disciplines[1])
student_2.lessons.append(disciplines[2])
student_2.lessons.append(disciplines[3])
student_1.show_disciplines()
student_2.show_disciplines()