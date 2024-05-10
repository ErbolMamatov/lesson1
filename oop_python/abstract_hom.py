"""
Представьте, что вы создаете систему управления учебным планом для университета.
Ваша система должна иметь возможность хранить информацию о курсах и студентах, а также выполнять различные операции, такие как добавление нового курса,
 регистрация студента на курс, оценка студента и т. д.

Вам нужно создать следующие классы:

Абстрактный класс Course, который представляет курс в университете. У курса должны быть атрибуты, такие как название курса,
 преподаватель, количество кредитов и список зарегистрированных студентов.
  Также должны быть реализованы абстрактные методы для добавления студента на курс и выставления оценки студенту.
Класс Student, представляющий студента в университете.
 У студента должны быть атрибуты, такие как имя, фамилия, номер студенческого билета и список курсов, на которые он зарегистрирован.
  Также должны быть реализованы методы для регистрации студента на курс и получения его средней оценки.
Класс University, который будет представлять университет и хранить информацию о всех курсах и студентах.
 Этот класс должен иметь методы для добавления нового курса, регистрации студента на курс, выставления оценки студенту и т. д.
Реализуйте эти классы и их методы таким образом, чтобы они соответствовали описанным требованиям.
"""
from abc import ABC, abstractmethod


class Course(ABC):
    name_curs = ''
    teacher = ''
    col_credit = 0
    all_students = ''

    def __init__(self):
        Course.all_students += 1
        Course.name_curs += self.name_curs
        Course.teacher += self.teacher
        Course.col_credit += 1

    @abstractmethod
    def info_curs(self):
        return f'название курса - {self.name_curs}\n перподователь - {self.teacher}\n количество кредитов - {self.col_credit}'


class Student(Course):
    def __init__(self, name, surname, number_student_card):
        self.name = name
        self.surname = surname
        self.number_student_card = number_student_card
        self.course_lists = []

    def grade(self, student_grade):
        if student_grade <= 3:
            print('низкая оценка')
        else:
            print('хорошая оценка')

    def info_student(self):
        return f' имя студента - {self.name} фамилия - {self.surname}\n номер студенческой карты: {self.number_student_card}'


class University:
    def info_teacher(self, teachers_name):
        return teachers_name

    def add_course(self, nev_curse_name):
        # self.course_lists.append(nev_curse_name)
        # print(self.course_lists)

    # def nev_curs_info(self):
        # return f'новый преподователь {self.teachers_name}, название нового курса {self.nev_curse_name}'


curs = Course('programmer', 'Baktyar', 1000)
print(curs.info_curs())
student = Student('Tom', 'Temirlanov', 563412)
print(student.info_student())
student.grade(4)
print('-----------------------------')
# univer = University
# print(univer.info_teacher('Tommm'))



