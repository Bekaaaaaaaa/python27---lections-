# "=================================Декоратор=================================="
# #декоратор - это функция высшего порядкакоторая нужна
# #чтобы расширять фнкционал другой функции не меняя ее

# def decorator(func):
#     def wrapper():
#         print('функция вызывается')
#         func()
#         print('функция завершила работу')
#     return wrapper


# def func():
#     print('hello')

# res = decorator(func)
# print(res)
# #<function decorator.<locals>.wrapper at 0x7f6ef77863b0>
# res()
# #функция вызывается
# # hello
# # функция завершила работу



# "=====================Синтаксический сахар====================="
# def decorator(func):
#     def wrapper():
#         print('функция вызывается')
#         func()
#         print('функция завершила работу')
#     return wrapper

# @decorator #func = decorator(func)
# def func():
#     print('hello')

# func()
# # функция вызывается
# # hello
# # функция завершила работу


# # @decorator
# def func(string):
#     print(string)



# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrapper 



# from datetime import datetime

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         func(*args, **kwargs)
#         end = datetime.now()
#         print(f'Функция отработала за {end-start}')
#     return wrapper

# @timer
# def func(count):

#     for i in range(count):
#         print(i)
    
# func(10)
# Функция отработала за 0:00:00.000142

# @cache - 



# <b>text</b> - жирный
# <i>text</i> - курсив
def bold(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<b>{res}</b>'
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<i>{res}</i>'
    return wrapper

@bold
@italic
def func(string):
    return f'Hello {string}' # <b><i>Hello Makers</i></b>

# func = bold(italic(func))
print(func('Makers'))



# в * args пойдут значения ввиде кортежа 
# а в **kwargs - пойдут именованные значения 