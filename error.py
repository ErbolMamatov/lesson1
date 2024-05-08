import random


def num():
    first_names = ["beka", "doni", "emil", "joxa", "yrysgul"]
    last_names = ['bekov', 'mamatov', 'emilov', 'kasenov', 'timurov']

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f'{first_name} {last_name}'


print(num())




""" ИГРА """

# import random
#
#
# def number():
#     try:
#         num = random.randint(1, 100)
#         total = 0
#         while True:
#             my_num = int(input('num: '))
#             total += 1
#             if my_num < num:
#                 print('твое  меньше моего')
#             elif my_num > num:
#                 print('твое  больше моего')
#             else:
#                 print(f'Угадал правильно число {num}, за {total} раз')
#                 break
#     except ValueError as a:
#         print('введите целое число', a)
#
#
# number()

























