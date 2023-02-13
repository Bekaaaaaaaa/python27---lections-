'===============================comprehension============================'
# генератор, с помощью которого можно создавать последовательность используя цикл for

list1 = []
for i in range(1, 11):
    list1.append(i)
# list1 = [1,2,3,4,5,6,7,8,9,10]

list1 = [i for i in range(1,11)]
# print(list1)  [1,2,3,4,5,6,7,8,9,10]

# результат for элемент in последовательность
# результат for элемент in последовательность if фильтр

comprehension = ( i for  i in range(1,11))
print(comprehension)
# <generator object <genexpr> at 0x7f93c0ca6490>
#генератор - итерируемый обьект, который не хранит в себе полностью
#все элементы последовательности, а генерирует их когда требует

print(next(comprehension))
print(next(comprehension))
print(next(comprehension))
print(next(comprehension))
print(next(comprehension))
#print(next(comprehension))

#next - функция которая принимает в себя генератор,
#запрашивает след. элемент у генератора и возвращает его 

comprehension = (i for i in range(1,4))
print(list(comprehension))#[1, 2, 3]
print(list(comprehension))#[] - еще раз он не выводит, comprehesion - одноразовый

'=====================Синтаксичкский сахар===================='
#list comprehension
list_compr = [i for i in 'hello']
print(list_compr)
#['h', 'e', 'l', 'l', 'o']

# dict comprehension 
dict_compr = { i:str(i) for i in range(1,11) }
print(dict_compr)
#{1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

#фильтр
string = 'HelLo WorLD'
res = [i for i in string if i.islower()]
print(res)
#['e', 'l', 'o', 'o', 'r']

#второй вариант - 
res = []
for i in string:
    if i.islower():
        res.append(i)
#['e', 'l', 'o', 'o', 'r']

list1 = [i for i in range(0,11) if i % 2 == 0]
print(list1)

# set comprehension
set_comp = {x for x in range(10)}
print({1,True,'hello',10,1})
#{1, 10, 'hello'}

#задача на comprehension
list1 = [i for i in range(1,11) if i % 2 == 0]
print(list1)
#[2, 4, 6, 8, 10]


# #умножить на 100
list1 = range(1,11)
res = [i * 100 for i in range(1,11)]
print(res)

#распечать 5 раз 'hello'
res = ['hello' for i in range (5)]
print(res)
#['hello', 'hello', 'hello', 'hello', 'hello']

#соеденить users и hello 
users = ['test1', 'test1', 'test3']
res = ['Hello '+name for name in users]
print(res)
#['Hello test1', 'Hello test1', 'Hello test3']

res = [[x for x in range(1,i+1)]for i in range(1,6)]
print(res)

list1 = [[1,2,3],[4,5,6],[7,8,9]]
res = [1,2,3,4,5,6,7,8,9]
res = [i for inner_list in list1 for i in inner_list]
# res = []
# for inner_list in list1:
#     for i in inner_list:
#         res.append(i)
print(res)


#[1,2,3,4]
#['не четное','четное','не четное','четное']
res = ['четное' if i % 2 == 0 else 'не четное' for i in range(1,7)]
print(res)
#['не четное', 'четное', 'не четное', 'четное', 'не четное', 'четное']

#[[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
res = [[x for x in range(1, i+1)] for i in range(1,6)]
print(res)


#{1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}
res = {i:[x for x in range(1, i+1)] for i in range(1,6)}
print(res)