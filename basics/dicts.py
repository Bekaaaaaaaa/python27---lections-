"=====================================СЛОВАРИ==========================================="
# dict - изменяемый, интерируемый, неупорядочный, неиндексируемый тип данных
#преднахначенный для хранения данных в парах (ключ:значение)


user = {
    'name':'Beka'
    'age': 13
    'last_name':'BKR'
}
print(user['name']) # 'Beka'
print(user['age'])  # 13
 


list = [10,20,30]
{
    0:10
    1:20
    2:30
}
# ключи в словаре будут уникальными, поэтому если в словарь добавить 
#значение по уже существующему ключу, то сохранится последнее значение 
dict = {'a':1, 'b':2, 'a':3}
#{'a':3, 'b':2}
a = 2
b = 2
a = 3
# a = 3, b = 3

# Ключами могут быть только хешируемые типы данны (неизменяемые типы данных)

dict = {'a':1, 'b':2, 'a':3}
#dict1['d'] #keyError: 'd'

"--------------------------Создание------------------------"
dict1 = {'a':1, 'b':2, 'a':3}
dict1 = dict1([('a', 1), ('b', 2)])
# {'a':1, 'b':2}

list1 = ['a', 'b', 'c']
list2 = [1,2,3]
dict3 = dict(zip(list1, list2))
# {'a':1, 'b':2, 'c':3}

"=============================Методы словаря========================="
# get - метод который принимает в себя ключ.
# Если такого ключ есть - возвращает его значение.
# Если такого ключа нет - возвращает None  (или его )

user = {
    'name':'Beka'
    'age': 13
    'last_name':'BKR'
}
# user['id'] # KeyError: 'id'
user.get('id') #NOne
user.det('name')#'Beka'
user.get('id',default=10)# 10
user.get('age', 20) #13
#default (значение по умолчанию) - возвращается если ключа нет
# если етсь ключ, возвращается его значение



#pop - метод который принимает ключ, удфлят пару под этим ключом.
#возвращает удаленное значение 
dict1 = {'a':10, 'b':20, 'a':30}
res = dict1.pop('a')
print(dict1) #{'b':20, 'a':30}
print(res) #10


#popitem - метод который удаляет пару, которая была добавлена последней в словарь
dict1 = {'a':10, 'b':20, 'c':30}
res = dict1.popitem()
print(dict1) # {'a':10, 'b':20}
print(res) # ('c', 30)



#update - расширяет словарь, вторым словарем



"--------------------------keys, values, items---------------------------"
# keys - возвращает список ключей
# values - возвращает список значений
# items - возвращает список из пар (ключ, значение)





'============================Итерируемые словари=========================='
user = {
    'name':'Beka'
    'age': 13
    'last_name':'BKR'
}

for i in user:

    print(i)


list1 = [1,2,3]
list2 = ['a', 'b', 'c']
dict3 = dict(zip(list1, list2))