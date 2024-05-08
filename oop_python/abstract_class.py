# from abc import ABC, abstractmethod
#
#
# class Car(ABC):
#
#     @abstractmethod
#     def speed(self):
#         ...
#
#     def color(self):
#         ...
#
#
# class Mers(Car):
#     def __init__(self, speeds, colors):
#         self.speeds = speeds
#         self.colors = colors
#
#     def speed(self):
#         return f'{self.speeds}'
#
#     def color(self):
#         return f'{self.colors}'
#
#
# class Audi(Car):
#     def __init__(self, years, price):
#         self.years = years
#         self.price = price
#
#     def speed(self):
#         return f'100'
#
#     def color(self):
#         return f'500'
#
#     def __str__(self):
#         return f'{self.years}\n{self.price}'


# mers = Mers(120, 'Black')
#
# print(mers.speed())
# print('')
# print(mers.color())

audi = Audi(2010, 500)
print(audi.speed())
print(audi.color())
print(audi)

