from abc import ABC, abstractmethod


class Course(ABC):
    def __init__(self, name_curs, teacher, col_credit):
        self.name_curs = name_curs
        self.teacher = teacher
        self.col_credit = col_credit

    def info_curs(self):
        return f'название курса - {self.name_curs}\n перподователь - {self.teacher}\n количество кредитов - {self.col_credit}'


class Student(ABC):
    def __init__(self, name, surname, number_student_card, course_lists):
        self.name = name
        self.surname = surname
        self.number_student_card = number_student_card
        self.course_lists = course_lists

    def grade(self, student_grade):
        if student_grade <= 3:
            print('низкая оценка')
        else:
            print('хорошая оценка')

    def info_student(self):
        return f' имя студента - {self.name} фамилия - {self.surname}\n номер студенческой карты: {self.number_student_card}'


# class University:
#     def info_teacher(self, teachers_name, nev_curse_name):
#         self.teachers_name = teachers_name
#         self.nev_curse_name = nev_curse_name
#
#     # def registration(self):
#     #     return (f' имя нового студента {self.name} фамилия {self.surname}\n номер студенческой карты {self.number_student_card}'
#     #             f' список курсов {self.course_lists}')
#
#     def nev_curs_info(self):
#         return f'новый преподователь {self.teachers_name}, название нового курса {self.nev_curse_name}'


curs = Course('programmer', 'Baktyar', 1000)
print(curs.info_curs())
student = Student('Tom', 'Temirlanov', 563412, 'programmer')
print(student.info_student())
student.grade(4)
print('-----------------------------')


