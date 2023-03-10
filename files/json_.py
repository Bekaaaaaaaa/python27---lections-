"============================JSON============================"
#JavaScript Object Notation - единый формат, в котором
# могут храниться только те типы данных,
# которые есть во всех яз-прог поддерживающие json

# числа itn, float
# строки str
# словари dict
# булевые значения True, False
# списки list
# пустое значение None

import json
# сериализациа - перевод из python в json 
# dump - принимает файл с питона в жс
# dumps - функция которая переводит python обьект в
    #json строку

# десерализация - перевод из json в python
# load - принимает файл с жс питон
# loads - функция которая переводит json строку в 
    #python обьект

print(dir(json))  #показывает подсказки 

python_list = [1,2,3]
json_list = json.dumps(python_list)
print(type(python_list)) #list списки
print(type(json_list)) #str строки

print(python_list) #[1, 2, 3]
print(json_list) #"[1,2,3]"


json_dict = '{"a":1, "b":2}'
python_dict = json.loads(json_dict)

print(type(json_dict)) #<class 'str'>
print(type(python_dict)) #<class 'dict'>



list_ = [
    1,2,3,
    4.5,
    (1,2,3),
    {"A":1},
    'beka',
    True, False, None
]

with open("test.json", "w") as file:
    json.dump(list_, file)


with open("test.json", "r") as file:
    res = json.load(file)

print(res)
#[1, 2, 3, 4.5, [1, 2, 3], {'A': 1}, 'beka', True, False, None]









# with open("test.txt", "w") as file:
#     json.dump(list_, file)