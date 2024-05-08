# class Animal:
#     def speak(self):
#         print('животное издает звук')
#
# class Dog(Animal):
#     def speak(self):
#         print('собака лает')
#


# class Shape:
#     def __init__(self, area):
#         self.area = area
#
#     def area(self):
#         return self.area
#
# class Rectangle(Shape):
#     def __init__(self, area, height, width):
#         super().__init__(area)
#         self.height = height
#         self.width = width
#
#     def area(self):
#         return self.height * self.width
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def display_name(self):
#         print(f'i am {self.name}')
#
# class Employee(Person):
#     def __init__(self, name, pozishn):
#         super().__init__(name)
#         self.pozishn =pozishn
#
# class Menager(Employee):
#     def __init__(self, name, pozishn, department):
#         super().__init__(name, pozishn)
#         self.department =department
#
#     def display_name(self):
#         super().display_name()
#         print(self.pozishn)
#         print(self.department)
#
#
# men = Menager('kuba', 'menejer', 'it')
# men.display_name()







# class Animal:
#     def __init__(self, name, legs, eyes, color):
#         self.name = name
#         self.legs = legs
#         self.eyes = eyes
#         self.color = color
#
#     def info(self):
#         print(f'name {self.name}, legs {self.legs}, eyes {self.eyes}, color {self.color}')
#
# animal = Animal('Laika', 4, 2, 'black')
# animal.info()
#
#
#
# class Cat(Animal):
#     def __init__(self, name, legs, eyes, color, tail):
#         super().__init__(name, legs, eyes, color)
#         self.tail = tail
#
#     def info(self):
#         super().info()
#         print(self.tail)
#
# cat = Cat('log', 4, 2, 'Yellow', 30)
# cat.info()
#
#
# class Dog(Animal):
#     def __init__(self, name, legs, eyes, color, zub):
#         super().__init__(name, legs, eyes, color)
#         self.zub = zub
#
#     def info(self):
#         super().info()
#         print(self.zub)
#
# dog = Dog('jeck', 4, 2, 'Red', 32)
# dog.info()








# class Employee:
#   def __init__(self):
#       pass
#
#
# class Developer(Employee):
#
#     def __init__(self, name, menejer, razrab, dizainer):
#         self.__name = name
#         self.__dizainer = dizainer
#         self.__menejer = menejer
#         self.__razrab = razrab
#
#     def info(self):
#         print(f'name: {self.__name} , menejer: {self.__menejer} , razrab: {self.__razrab} , dizainer: {self.__dizainer}')
#
#
# mojang = Developer('Mojang', 'Jek', 'Nikita', 'Robert')
# mojang.info()









# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
# class Cat(Animal):
#     def __init__(self, name, color, tail):
#         super().__init__(name, color)
#         self.tail = tail
#
#     def info(self):
#         print(f'name {self.name} color {self.color} tail {self.tail}')
#
#
# cat = Cat('Tom', 'Black', 30)
# cat.info()




# class Car:
#     def __init__(self, glass, door, wheels, color):
#         self.__glass = glass
#         self.__door = door
#         self.__wheels = wheels
#         self.color = color
#
#     @property
#     def glass(self):
#         return self.__glass #стекло
#
#     @property
#     def door(self):
#         return self.__door #дверь
#
#     @property
#     def wheels(self):
#         return self.__wheels #колеса
#
#
# class Bmw(Car):
#     def __init__(self, glass, door, wheels, color, sitting, pedal, leather):
#         super().__init__(glass, door, wheels, color)
#         self.sitting = sitting
#         self.pedal = pedal
#         self.leather = leather
#
#     def info(self):
#         print(f'стекло: {self.glass} дверь {self.door} колеса: {self.wheels} цвет: {self.color} сидение: {self.sitting} педаль: {self.pedal} кожа: {self.leather} ')
#
#
# bmw = Bmw(6, 4, 4, 'Black', 4, 2, 'Red')
# bmw.info()























