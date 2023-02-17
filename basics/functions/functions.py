'=======================================Функции===================================='
#функции - именованный блок кода который принимает аргументы и возвращает результат


# my_sum - lambda num1, num2: num1 + num2 
# res - my_sum(5,10)
# print(res)#15
#lambda - ключевое слово для создания анонимной функции

def my_sum2(num1,num2):
    return num1 + num2
print(my_sum2) #<function my_sum2 at 0x7f2294367d90>
res = my_sum2(13, 45)
print(res) #58

def calc(num1, num2, oper):
    """
     oper - строка, с операцией для вычеслеий
     "+" - сложение
     "-" - вычитание

     """
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2
    if oper == '/':
        return num1 / num2

print(calc(10, 12, '+')) #22
print(calc(10, 12, '-')) #12
print(calc(10, 12, '*')) #20
print(calc(10, 12, '/')) #3.0
print(calc(11, 23, '5')) #none

def my_len(obj):
    "возвращает длину обьекта"
    count = 0
    for i in obj:
        count += 1
        #count = count + 1
    return count
print(my_len([15,23,14,64,12])) #5
print(my_len('asvdsvf')) # 7
print(my_len({'a':1, 'b':2}))# 2

def super_len(obj):
    try:
        return my_len(obj)
    except TypeError:
        #если не можем будем итерировать его в виде строки 
        return my_len(str(obj))
    
print(super_len([1,2,3,4])) # 4
print(super_len(123456789)) # 9 (123456789)
print(super_len(None)) #4 ('None) - 4 буквы

'======================================DRY======================================'
#DRY - don't repeat yourself (не повторяйся)

# представим у нас енет функции len 

"===========================аргументы и параметры============================="
# парметры  - локальные переменные, знвсения еоторые мы задаем при вызове функции
# #аргументы  - значения которые мы задаем параметрам при вызове функции


def func(var):
    local_var = 5
    print(locals())
    #{'var': 6, 'local_var': 5}

func(6)
#print(local_var) NameError: name 
#print(var) NameError

"==================================виды параметров================================="
#1.обязательные 
#2.необязательные 
#2.1 с дефолтным значением (по умолчаню)
#2.2 args (arguments)
#2.3kwargs (key word arguments)

def func(a, b='deafault', *args, **kwargs):
    # args - tuple, куда попадут все позиционные
    # kwargs - dict, куда попадут все именованные аргументы,
    #которые не попали по имени
    print(a,b, args, kwargs)

func('hello') #hello deafault
func('hello', '100')#hello 100
func('hello',100, 84, 23, 'world')#hello 100 (84, 23, 'world')

func('hello', 100, 10, 20, 30, key1='value1', key2=500)
# 'hello' 100 (10, 20, 30) {'key1': 'value1', 'key2': 500}


"======================================виды агументов======================================"
#позиционные (по порядку параметров)
#именнованные ( по имени параметров)

def func2(a, b):
    print(f"a={a}, b={b}")

func2(10, 20)# позиционно
#a=10, b=20
func2(b=23, a=20) #именованно передает нам по порядку 
#a=20, b=23


"+======================звездочки=========================="
list1 = [1,2,3]
list2 = [*list1]# * - распаковывает 
print(list2)#грубо говоря копирует в новую ячейку
[1, 2, 3]


dict1 = {'a':1, 'b':2}
list3 = [*dict1]
# list3 = ['a', 'b']
dict2 = {**dict1}
#dict2 = {'a':1, 'b':2}