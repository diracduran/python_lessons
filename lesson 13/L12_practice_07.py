# -*- coding: utf-8 -*-
# L12_practice_07.py
"""
1. Создайте класс University, который описывает университет.
2. У класса University есть Переменные экземпляра класса: title (название), city(город)
3. Также у Класса University есть Переменные класса: students (список студентов), teachers (список учителей)
4. Напишите метод класса University, add_person(new_person), где new_person (студент или учитель - определяется с использованием композиции классов Student и Teacher).
5. Каждый раз, когда идет зачисление в университет списки должны пополняться в зависимости от того, кем является person
6. Поэтому необходимо создать 2 класса: Student и Teacher, оба имеющие атрибуты (переменные экземпляра класса), role (пораметр по умолчанию 'студент' или 'учитель'). Помимо этого, атрибуты: name (имя), lastname (фамилия), age (возраст).
7. Напишите метод для класса University, show_student_list() - выводит всех студентов, show_teacher_list() - выводит всех учителей. Формат вывода на экран: название университета, город, имя, фамилия, возраст, роль
8. Создайте 3 университета и зачислите по 3 студента и по 2 учителя в каждый.
"""

class University:
    students = []
    teachers = []
    def __init__(self, title, city):
        self.title = title,
        self.city = city

    def add_person(self, new_person):
        if new_person.role == 'student':
            self.students.append(new_person)
        elif new_person.role == 'teacher':
            self.teachers.append(new_person)
    
    def show_student_list(self):
        for student in self.students:
            print(student)

    def show_teacher_list(self):
        for teacher in self.teachers:
            print(teacher)

class Student:
    def __init__(self, name, lastname, age):
        self.name = name,
        self.lastname = lastname,
        self.age = age,
        self.role = 'student'

class Teacher:
    def __init__(self, name, lastname, age):
        self.name = name,
        self.lastname = lastname,
        self.age = age,
        self.role = 'teacher'
