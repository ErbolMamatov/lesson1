# lambda

# summa = lambda a,b,c:a + b + c
# print(summa(2,2,2))


# проверяет есть ли слово Python:

# text = lambda s: "Python" in s
# print(text("erbol"))


#******************************************************************************************************************************
# from functools import reduce
# numbers = [10, 20, 30, 40, 50]
#
# average = reduce(lambda x, y: x + y, numbers) / len(numbers)
#
# print("Среднее значение:", average)
#*******************************************************************************************************************************


# last = lambda lst: lst[-1]
#
# # Ваш список
# my_list = [1, 2, 3, 4, 5]
#
# # Получаем последний элемент списка
# l = last(my_list)
#
# # Выводим результат
# print(l)


# a = "привет"
# b = "мир"



# log = lambda a,b:a + b
# a = "привет "
# b = "мир"
# print(log(a, b))




# agre = dict(name='Erbol',age=17)
# print(agre.values())


# firstname = input("имя ")
# lastname = input("фамилия ")
# age = int(input("возраст "))
# user = dict(firstname=firstname,lastname=lastname,age=age)
# print(user)



# e = int(input("количество друзей: "))
# slovo = {}
# for _ in range(e):
#     name_g = input("имя: ")
#     age_g = input("возраст: ")
#     slovo[name_g] = age_g

# print(slovo)

# print(slovo.values())

# print(slovo.keys())

# for i, value in slovo.items():
#     print(i, value)



# coutris = {'Kyrgyzstan': 'Bishkek','Rossian':'Moscov'}
# Rossian = coutris.pop('Rossian')
# print(Rossian)
