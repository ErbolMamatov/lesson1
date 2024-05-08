# class Tom:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def cats(self):
#         print(f'my name is: {self.name} i am: {self.age}')
#
#
# cat = Tom('TOM',3)
# cat.cats()
#
#
#
#
# class Stydents:
#
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
#     def stud(self):
#         print(f'my name is {self.name} i am {self.age} years old. i am a {self.course} students')
#
#
# stu = Stydents('Tommy', 20, 3)
# stu.stud()
#
#
#
#
#
#
#
# class Book:
#
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def book(self):
#         print(f'name books {self.title} author {self.author} year {self.year} ')
#
#
# book = Book('AZBUKA', 'Erbol.M', 1999)
# book.book()
# print(book.author)
# print(book.title)
# print(book.year)
#
#
#
#
# class Shopss:
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def sps(self):
#         print(f'name of shop {self.name} apple price {self.price} quantity in stock {self.quantity}')
#
#
# shop = Shopss('GLOBUS', 20, 50)
# shop.sps()
#
#
# class Person:
#     def init(self, name, age):
#         self.name = name  # устанавливаем имя
#         self.age = age  # устанавливаем возраст
#
#     @property
#     def age(self):
#         return self.age
#
#     @age.setter
#     def age(self, age):
#         if 0 < age < 110:
#             self.age = age
#         else:
#             print("Недопустимый возраст")
#
#     @property
#     def name(self):
#         return self.name
#
#     def print_person(self):
#         print(f"Имя: {self.name}\tВозраст: {self.age}")
#
#
# tom = Person("Tom", 39)
#
# tom.age = 111
# print(tom.age)
#
# """
# Инкапсуляция
#
# name
# __age
#
# @property - геттер
# @age.setter - сеттер
# @name.setter - сеттер
#
# """
#
#
# class Person:
#     def init(self, name, age):
#         self.name = name  # устанавливаем имя
#         self.age = age  # устанавливаем возраст
#
#     def set_age(self, age):
#         if 0 < age < 110:
#             self.age = age
#         else:
#             print("Недопустимый возраст")
#
#     def get_age(self):
#         return self.age
#
#     # геттер для получения имени
#     def get_name(self):
#         return self.name
#
#     def print_person(self):
#         print(f"Имя: {self.name}\tВозраст: {self.__age}")
#
#
# tom = Person("Tom", 39)
# tom.print_person()
#
# tom.set_age(30)
# tom.print_person()
# print(tom.get_age())
# print(tom.get_name())
#
#
#
#
#
#
#
# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.__age = age
#         self.__color = color
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 0 < age < 100:
#             self.__age = age
#         else:
#             print("недопустимый воз")
#
#
#
#     def cat_info(self):
#         print(f'{self.name}, {self.__age}, {self.__color}')
#
# cat = Cat('Tom', 5, 'yellow')
# cat.cat_info()
#
# cat.age=3000
#















