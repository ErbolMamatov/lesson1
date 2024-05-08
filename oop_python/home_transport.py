"""
Допустим, вы разрабатываете программу для моделирования различных видов транспорта.
Вам нужно создать абстрактный класс Transport, который будет представлять общие характеристики и методы для всех видов транспорта.
Затем вы будете создавать конкретные классы для каждого типа транспорта, например, Car, Bicycle, Plane и т. д.

Вот что должен содержать абстрактный класс Transport:

Абстрактный метод move, который будет моделировать перемещение транспорта.
Абстрактный метод stop, который будет моделировать остановку транспорта.
Ваша задача состоит в том, чтобы создать абстрактный класс Transport и добавить абстрактные методы move и stop.
Затем создайте несколько конкретных классов (например, Car, Bicycle, Plane) и реализуйте эти методы для каждого из них в соответствии с их поведением
"""
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def move(self):
        ...

    def stop(self):
        ...


class Car(Transport):
    def __init__(self, name):
        self.name = name

    def move(self):
        return f'{self.name} едет'

    def stop(self):
        return f'{self.name} остановился'


car = Car('Audi')
car2 = Car('mers')

print(car.move())
print(car.stop())
print('-------------')
print(car2.move())
print(car2.stop())
