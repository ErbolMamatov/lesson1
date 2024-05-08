# def num(a):
#     if a < 0:
#         raise Exception('меньше нуля')
# try:
#     num(-1)
# except Exception as e:
#     print('ERROR', e)



# def num(a,b):
#     if not (isinstance(a,int) and (isinstance(b,int))):
#         raise TypeError('должна быть цифра')
#     return a + b
# try:
#     print(num(1,2.3))
# except TypeError as e:
#     print('error', e)



# def num(a,b):
#     if b == 0:
#         raise ZeroDivisionError('ненадо 0')
#     return a/b
# try:
#     print(num(3,0))
# except ZeroDivisionError as e:
#     print('ошибка', e)




# def num(a):
#     if (isinstance(a,int)):
#         raise TypeError('не правельно')
#     if a % 2 != 0:
#          raise ValueError('ошибка2')
#     return a
# try:
#         print(num(5))
# except TypeError:
#         print("ошибка номер 2")
# except ValueError:
#     print('ошибкка 3')
# except Exception as e:
#     print('конец')
