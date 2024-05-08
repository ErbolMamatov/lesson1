# class Mbank:
#
#     def __init__(self, owner, balance):
#         self.__owner = owner
#         self.__balance = balance
#     @owner.setter
#     def owner(self, owner):
#         self.__owner = owner
#
#     @property
#     def owner(self):
#         return self.__owner
#
#     def get_balance(self):
#         return self.__balance
#
#     def mbank(self):
#         print(f'Владелец: {self.__owner} ваш баланс: {self.__balance}')
#
#
# bank = Mbank('Nikita', 5000)
# bank.mbank()
# bank.set_owner = 'Erbol'




# class Accaunt:
#     def __init__(self, name, age, gmail):
#         self.name = name
#         self.__age = age
#         self.gmail = gmail
#
#     @property
#     def age(self):
#         return self.__age
#
#     def name(self):
#         return self.name
#
#     def human_info(self):
#         print(f'{self.name}, {self.__age}, {self.gmail}')
#
# info = Accaunt('Tommi', 20, 'tommi_nikitov')
# info.human_info()
# info.name = 'erbol'
# info.age=110





# class Animal:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.__age = age
#         self.color = color
#
#     @property
#     def age(self):
#         return self.__age
#
#     def show_info(self):
#         print(f'{self.name}, {self.__age}, {self.color}')
#
# class Zebra(Animal):
#     def sey(self):
#         print('zebra alot')
#
# class Buka(Animal):
#
#     def byka(self):
#         print('bykyit')
#
# def erbol(animal):
#     if isinstance(animal, Animal):
#         animal.show_info()
#
#     elif isinstance(animal, Zebra):
#         animal.sey()
#
#     elif isinstance(animal, Buka):
#         animal.byka()
#
#
# animal = Animal('erbol', 20, 'yllow')
# zebra = Zebra('zebr', 10 , 'black')
# buka = Buka('bukka', 30, 'lrsfv')
#
# erbol(animal)
# erbol(zebra)
# erbol(buka)







class Animal:

    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"{self.name} Animal")


class Zebra(Animal):
    def sey(self):
        print(f"{self.name} Zebra")


class Buka(Animal):

    def byka(self):
        print(f"{self.name} Buka")


def erbol(animal):
    if isinstance(animal, Zebra):
        animal.sey()

    elif isinstance(animal, Buka):
        animal.byka()

    elif isinstance(animal, Animal):
        animal.show_info()


animal = Animal('animal')
zebra = Zebra('zebra')
buka = Buka('buka')

erbol(animal)
erbol(zebra)
erbol(buka)










