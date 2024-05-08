class Animal:
    def __init__(self, dog):
        self.dog = dog


class Dog(Animal):
    def info(self):
        print(f'{self.dog} лает !!')


dog = Dog('Laika')
dog.info()





# class Hom:
#     def __init__(self, com_1):
#         self.com_1 = com_1
#
#
# class Com(Hom):
#     def comnata(self, com_2):
#         self.com_2 = com_2
#
#
# class Resultat(Com):
#     def info(self):
#         print(f"цвет первой комнаты{self.com_1} и цвет второй комнаты {self.com_2} ")
#
#
# result = Resultat('белый', 'серый')
# result.info()

























